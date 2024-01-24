from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario
from django.forms import ModelForm


class CriarContaForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CriarContaForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'cpf', 'cep', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'cpf', 'cep', 'password1', 'password2')

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


