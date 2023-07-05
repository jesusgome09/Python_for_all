# Gestor Administrativo
## Version 2.0
### Created by: Jesus Gomez
Para empezar a usar el programa ejecuta la el archivo ```Main.py```
### Archivo para ejecutar en windows
dentro de la carpeta dist podras encontrar un ejecutable, procura descargar todas las dependencias pára que funcione
### Para crear un instalador 
Para incluir todos los archivos en tu programa y excluir únicamente el archivo `Readme.md`, puedes seguir estos pasos:

1. Crea un archivo `setup.py` en el mismo directorio que tus archivos Python.
2. Abre el archivo `setup.py` y agrega el siguiente código:

```python
from cx_Freeze import setup, Executable

# Configuración de la aplicación
app = 'Main.py'  # Nombre del archivo principal de tu aplicación

# Configuración de los ejecutables
executables = [Executable(app)]

# Opciones de configuración
options = {
    'build_exe': {
        'include_files': ['sqlite_conect.db'],
        'excludes': ['Readme.md'],
    }
}

# Configuración final del setup
setup(
    name='NombreDeTuPrograma',
    version='1.0',
    description='Descripción de tu programa',
    executables=executables,
    options=options
)
```

3. Guarda el archivo `setup.py`.

4. Abre una ventana de comandos (Command Prompt) y navega hasta el directorio donde se encuentra tu archivo `setup.py` (por ejemplo, `C:\Users\Jesus\python_developer\Gestor-Administrativo`).

5. Ejecuta el siguiente comando en la ventana de comandos para generar el ejecutable:

```bash
python setup.py build
```

Esto generará una carpeta `build` en tu directorio actual que contiene el ejecutable de tu programa, junto con las dependencias necesarias.

Ahora podrás ejecutar el programa en otro computador sin necesidad de un editor de código instalado. Simplemente copia la carpeta `build` en el otro computador y podrás ejecutar el programa desde allí.

Recuerda que debes tener `cx_Freeze` instalado en tu entorno Python para poder usarlo. Si aún no lo has instalado, puedes instalarlo usando el comando `pip install cx-Freeze`.

Espero que esto te ayude a generar el ejecutable de tu programa con `cx_Freeze`. Si tienes más preguntas, no dudes en hacerlas. ¡Buena suerte con tu proyecto!


### Codigo usado en setup.py
```python
from cx_Freeze import setup, Executable

# Archivo principal de tu programa
main_script = 'Main.py'

# Opciones de configuración
options = {
    'build_exe': {
        'packages': ['tkinter'],
        'excludes': ['Readme.md'],
        'include_files': ['sqlite_conect.db', 'icono.ico'],
    }
}

# Configuración de la aplicación
setup(
    name='Gestor-Administrativo',
    version='1.0',
    description='Gestión de usuarios',
    options=options,
    executables=[Executable(main_script, base='Win32GUI')]  # Ocultar la ventana de la terminal
)

```
