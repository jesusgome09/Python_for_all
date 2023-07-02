from django.contrib import admin
from .models import Autor, Genre, Book, BookInstance


# Register your models here.

admin.site.register(Autor)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)
