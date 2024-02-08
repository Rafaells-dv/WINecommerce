import json

from django.test import TestCase, Client
from venda.models import Carrinho, Usuario, Produto, ItemCarrinho
from venda.views import add_to_carrinho
from django.urls import reverse, resolve
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

    def test_valor_do_carrinho(self):
        valor_carrinho = (self.itemcarrinho1.quantidade * self.itemcarrinho1.produto.preco + self.itemcarrinho2.quantidade * self.itemcarrinho2.produto.preco)
        self.assertEquals(self.carrinho.subtotal_carrinho, f"{valor_carrinho:.2f}")

    def test_quantidade_itens_carrinho(self):
        quantidade = self.itemcarrinho1.quantidade + self.itemcarrinho2.quantidade
        self.assertEquals(self.carrinho.num_itens_carrinho, quantidade)

    def test_add_item_carrinho_not_authenticated(self):
        url = reverse('add')
        data = {'id':self.produto1.id}
        payload = json.dumps(data)
        response = self.client.post(url, data=payload, content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_add_item_carrinho_is_authenticated(self):
        login_successful = self.client.login(username='testuser', password='testpassword')
        if not login_successful:
            self.fail("Login failed. Check username and password.")
        quantidade_inicial = self.carrinho.num_itens_carrinho

        url = reverse('add')
        data = {'id':self.produto1.id}
        payload = json.dumps(data)
        response = self.client.post(url, data=payload, content_type='application/json')

        quantidade_final = self.carrinho.num_itens_carrinho

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Item added to cart successfully."})
        self.assertEquals(quantidade_inicial+1, quantidade_final)
