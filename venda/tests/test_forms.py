from django.test import TestCase
from venda.forms import CriarContaForm
from venda.models import Usuario


class TestFormCadastro(TestCase):

    def test_cadastro_form_valid_data(self):
        form = CriarContaForm(data={
            'username': 'testuser',
            'email': 'usertestemail@gmail.com',
            'cpf':'12345678910',
            'cep':'9260521',
            'password1':'testpassword',
            'password2':'testpassword'
        })

        self.assertTrue(form.is_valid())

    def test_cadastro_form_no_data(self):
        form = CriarContaForm(data={})

        self.assertFalse(form.is_valid())

    def test_cadastro_form_email_invalido(self):
        form = CriarContaForm(data={
            'username': 'testuser',
            'email': 'usertestemailgmail.com',
            'cpf':'12345678910',
            'cep':'9260521',
            'password1':'testpassword',
            'password2':'testpassword'
        })

        self.assertFormError(form, 'email', 'Informe um endereço de email válido.')
        
    def test_cadastro_form_email_ja_utilizado(self):
        self.user = Usuario.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpassword'
        )

        form = CriarContaForm(data={
            'username': 'testuser',
            'email': 'test@gmail.com',
            'cpf':'12345678910',
            'cep':'9260521',
            'password1':'testpassword',
            'password2':'testpassword'
        })

        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], [
            "Este e-mail já está cadastrado em outra conta! Por favor, utilize outro endereço de e-mail."])