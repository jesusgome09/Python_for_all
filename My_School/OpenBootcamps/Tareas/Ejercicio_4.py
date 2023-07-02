from colorama import Fore
def mostrar_numeros_en_orden_inverso_v1():
    for i in range(1,101):
        numero = 101
        print(Fore.BLUE, numero - i)
        numero -= i

def mostrar_numeros_en_orden_inverso_v2():
    for i in reversed(range(1,101)):
        print(Fore.GREEN, i)
mostrar_numeros_en_orden_inverso_v1()
mostrar_numeros_en_orden_inverso_v2()

