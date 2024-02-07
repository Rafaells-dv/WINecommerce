from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from venda.views import *
from venda.models import Produto, Usuario


class TestUrls(TestCase):

    def test_home_url_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

    def test_product_detail_view_resolved(self):
        ids = Produto.objects.values_list('pk', flat=True)
        for id in ids:
            url = reverse('product-detail', args=[id])
            self.assertEquals(resolve(url).func.view_class, ProductDetailView)

    def test_cadastro_resolved(self):
        url = reverse('cadastro')
        self.assertEquals(resolve(url).func.view_class, CadastroView)

    def test_edit_profile_resolved(self):
        users = Usuario.objects.values_list('pk', flat=True)
        for user in users:
            url = reverse('editarperfil', args=[user])
            self.assertEquals(resolve(url).func.view_class, EditarPerfilView)

    def test_gear_list_resolved(self):
        url = reverse('gears')
        self.assertEquals(resolve(url).func.view_class, GearListView)

    def test_add_to_carrinho_resolved(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func, add_to_carrinho)

    def test_remove_from_carrinho_resolved(self):
        url = reverse('remove')
        self.assertEquals(resolve(url).func, remove_from_carrinho)

    def test_delete_item_carrinho_resolved(self):
        url = reverse('delete')
        self.assertEquals(resolve(url).func, delete_item_carrinho)

    def test_perfil_resolved(self):
        url = reverse('perfil')
        self.assertEquals(resolve(url).func, perfil)

    def test_carrinho_resolved(self):
        url = reverse('carrinho')
        self.assertEquals(resolve(url).func, carrinho)

    def test_pagamento_resolved(self):
        url = reverse('pagamento')
        self.assertEquals(resolve(url).func, pagamento)