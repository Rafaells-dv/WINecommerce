from .views import HomePageView, ProductDetailView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail')
]