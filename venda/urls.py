from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    path('add_to_carrinho', views.add_to_carrinho, name="add"),
    path('carrinho', views.carrinho, name="carrinho"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
