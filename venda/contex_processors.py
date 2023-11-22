from .models import Carrinho

def carrinho(request):
    return{'carrinho':Carrinho}