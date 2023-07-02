from conect import csv_conect
from time import sleep
from colorama import Fore

def sacar(ids):
    informacion = csv_conect.pedir_Datos("PyPage.py/BaseDatosInformacion.csv", ids)
    print(f"Tu informacion es: {informacion}")
    print("-"*50)
intentos = 0
def sing_in():
    global intentos
    print("-"*50)
    print(Fore.BLUE, "sing_in")
    User = input(Fore.WHITE + "User: ")
    Password = input("Password: ")
    if csv_conect.verificar_Datos("PyPage.py/BaseDatos.csv",User, Password):
        ids = csv_conect.pedir_ids("PyPage.py/BaseDatos.csv", User, Password)
        print("-"*30)
        sacar(ids)
    else:
        intentos += 1
        if intentos < 3:
            print("Usuario o contraseña incorrecta")
            print("Por favor intente nuevamente")
            sleep(1)
            sing_in()
        else:
            print("Intentos acabados")
            intentos = 0
            sleep(1)
            opcional_in()

def sing_up():
    print("-"*50)
    print(Fore.BLUE, "sing_up")
    User = input(Fore.WHITE + "User: ")
    Password = input("Password: ")
    if csv_conect.verificador_user("PyPage.py/BaseDatos.csv",User):
        print("El usuario ya existe\n Por favor intente recuperar su contraseña")
        sleep(3)
        opcional_in()
    ids = csv_conect.Crear_e_ingresar_Datos("PyPage.py/BaseDatos.csv",User, Password)
    csv_conect.agregar_ids_a_BDI("PyPage.py/BaseDatosInformacion.csv",ids)
    print("Usuario y contraseña registrados exitosamente")

    sing_in()

def opcional_in():
    print("-"*50)
    print("Bienvenido a WebApp punto py")
    print("")
    print("""Por favor seleciona una opción:
    1 - Iniciar sesión
    2 - Registrarse
    3 - Salir""")
    opcion = int(input("Ingrese un digito: "))
    if opcion == 1:
            sing_in()
    elif opcion == 2:
            sing_up()
    elif opcion == 3:
            exit()

opcional_in()
