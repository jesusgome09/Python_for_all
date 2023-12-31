# Generated by Django 4.2.2 on 2023-07-01 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directores_cine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del autor', max_length=64)),
                ('apellido', models.CharField(help_text='Apellido del autor', max_length=64)),
                ('Peliculas_dirigidas', models.CharField(help_text='Peliculas dirigidas', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la pelicula', max_length=64)),
                ('descripcion', models.TextField(help_text='De que se trata la pelicula', max_length=100)),
                ('lanzamiento', models.DateField(blank=True, null=True)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='miapp.directores_cine')),
            ],
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
