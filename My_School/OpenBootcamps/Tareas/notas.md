# Crear un proyecto en django
django-admin startproject miproyecto .
### cuando no te sirva puedes usar
python -m django startproject myproject
# levantar un servidor web de django
```python3 manage.py runserver```
# crear aplicaciones
python3 manage.py startapp miaplicacion
### cuando no te sirva puedes usar
python -m django startapp miapp
## elazar con con el proyecto general
Me dirigo a [miproyecto] -> settings.py -> INSTALLED_APPS = [
    escribo algo como esto
    ```'miaplicacion.apps.MiaplicacionConfig',```
]
## agregar a patterns
Me dirijo a [miproyecto] -> urls.py -> urlpatterns = [
    escribo
    ```path('miaplicacion/', include('miaplicacion.urls'))```
    para que funcione debo importar include de la siguiente manera
    ```from django import include```
]
## seguir con patterns en miaplicacion
si no tienes urls.py tienes que crearlo de la siguiente manera:
Crear [urls.py] y escribir lo siguiente:
```python
from django.conf.urls import url
from . import views

urlpatterns = []
```
## ejecutar noseque cambios
python3 manage.py migrate

## crear superuser
python3 manage.py createsuperuser

## nose pero para algo sirve
python3 manage.py makemigrations
