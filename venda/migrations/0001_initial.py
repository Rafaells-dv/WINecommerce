# Generated by Django 4.2.6 on 2023-10-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome', max_length=100)),
                ('cpu', models.CharField(help_text='CPU', max_length=100)),
                ('gpu', models.CharField(help_text='GPU', max_length=100)),
                ('memoria_ram', models.CharField(help_text='Memória Ram', max_length=100)),
                ('motherboard', models.CharField(help_text='Placa mãe', max_length=100)),
                ('armazenamento', models.CharField(help_text='Armazenamento', max_length=100)),
                ('cooler', models.CharField(help_text='Sistema de resfriamento', max_length=100)),
                ('fonte', models.CharField(help_text='Fonte', max_length=100)),
                ('gabinete', models.CharField(help_text='Gabinete', max_length=100)),
                ('preco', models.IntegerField()),
                ('imagem', models.ImageField(upload_to='product_images_PC')),
            ],
        ),
    ]
