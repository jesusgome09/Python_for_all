from django.shortcuts import render
from .models import Book, Autor, BookInstance, Genre
#lo de abajo lo agrego chatgpt
def index(request):
    #return render(request, 'miaplicacion/index.html')
    num_books = Book.objects.all().count()
    num_instanses = BookInstance.objects.all().count()

    dispponibles = BookInstance.objects.filter(status='a').count()
    num_autor = Autor.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_books':num_books,
            'num_autors':num_autor,
            'disponibles':dispponibles,
            "num_instances":num_instanses,
        }
    )
