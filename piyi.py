import os
import random
import sqlite3 as sq
import time

from progress.bar import Bar, ChargingBar


def crear_perfume():
    print("-" * 50)
    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    marca = input("Marca: ")
    valor = int(input("Valor: "))
    cantidad = input("Cantidad disponible: ")

    marca = marca.upper()

    with sq.connect("sqlite_conect.db") as f:
        cursor = f.cursor()
        cursor.execute(f"insert into perfumes(codigo, nombre, marca, cantidad, valor) values({codigo}, '{nombre}', '{marca}', {cantidad}, {valor})")

    print("")
    print("Se a agregado correctamente")
    print("")
    time.sleep(1)
    incio()

def crear_cupon():
    print("-" * 50)
    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    descuento = input("Descuento: ")

    with sq.connect("sqlite_conect.db") as f:
        cursor = f.cursor()
        cursor.execute(f"insert into cupones(codigo, nombre, descuento) values({codigo}, '{nombre}', {descuento})")

    print("")
    print("Se a agregado correctamente")
    print("")
    time.sleep(1)
    incio()

def crear():
    print("-" * 50)
    print("¿Que desear crear?")
    print("")
    print("1) Nuevo Perfume")
    print("1) Nuevo Cupon de descuento")
    print("-" * 50)
    opcion = input("Digita un numero: ")

    if int(opcion) == 1:
        crear_perfume()
    elif int(opcion) == 2:
        crear_cupon()
    else:
        print("Error: Numero equivocado")

def modificar(item):
    if item == "perfume":
        print("-" * 50)
        print("Modificar perfume")
        codigo = input("Codigo: ")
        print("-" * 50)
        print("¿Que desear modificar?")
        print("")
        print("1) Nombre")
        print("2) Marca")
        print("3) Valor")
        print("4) Cantidad")
        print("-" * 50)
        opcion = input("Digita un numero: ")
        print("-" * 50)

        if int(opcion) == 1:
            nuevo_dato = input("Digite el nuevo valor: ")
            with sq.connect("sqlite_conect.db") as f:
                cursor = f.cursor()
                cursor.execute(f"update perfumes set nombre = {nuevo_dato} where codigo = {codigo}")
        elif int(opcion) == 2:
            nuevo_dato = input("Digite el nuevo valor: ")
            with sq.connect("sqlite_conect.db") as f:
                cursor = f.cursor()
                cursor.execute(f"update perfumes set marca = '{nuevo_dato}' where codigo = {codigo}")

        elif int(opcion) == 3:
            nuevo_dato = input("Digite el nuevo valor: ")
            with sq.connect("sqlite_conect.db") as f:
                cursor = f.cursor()
                cursor.execute(f"update perfumes set valor = {nuevo_dato} where codigo = {codigo}")

        elif int(opcion) == 4:
            nuevo_dato = input("Digite el nuevo valor: ")
            with sq.connect("sqlite_conect.db") as f:
                cursor = f.cursor()
                cursor.execute(f"update perfumes set cantidad = {nuevo_dato} where codigo = {codigo}")

        else:
            print("Error: Numero equivocado")

        print("Se a modificado correctamente")
        time.sleep(1)
        incio()


    elif item == "cupon":

        print("-" * 50)
        print("Modificar cupon")
        codigo = input("Codigo: ")
        print("-" * 50)
        print("¿Que desear modificar?")
        print("")
        print("1) Nombre")
        print("2) Descuento")
        print("-" * 50)
        opcion = input("Digita un numero: ")
        print("-" * 50)

        if int(opcion) == 1:
            nuevo_dato = input("Digite el nuevo valor: ")
            with sq.connect("sqlite_conect.db") as f:
                cursor = f.cursor()
                cursor.execute(f"update cupones set nombre = '{nuevo_dato}' where codigo = {codigo}")
        elif int(opcion) == 2:
            nuevo_dato = input("Digite el nuevo valor: ")
            with sq.connect("sqlite_conect.db") as f:
                cursor = f.cursor()
                cursor.execute(f"update cupones set descuento = {nuevo_dato} where codigo = {codigo}")
        else:
            print("Error: Numero equivocado")
        print("Se a modificado correctamente")
        time.sleep(1)
        incio()
    else:
        print("Error: Item no encontrado")


def eliminar(item):
    if item == "perfume":
        print("-" * 50)
        print("Eliminar perfume")
        codigo = input("Codigo: ")
        print("-" * 50)
        print("¿Estas seguro? (s/n)")
        seguro = input("Digita aqui: ")
        if seguro == "s":
            with sq.connect("sqlite_conect.db") as f:
                cursor = f.cursor()
                cursor.execute(f"delete from perfumes where codigo = {codigo}")
                print("Se a eliminado correctamente")
                time.sleep(1)
                incio()
        elif seguro == "n":
            print("")
            eliminar("perfume")
        else:
            print("Error: Opcion no valida")


    elif item == "cupon":
        print("-" * 50)
        print("Eliminar cupon")
        codigo = input("Codigo: ")
        print("-" * 50)
        print("¿Estas seguro? (s/n)")
        seguro = input("Digita aqui: ")
        if seguro == "s":
            with sq.connect("sqlite_conect.db") as f:
                cursor = f.cursor()
                cursor.execute(f"delete from cupones where codigo = {codigo}")
                print("Se a eliminado correctamente")
                time.sleep(1)
                incio()
        elif seguro == "n":
            print("")
            eliminar("cupon")
        else:
            print("Error: Opcion no valida")
    else:
        print("Error: Item no encontrado")

def leer_perfume():

    with sq.connect("sqlite_conect.db") as f:
        cursor = f.cursor()
        valor = cursor.execute(f"select * from perfumes")
        resultado = valor.fetchall()

    print("")
    print("-"* 50)
    print("CODIGO   MARCA  NOMBRE  CANTIDAD  VALOR ")
    print("-"* 50)

    for i in resultado:
        codigo, marca, nombre, cantidad, valor = i
        print(f"{codigo}  {marca}   {nombre}     {cantidad}      ${valor}")

    print("")
    print("Se a cargado correctamente")
    print("")

    print("-"* 50)
    print("¿Quiere Hacer algo mas?")
    print("1) Modificar")
    print("2) Eliminar")
    print("3) volver al incio")
    print("-"* 50)
    opcion = input("Digita un numero: ")

    if int(opcion) == 1:
        modificar("perfume")
    elif int(opcion) == 2:
        eliminar("perfume")
    elif int(opcion) == 3:
        incio()
    else:
        print("Error: Numero equivocado")

def leer_cupon():

    with sq.connect("sqlite_conect.db") as f:
        cursor = f.cursor()
        valor = cursor.execute(f"select * from cupones")
        resultado = valor.fetchall()

    print("")
    print("-"* 50)
    print("CODIGO           NOMBRE           DESCUENTO  ")
    print("-"* 50)

    for i in resultado:
        codigo, nombre, descuento = i
        espacio1 = " " * (10 - len(str(codigo)))
        espacio2 = " " * 10
        print(f" {codigo}{espacio1}{nombre}{espacio2}{descuento}")

    print("")
    print("Se a cargado correctamente")
    print("")

    print("-"* 50)
    print("¿Quiere Hacer algo mas?")
    print("1) Modificar")
    print("2) Eliminar")
    print("3) volver al incio")
    print("-"* 50)
    opcion = input("Digita un numero: ")

    if int(opcion) == 1:
        modificar("cupon")
    elif int(opcion) == 2:
        eliminar("cupon")
    elif int(opcion) == 3:
        incio()
    else:
        print("Error: Numero equivocado")

def leer():
    print("-" * 50)
    print("¿Que desear leer?")
    print("")
    print("1) Perfumes")
    print("2) cupones de descuento")
    print("-" * 50)
    opcion = input("Digita un numero: ")

    if int(opcion) == 1:
        leer_perfume()
    elif int(opcion) == 2:
        leer_cupon()
    else:
        print("Error: Numero equivocado")

def generar_factura(codigo_p, cantidad_p, codigo_c=0):
    # codigo_p = codigo del perfume
    # cantidad = cantidad de perfumes
    # codigo_c = codigo del cupon

    with sq.connect("sqlite_conect.db") as f:
        cursor = f.cursor()
        valor = cursor.execute(f"select * from perfumes where codigo = {codigo_p}")
        resultado = valor.fetchall()

    with sq.connect("sqlite_conect.db") as f:
        cursor = f.cursor()
        valor = cursor.execute(f"select * from cupones where codigo = {codigo_c}")
        resultado2 = valor.fetchall()

    for i in resultado:
        codigo, marca, nombre, cantidad, valor = i

    for i in resultado2:
        codigo2, nombre2, descuento = i

    print("-" * 50)
    print("Factura")
    print("-" * 50)
    print(f"Producto: {nombre}")
    print(f"Cantidad: {cantidad_p}")
    print(f"Valor total: ${int(valor) * int(cantidad_p)}")
    if codigo_c != 0:
        print(f"Descuento: {descuento}%")
        print(f"Valor final: ${int(valor) * int(cantidad_p) - (int(descuento) / 100 * int(valor) * int(cantidad_p))}")
    print("-" * 50)

def recolectar_datos():
    print("-" * 50)
    perfume = input("Codigo del perfume: ")
    cantidad = input("Cantidad: ")
    cupon = input("Codigo del cupon: ")

    bar2 = ChargingBar('Creando:', max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.05))
        bar2.next()
    bar2.finish()

    print("")
    print("")
    print("-" * 50)
    if cupon == "":
        generar_factura(perfume, cantidad)
    else:
        generar_factura(perfume, cantidad, cupon)



def incio():
    print("-" * 50)
    print("Bienvenido a mi CRUD de consola")
    print("-" * 50)
    print("1) Crear")
    print("2) Leer")
    print("3) Actualizar")
    print("4) Eliminar")
    print("")
    print("5) Generar factura")

    print("-" * 50)
    opcion = input("Digita un numero: ")
    print("-" * 50)

    if int(opcion) == 1:
        crear()
    elif int(opcion) == 2:
        leer()
    elif int(opcion) == 3:
        print("¿Que desear actualizar?")
        print("")
        print("1) Perfumes")
        print("2) cupones de descuento")
        print("-" * 50)
        opcion = input("Digita un numero: ")
        print("-" * 50)
        if int(opcion) == 1:
            modificar("perfume")
        elif int(opcion) == 2:
            modificar("cupon")
        else:
            print("Error: Numero equivocado")
    elif int(opcion) == 4:
        print("¿Que desear eliminar?")
        print("")
        print("1) Perfumes")
        print("2) cupones de descuento")
        print("-" * 50)
        opcion = input("Digita un numero: ")
        print("-" * 50)
        if int(opcion) == 1:
            eliminar("perfume")
        elif int(opcion) == 2:
            eliminar("cupon")
        else:
            print("Error: Numero equivocado")
    elif int(opcion) == 5:
        recolectar_datos()
    else:
        print("Error: Numero equivocado")

if __name__ == '__main__':
    incio()
