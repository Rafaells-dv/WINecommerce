from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    cpf = models.IntegerField(default=0)
    celular = models.IntegerField(default=0)
    cep = models.IntegerField(default=0)
    foto = models.ImageField(default='media/perfil.png', upload_to="media/")

    def get_absolute_url(self):
        return reverse('editarperfil', args=[str(self.id)])


class Produto(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome')
    descricao = models.TextField(max_length=500, help_text='Descrição')
    preco = models.FloatField(help_text='Preço')
    imagem = models.ImageField(upload_to='images', default='Sem imagem')
    estoque = models.IntegerField(default=0)
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

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

    def pecas_pc(self):
        valores = PC.objects.filter(produto__nome__icontains=self.nome).values()
        valores = valores[0]

        gpu = valores['gpu']
        cpu = valores['cpu']
        fonte = valores['fonte']
        cooler = valores['cooler']
        armazenamento = valores['armazenamento']
        gabinete = valores['gabinete']
        ram = valores['memoria_ram']
        motherboard = valores['motherboard']

        pecas = {
            'gpu': gpu,
            'cpu': cpu,
            'fonte': fonte,
            'cooler': cooler,
            'armazenamento': armazenamento,
            'gabinete': gabinete,
            'ram': ram,
            'motherboard': motherboard,
        }
        return pecas


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


class Carrinho(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def num_itens_carrinho(self):
        itens = self.itenscarrinho.all()
        quantidade = sum([item.quantidade for item in itens])
        return quantidade

    @property
    def subtotal_carrinho(self):
        produtos = self.itenscarrinho.all()
        total = sum([produto.total for produto in produtos])
        preco_total = f"{total:.2f}"
        return preco_total


class ItemCarrinho(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE, related_name='itens')
    carrinho = models.ForeignKey('Carrinho', on_delete=models.CASCADE, related_name='itenscarrinho')
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.produto.nome

    @property
    def total(self):
        total = self.produto.preco * self.quantidade
        return total

