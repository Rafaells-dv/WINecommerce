from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CriarContaForm(UserCreationForm):

    email = forms.EmailField()
    cpf = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'email', 'cpf', 'password1', 'password2')


