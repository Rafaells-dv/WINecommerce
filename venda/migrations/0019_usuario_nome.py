# Generated by Django 4.2.6 on 2023-11-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0018_remove_usuario_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
