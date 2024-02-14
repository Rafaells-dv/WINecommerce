from django.test import TestCase
from venda.models import *


class TestCarrinhoModels(TestCase):

    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')

        self.produto = Produto.objects.create(
            nome='produto1',
            preco=1000.00,
            id=1,
        )

        self.carrinho = Carrinho.objects.create(user=self.user)

        self.itemcarrinho = ItemCarrinho.objects.create(
            produto=self.produto,
            carrinho=self.carrinho,
            quantidade=2
        )

    def test_total_preco_cada_item_no_carrinho(self):
        self.assertEquals(self.itemcarrinho.total, 2000.00)

    def test_num_itens_no_carrinho(self):
        self.itemcarrinho2 = ItemCarrinho.objects.create(
            produto=self.produto,
            carrinho=self.carrinho,
            quantidade=4
        )

        self.assertEquals(self.carrinho.num_itens_carrinho, 6)

    def test_preco_total_do_carrinho(self):
        self.produto2 = Produto.objects.create(
            nome='produto2',
            preco=500.00,
            id=2,
        )

        self.itemcarrinho2 = ItemCarrinho.objects.create(
            produto=self.produto2,
            carrinho=self.carrinho,
            quantidade=3
        )

        self.assertEquals(self.carrinho.subtotal_carrinho, f'{3500.00:.2f}')


class TestProduct(TestCase):

    def setUp(self):
        self.produto = Produto.objects.create(
            nome="pc",
            preco=1000.00,
            categoria='c',
            id=1,
        )

        self.pc = PC.objects.create(
            id=1,
            produto=self.produto,
            cpu = 'processador',
            gpu = 'placa de video',
            memoria_ram = '16gb',
            motherboard = 'placa mãe',
            armazenamento = '1tb',
            cooler = 'cooler',
            fonte = '600w',
            gabinete = 'gamer',
        )

    def test_funcao_pecas(self):
        pecas_teste = {
            'gpu': 'placa de video',
            'cpu': 'processador',
            'fonte': '600w',
            'cooler': 'cooler',
            'armazenamento': '1tb',
            'gabinete': 'gamer',
            'ram': '16gb',
            'motherboard': 'placa mãe',
        }

        self.assertEquals(self.produto.pecas_pc(), pecas_teste)


