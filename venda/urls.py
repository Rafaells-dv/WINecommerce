from .views import HomePageView, ProductDetailView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
