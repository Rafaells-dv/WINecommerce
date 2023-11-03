from django.views.generic import ListView, DetailView, CreateView
from .models import Produto
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(ListView):
    model = Produto
    paginate_by = 3

    def get_queryset(self):
        return Produto.objects.filter(categoria__exact='c').order_by('preco')


class ProductDetailView(DetailView):
    model = Produto

class CadastroView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/cadastro.html"