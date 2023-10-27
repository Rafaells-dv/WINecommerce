from django.views.generic import ListView, DetailView
from .models import PC, Produto


# Create your views here.
class HomePageView(ListView):
    model = Produto
    paginate_by = 10

    def get_queryset(self):
        return Produto.objects.filter(categoria__exact='c').order_by('preco')


class ProductDetailView(DetailView):
    model = Produto

