# Generated by Django 4.2.6 on 2024-02-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0006_remove_carrinho_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]