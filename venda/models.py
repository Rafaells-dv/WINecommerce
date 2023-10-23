from django.db import models


# Create your models here.

class PC(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome')
    cpu = models.CharField(max_length=100, help_text='CPU')
    gpu = models.CharField(max_length=100, help_text='GPU')
    memoria_ram = models.CharField(max_length=100, help_text='Memória Ram')
    motherboard = models.CharField(max_length=100, help_text='Placa mãe')
    armazenamento = models.CharField(max_length=100, help_text='Armazenamento')
    cooler = models.CharField(max_length=100, help_text='Sistema de resfriamento')
    fonte = models.CharField(max_length=100, help_text='Fonte')
    gabinete = models.CharField(max_length=100, help_text='Gabinete')
    preco = models.IntegerField()
