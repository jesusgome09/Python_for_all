from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

# como no se puede instanciar solo se puede usar para que otra clase la herede
# osea hay que derivarla


class Perro(Animal):
    def sonido(self):  # y otra cosa, son como la interfaces en java, solo son un molde, deber armar el resto
        print("Miau")


d = Perro()

d.sonido()
