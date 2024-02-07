from django.test import TestCase
from venda.models import Carrinho, Usuario, Produto, ItemCarrinho


class CarrinhoTestView(TestCase):

    def setUp(self):
        self.usuario = Usuario.objects.create(username='testuser')
        self.produto1 = Produto.objects.create(
            nome='produto1',
            preco=1000.00,
        )
        self.produto2 = Produto.objects.create(
            nome='produto2',
            preco=1000.00,
        )
        self.carrinho = Carrinho.objects.create(user=self.usuario)

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

    def test_valor_do_carrinho_correto(self):
        valor_carrinho = (self.itemcarrinho1.quantidade * self.itemcarrinho1.produto.preco + self.itemcarrinho2.quantidade * self.itemcarrinho2.produto.preco)
        self.assertEquals(self.carrinho.subtotal_carrinho, f"{valor_carrinho:.2f}")