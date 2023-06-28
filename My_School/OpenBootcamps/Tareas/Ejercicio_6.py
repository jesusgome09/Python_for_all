from os import system as clear
clear("cls")

class Vehiculo:
    color = "negro"
    ruedas = 4
    puertas = 2

class Coche(Vehiculo):
    velocidad = 60
    cilindrada = 42

coche = Coche()

print("Color:",coche.color)
print("Cantidad de ruedas:",coche.ruedas)
print("Cantidad de puertas:",coche.puertas)
print("Maxima velocidad:",coche.velocidad)
print("Cilindrada:",coche.cilindrada)