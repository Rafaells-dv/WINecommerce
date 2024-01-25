from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    path('editarperfil/<int:pk>', views.EditarPerfilView.as_view(), name='editarperfil'),
    path('gear', views.GearListView.as_view(), name="gear"),
    path('add_to_carrinho', views.add_to_carrinho, name="add"),
    path('remove_from_carrinho', views.remove_from_carrinho, name="remove"),
    path('delete_item_carrinho', views.delete_item_carrinho, name="delete"),
    path('perfil', views.perfil, name="perfil"),
    path('carrinho', views.carrinho, name="carrinho"),
    path('pagamento', views.pagamento, name="pagamento"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
