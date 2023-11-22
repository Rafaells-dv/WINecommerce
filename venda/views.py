from django.views.generic import  DetailView, CreateView
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
import json


# Create your views here.
def carrinho(request):
    carrinho = None
    itenscarrinho = []

    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(user=request.user, completed=False)
        itenscarrinho = carrinho.itenscarrinho.all()

    context = {"carrinho":carrinho, "itens":itenscarrinho}
    return render(request, "venda/carrinho.html", context)

def index(request):
    produtos = Produto.objects.filter(categoria__icontains="c")
    context = {"produtos": produtos}
    return render(request, "index.html", context)


def add_to_carrinho(request):
    data = json.loads(request.body)
    id_produto = data["id"]
    produto = Produto.objects.get(id=id_produto)

    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(user=request.user, completed=False)
        itemcarrinho, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
        itemcarrinho.quantidade += 1
        itemcarrinho.save()
        print(itemcarrinho)

    return JsonResponse("Funcionando", safe=False)


def remove_from_carrinho(request):
    data = json.loads(request.body)
    id_produto = data["id"]
    produto = Produto.objects.get(id=id_produto)

    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(user=request.user, completed=False)
        itemcarrinho, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
        if itemcarrinho.quantidade > 1:
            itemcarrinho.quantidade -= 1
            itemcarrinho.save()
        print(itemcarrinho)

    return JsonResponse("Funcionando", safe=False)


def delete_item_carrinho(request):
    data = json.loads(request.body)
    id_produto = data["id"]
    produto = Produto.objects.get(id=id_produto)

    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(user=request.user, completed=False)
        itemcarrinho, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)

        itemcarrinho.delete()
        carrinho.save()

        print(itemcarrinho)

    return JsonResponse("Funcionando", safe=False)


class ProductDetailView(DetailView):
    model = Produto


class CadastroView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/cadastro.html"