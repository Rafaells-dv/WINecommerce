import requests
from django.views.generic import DetailView, FormView, UpdateView
from .models import *
from django.shortcuts import render
from .forms import CriarContaForm, EditarPerfilForm
from django.http import JsonResponse
from efipay import EfiPay
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

def perfil(request):
    return render(request, "venda/perfil.html")

def pagamento(request):

    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(user=request.user, completed=False)


        credentials = {
            'client_id': 'Client_Id_3e8b0d2b528839d31913ae02f3982980e3fd1d74',
            'client_secret': 'Client_Secret_304d68cc3dea0e1c2347c5594e0382e359e486fc',
            'sandbox': True,
            'certificate': 'D:\Efi\certificados\homologacao-539200-win - homo_cert.pem'
        }

        efi = EfiPay(credentials)

        print(request.user.cpf)
        print(request.user.username)
        print(carrinho.subtotal_carrinho)

        body = {
            'calendario': {
                'expiracao': 3600
            },
            'devedor': {
                'cpf': f'{str(request.user.cpf)}',
                'nome': f'{str(request.user.username)}'
            },
            'valor': {
                'original': f'{str(carrinho.subtotal_carrinho)}'
            },
            'chave': '71cdf9ba-c695-4e3c-b010-abb521a3f1be',
            'solicitacaoPagador': 'Cobrança dos serviços prestados.'
        }

        response = efi.pix_create_immediate_charge(body=body)
        print(response)

        id = response["loc"]["id"]

        params = {
            'id': id
        }

        resposta = efi.pix_generate_qrcode(params=params)
        print(resposta)



        qrcode = resposta["qrcode"]
        img_qrcode = resposta["imagemQrcode"]

        context={"qrcode":qrcode, "img_qrcode":img_qrcode}


    return render(request, "venda/pagamento.html",context)

def add_to_carrinho(request):
    data = json.loads(request.body)
    id_produto = data["id"]
    produto = Produto.objects.get(id=id_produto)

    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(user=request.user, completed=False)
        itemcarrinho, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
        itemcarrinho.quantidade += 1
        itemcarrinho.save()

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


class CadastroView(FormView):
    form_class = CriarContaForm
    template_name = "registration/cadastro.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class EditarPerfilView(UpdateView):
    model = Usuario
    template_name = "registration/editarperfil.html"
    fields = ['username', 'email', 'cpf', 'cep', 'foto']

    def get_success_url(self):
        return reverse('perfil')
