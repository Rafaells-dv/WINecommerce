from django.shortcuts import render
from django.views import generic
from .models import PC


# Create your views here.
class HomePageView(generic.ListView):
    model = PC
    paginate_by = 10