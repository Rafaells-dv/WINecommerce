from .models import Carrinho

def carrinho(request):
    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(user=request.user, completed=False)
        return {'carrinho': carrinho}
    else:
        return {'carrinho':0}