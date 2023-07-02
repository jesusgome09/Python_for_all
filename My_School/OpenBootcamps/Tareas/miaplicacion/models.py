from django.db import models
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="pon el nombre del genero")

    def __str__(self):
        return self.name

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
        
class Book(models.Model):
    title = models.CharField(max_length=32)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True) #un campo de esta tabla estara en otra tabla
    sumary = models.TextField(max_length=100, help_text="Pon de que va el libro")
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=220)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Avaliable'),
        ('r','Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')


    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)
