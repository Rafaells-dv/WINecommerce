from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario


class CriarContaForm(UserCreationForm):

    email = forms.EmailField()
    celular = forms.IntegerField()
    cpf = forms.IntegerField()
    cep = forms.IntegerField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'celular', 'cep', 'password1', 'password2')


