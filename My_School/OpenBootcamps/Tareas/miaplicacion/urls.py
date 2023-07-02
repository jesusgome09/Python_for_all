from django.urls import path
from miaplicacion import views
#from django.conf.urls import url

urlpatterns = [
    #lo de abajo lo agrego chatgpt
    #url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    # otras rutas de tu aplicación
]
