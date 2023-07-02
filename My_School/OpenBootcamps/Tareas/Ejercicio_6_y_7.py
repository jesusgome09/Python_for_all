"""
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
"""
# inicializamos la clase
class Alumno:
    # inicializamos los atributos
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
 
 
    # función para imprimir los datos
    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
 
 
    # función para obtener el resultado
    def resultado(self):
            if self.nota < 5:
                print("El alumno ha suspendido")
            else:
                print("El alumno ha aprobado")
 
 
 
# bloque principal
# creamos los nuevos objetos
alumno1=Alumno()
alumno2=Alumno()
 
# inicializamos los atributos
alumno1.inicializar("Pipe",10)
alumno2.inicializar("Mafe",2)
 

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
