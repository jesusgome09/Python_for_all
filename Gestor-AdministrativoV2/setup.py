from cx_Freeze import setup, Executable

# Archivo principal de tu programa
main_script = 'Main.py'

# Opciones de configuración
options = {
    'build_exe': {
        'packages': ['tkinter','customtkinter'],
        'excludes': ['Readme.md'],
        'include_files': ['sqlite_conect.db', 'icono.png'],
    }
}

# Configuración de la aplicación
setup(
    name='Gestor-Administrativo',
    version='2.0',
    description='Gestión de usuarios',
    options=options,
    executables=[Executable(main_script, base='Win32GUI')]  # Ocultar la ventana de la terminal
)
