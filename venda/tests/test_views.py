import json
from unittest import mock
from django.test import TestCase, Client, RequestFactory
from venda.models import Carrinho, Usuario, Produto, ItemCarrinho
from venda.views import pagamento
from django.urls import reverse


class CarrinhoTestView(TestCase):

    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')
        self.produto1 = Produto.objects.create(
            nome='produto1',
            preco=1000.00,
            id=1,
        )
        self.produto2 = Produto.objects.create(
            nome='produto2',
            preco=1000.00,
            id=2,
        )
        self.carrinho = Carrinho.objects.create(user=self.user)

        self.itemcarrinho1 = ItemCarrinho.objects.create(
            produto=self.produto1,
            carrinho=self.carrinho,
            quantidade=1
        )
        self.itemcarrinho2 = ItemCarrinho.objects.create(
            produto=self.produto2,
            carrinho=self.carrinho,
            quantidade=2
        )

        self.client = Client()
        self.data = {'id': self.produto1.id}
        self.data2 = {'id': self.produto2.id}
        self.payload = json.dumps(self.data)
        self.payload2 = json.dumps(self.data2)

    def test_valor_do_carrinho(self):
        valor_carrinho = (
                    self.itemcarrinho1.quantidade * self.itemcarrinho1.produto.preco + self.itemcarrinho2.quantidade * self.itemcarrinho2.produto.preco)
        self.assertEquals(self.carrinho.subtotal_carrinho, f"{valor_carrinho:.2f}")

    def test_quantidade_itens_carrinho(self):
        quantidade = self.itemcarrinho1.quantidade + self.itemcarrinho2.quantidade
        self.assertEquals(self.carrinho.num_itens_carrinho, quantidade)

    def test_add_item_carrinho_not_authenticated(self):
        url = reverse('add')
        response = self.client.post(url, data=self.payload, content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_add_item_carrinho_is_authenticated(self):
        login_successful = self.client.login(username='testuser', password='testpassword')
        if not login_successful:
            self.fail("Login failed. Check username and password.")
        quantidade_inicial = self.carrinho.num_itens_carrinho

        url = reverse('add')
        response = self.client.post(url, data=self.payload, content_type='application/json')

        quantidade_final = self.carrinho.num_itens_carrinho

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Item added to cart successfully."})
        self.assertEquals(quantidade_inicial + 1, quantidade_final)

    def test_remove_item_carrinho_not_authenticated(self):
        url = reverse('remove')
        response = self.client.post(url, data=self.payload, content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_not_remove_to_zero_item_carrinho_is_authenticated(self):
        login_successful = self.client.login(username='testuser', password='testpassword')
        if not login_successful:
            self.fail("Login failed. Check username and password.")

        url = reverse('remove')
        response = self.client.post(url, data=self.payload, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Can´t remove, just one unit in the cart."})

    def test_remove_one_item_carrinho_is_authenticated(self):
        login_successful = self.client.login(username='testuser', password='testpassword')
        if not login_successful:
            self.fail("Login failed. Check username and password.")
        quantidade_inicial = self.carrinho.num_itens_carrinho

        url = reverse('remove')
        response = self.client.post(url, data=self.payload2, content_type='application/json')

        quantidade_final = self.carrinho.num_itens_carrinho
        self.assertEquals(quantidade_inicial - 1, quantidade_final)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Item removed to cart successfully."})

    def test_delete_item_carrinho_not_authenticated(self):
        url = reverse('delete')
        response = self.client.post(url, data=self.payload, content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_delete__item_carrinho_is_authenticated(self):
        login_successful = self.client.login(username='testuser', password='testpassword')
        if not login_successful:
            self.fail("Login failed. Check username and password.")

        quantidade_esperada = self.carrinho.num_itens_carrinho - self.itemcarrinho2.quantidade

        url = reverse('delete')
        response = self.client.post(url, data=self.payload2, content_type='application/json')

        quantidade_final = self.carrinho.num_itens_carrinho

        self.assertEquals(quantidade_esperada, quantidade_final)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Item deleted to cart successfully."})


class PagamentoTestView(TestCase):

    def setUp(self):
        self.usuario = Usuario.objects.create_user(username='testuser', password='testpassword', cpf='12404949985')

        self.produto = Produto.objects.create(
            nome='produto',
            preco=1500.00,
            id=1,
        )
        self.carrinho = Carrinho.objects.create(user=self.usuario)

        self.itemcarrinho = ItemCarrinho.objects.create(
            produto=self.produto,
            carrinho=self.carrinho,
            quantidade=1
        )

        self.client = Client()

        self.factory = RequestFactory()

    def test_pagamento_not_authenticated_user(self):
        response = self.client.get('/pagamento')
        self.assertEqual(response.status_code, 401)

    def test_pagamento_authenticated_user(self):
        login_successful = self.client.login(username='testuser', password='testpassword')
        if not login_successful:
            self.fail("Login failed. Check username and password.")

        response = self.client.get('/pagamento')
        self.assertEqual(response.status_code, 200)

    @mock.patch('venda.views.EfiPay')
    def test_charges_generation(self, mock_efi_pay):
        mock_efi_instance = mock_efi_pay.return_value

        mock_efi_instance.pix_list_evp.return_value = {'chaves': ['example_key']}
        mock_efi_instance.pix_create_immediate_charge.return_value = {'loc': {'id': 'example_loc_id'}}
        mock_efi_instance.pix_generate_qrcode.return_value = {'qrcode': 'example_qrcode',
                                                              'imagemQrcode': 'example_image'}

        request = self.factory.get('/pagamento')  # Replace '/your-url/' with the actual URL of your view
        request.user = self.usuario
        request.user.cpf = self.usuario.cpf

        response = pagamento(request)

        mock_efi_instance.pix_create_immediate_charge.assert_called_once_with(body={
            'calendario': {'expiracao': 3600},
            'devedor': {'cpf': f'{self.usuario.cpf}', 'nome': f'{self.usuario.username}'},
            'valor': {'original': f'{self.carrinho.subtotal_carrinho}'},
            'chave': 'example_key',
            'solicitacaoPagador': 'Cobrança dos serviços prestados.'
        })

        self.assertEqual(response.status_code, 200)