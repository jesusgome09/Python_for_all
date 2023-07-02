import os
os.system("cls")

class Dino: # en python todo es publico
    encendido = False #una regla es que si una variable enpieza por "_" no debemops modificarla

    def encender(self):
        self.encendido = True #esto es como un "global" pero esto indica que es una variable de la clase
    def isEncendido(self):
        return self.encendido

d = Dino()
d.encender()
print(d.encendido)
print(d.isEncendido())

class Estatica: #esta es una clase estatica, ella comparten un mismo espacio de memoria
    numero = 1

    def incrementa(): #da error pero funciona
        Estatica.numero += 1

Estatica.incrementa()
print(Estatica.numero)
Estatica.incrementa()
print(Estatica.numero)
Estatica.incrementa()
print(Estatica.numero)

#estas clases no son muy usadas

## Herencia ##

class Jugete(Dino):
    def pola(self):
        return "pola"

j = Jugete()
print(j.pola())

class incial:
    def __init__(self, nombre): # esto es un constructor, lo que inicializa una clase
        print(f"Estoy jugando con {nombre}")
    # se puede crear un destructor que de inicializa cual el programa finaliza, se llama __del__
    #amenos que la llamen antes con del("class"), ten en cuenta que al llamarlo no podras llamar mas esa clase hasta instanciarla de nuevo

i = incial("Jesus")
i

#las clases en python no existen, son un diccionario