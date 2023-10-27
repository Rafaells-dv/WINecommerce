# Generated by Django 4.2.6 on 2023-10-24 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0007_produto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pc',
            name='imagem',
        ),
        migrations.RemoveField(
            model_name='pc',
            name='preco',
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default='Sem imagem', upload_to='static'),
        ),
    ]
