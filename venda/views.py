from django.views.generic import DetailView, FormView, UpdateView
from .models import *
from django.shortcuts import render
from .forms import CriarContaForm
from django.http import JsonResponse
from efipay import EfiPay
from venda.credentials.credentials import *
import json


# Create your views here.
def carrinho(request):
    carrinho = None
    itenscarrinho = []

    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(user=request.user, completed=False)
        itenscarrinho = carrinho.itenscarrinho.all()

    context = {"carrinho": carrinho, "itens": itenscarrinho}
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

        efi = EfiPay(credentials_h)

        lista_chaves = efi.pix_list_evp()
        n_chaves = len(lista_chaves['chaves'])

        if n_chaves < 1:
            chave_criada = efi.pix_create_evp()
            chave_pix = chave_criada['chave']
        else:
            chave_pix = lista_chaves['chaves'][0]

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
            'chave': chave_pix,
            'solicitacaoPagador': 'Cobrança dos serviços prestados.'
        }

        response = efi.pix_create_immediate_charge(body=body)

        loc_id = response["loc"]["id"]

        params = {
            'id': loc_id
        }

        resposta = efi.pix_generate_qrcode(params=params)

        qrcode = resposta["qrcode"]
        img_qrcode = resposta["imagemQrcode"]

        context = {"qrcode": qrcode, "img_qrcode": img_qrcode}

    return render(request, "venda/pagamento.html", context)


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
