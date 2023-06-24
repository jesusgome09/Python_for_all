
def escribir(texto):
    with open("My_School/Clases_de_youtube_intermedio/My_file.txt", "a") as file:
        file.write("\n"+texto)

def leer():
    with open("My_School/Clases_de_youtube_intermedio/My_file.txt", "r") as file:
        print(file.read())


def ingreso_datos(nombre, edad:int):
    escribir(f"Nombre: {nombre}; Edad: {edad}")

#ingreso_datos("pedro", 43)
#leer()

def buscar(nombre):
    with open("My_School/Clases_de_youtube_intermedio/My_file.txt", "r") as file:
        i = 0
        e = 0
        for line in file:
            if nombre in line:
                print(f"Linea: {i}; {line}")
                 

buscar("juan")