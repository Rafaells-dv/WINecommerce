from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario
from django.forms import ModelForm


class CriarContaForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'celular', 'cep', 'password1', 'password2')

        def clean_email(self):
            email = self.cleaned_data['email']
            if Usuario.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "Este e-mail já está cadastrado em outra conta! Por favor, utilize outro endereço de e-mail.")
            return email


class EditarPerfilForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ('username','email','cep','foto')

        def clean_email(self):
            email = self.cleaned_data['email']
            if Usuario.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "Este e-mail já está cadastrado em outra conta! Por favor, utilize outro endereço de e-mail.")
            return email


