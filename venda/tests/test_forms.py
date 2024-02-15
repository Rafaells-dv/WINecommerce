from django.test import TestCase, Client
from venda.forms import CriarContaForm, EditarPerfilForm
from venda.models import Usuario
from django.urls import reverse
import os
from django.core.files.images import ImageFile


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


class TestEditarPerfilForm(TestCase):

    def setUp(self):

        self.user = Usuario.objects.create_user(
            username='test',
            password='test',
            email='test@gmail.com',
            cep='12345678910',
            foto='foto1.jpg',
            id=1
        )

        self.client = Client()

    def test_editar_perfil_valid_data(self):

        self.client.login(username='test', password='test')

        image_path = r'C:\Users\Rafael\OneDrive - ufpr.br\Área de Trabalho\foto.jpg'
        with open(image_path, 'rb') as f:
            photo_content = f.read()

        photo = ImageFile(open(image_path, 'rb'))

        form_data = {
            'username': 'test2',
            'email': 'test2@gmail.com',
            'cpf': 234253235,
            'cep': 10987654321,
            'foto': photo,
        }

        form = EditarPerfilForm(data=form_data)

        self.assertTrue(form.is_valid())

        url = reverse('editarperfil', kwargs={'pk': self.user.id})
        response = self.client.post(url, data=form_data, format='multipart')

        self.assertEqual(response.status_code, 302)

        redirect_url = response.url
        response = self.client.get(redirect_url)

        self.assertEqual(response.status_code, 200)
        updated_user = Usuario.objects.get(id=self.user.id)

        for chave, valor in form_data.items():
            if chave == 'foto':
                updated_foto_filename = os.path.basename(updated_user.foto.name)

                self.assertEquals(updated_foto_filename, 'foto.jpg')

                foto_teste = r'C:\Users\Rafael\PycharmProjects\WINecommerce\profiles_img\foto.jpg'
                if os.path.exists(foto_teste):
                    os.remove(foto_teste)
            else:
                self.assertEquals(getattr(updated_user, chave), valor)

