from django.shortcuts import render
from .models import Directores_cine, Peliculas

# Create your views here.

def index(request):
    num_pelis = Peliculas.objects.all().count()
    num_autores = Directores_cine.objects.all().count()

    return render(request,
    'index.html',
    context={
        'num_pelis':num_pelis,
        'num_autores':num_autores,
    }
    )
