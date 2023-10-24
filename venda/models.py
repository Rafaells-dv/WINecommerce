from django.db import models
import uuid


# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome')
    descricao = models.CharField(max_length=100, help_text='Descrição')
    preco = models.FloatField(max_length=100, help_text='Preço')
    imagem = models.ImageField(upload_to='product_images_PC', default='Sem imagem')

    CATEGORIAS = (
        ('c', 'Computador'),
        ('p', 'Periférico'),
        ('a', 'Acessório')
    )
    categoria = models.CharField(max_length=1,
                                 choices=CATEGORIAS,
                                 default='c',
                                 blank=True,
                                 help_text='Categoria do produto')

    def __str__(self):
        return self.nome


class PC(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID')
    produto = models.ForeignKey('Produto', on_delete=models.SET_NULL, null=True)
    cpu = models.CharField(max_length=100, help_text='CPU')
    gpu = models.CharField(max_length=100, help_text='GPU')
    memoria_ram = models.CharField(max_length=100, help_text='Memória Ram')
    motherboard = models.CharField(max_length=100, help_text='Placa mãe')
    armazenamento = models.CharField(max_length=100, help_text='Armazenamento')
    cooler = models.CharField(max_length=100, help_text='Sistema de resfriamento')
    fonte = models.CharField(max_length=100, help_text='Fonte')
    gabinete = models.CharField(max_length=100, help_text='Gabinete')

    def __str__(self):
        return self.produto.nome


class InstanciaProduto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID do produto')
    produto = models.ForeignKey('Produto', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.produto.nome