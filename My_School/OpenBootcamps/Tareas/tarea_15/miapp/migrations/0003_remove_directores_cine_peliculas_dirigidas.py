# Generated by Django 4.2.2 on 2023-07-01 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_directores_cine_peliculas_delete_usuarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directores_cine',
            name='Peliculas_dirigidas',
        ),
    ]