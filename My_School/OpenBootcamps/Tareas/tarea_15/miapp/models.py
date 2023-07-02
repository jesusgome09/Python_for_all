from django.db import models

class Directores_cine(models.Model):
    nombre = models.CharField(max_length=64, help_text="Nombre del autor")
    apellido = models.CharField(max_length=64, help_text="Apellido del autor")
    peliculas_dirigidas = models.ManyToManyField('Peliculas')

    def __str__(self):
        return self.nombre

class Peliculas(models.Model):
    nombre = models.CharField(max_length=64, help_text="Nombre de la pelicula")
    autor = models.ForeignKey('Directores_cine', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(max_length=100, help_text="De que se trata la pelicula")
    lanzamiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre
