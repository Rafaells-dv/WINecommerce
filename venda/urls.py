from venda import views
from django.urls import path, include

urlpatterns = [
    path('home/', views.HomePageView.as_view, name='home')
]