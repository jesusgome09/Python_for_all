#Crea una única función (importante que sólo sea una) que sea capaz
#de calcular y retornar el área de un polígono.
#La función recibirá por parámetro sólo UN polígono a la vez.
#Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#Imprime el cálculo del área de un polígono de cada tipo.
import math


def calcularArea(base, altura):
    base = int(base)
    altura = int(altura)
    area = 0
    print("""
    Estamos hablando de:
    1) Triangulo
    2) Cuadrado
    3) Rectangulo
    """)
    respuesta = input("Digite aqui: ")
    respuesta = int(respuesta)
    if respuesta == 2:
        area = math.pow(base, 2) #saca area de un cuadrado
    elif respuesta == 1:
        area = base * altura / 2 #saca area de un triangulo
    else:
        area = base * altura #saca area de un rectangulo

    return(f"El Area es: {area}")

print("-"*50)
print("Vamos a sacar el area de un poligono!")
x = input("Digite la base: ")
y = input("Diguite la altura: ")
print(calcularArea(x,y))
print("-"*50)

#superado