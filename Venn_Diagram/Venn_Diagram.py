# Created by: Jesus Gomez

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# graficador(total, A, B, C, AB, BC, AC, ABC)


def graficador(*datos):
    a = datos[1]
    b = datos[2]
    c = datos[3]
    ab = datos[4]
    bc = datos[5]
    ac = datos[6]
    abc = datos[7]

    venn3((a, b, ab, c, ac, bc, abc), set_labels=("A", "B", "C"))
    plt.show()


def conjuntos(*valores: int):

    ABC = valores[7]
    if valores[4] > ABC:
        AB = valores[4] - ABC
    else:
        AB = valores[4]
    if valores[5] > ABC:
        BC = valores[5] - ABC
    else:
        BC = valores[5]
    if valores[6] > ABC:
        AC = valores[6] - ABC
    else:
        AC = valores[6]
    if valores[1] > (AB+ABC+AC):
        A = valores[1] - (AB+ABC+AC)
    else:
        A = valores[1]
    if valores[2] > (AB+ABC+BC):
        B = valores[2] - (AB+ABC+BC)
    else:
        B = valores[2]
    if valores[3] > (AB+ABC+BC):
        C = valores[3] - (AB+ABC+BC)
    else:
        C = valores[3]
    total = valores[0]
    universal = total - (A+B+C+AB+BC+AC+ABC)

    if (A+B+C+AB+BC+AC+ABC)+universal != total:
        print("Algo salio mal!")
    else:
        print("Todo bien!")

    graficador(total, A, B, C, AB, BC, AC, ABC)


def entrada():  # Aqui pedimos la informacion necesaria para empezar y llamar a la otra funcion
    print("-"*50)
    print("Bienvenido a nuestro creador de conjuntos")
    print("""
    Los conjuntos se nombran desde (A, B y C)
    te pediremos unos datos, agradesemos que los coloques bien.
    """)
    print("-"*50)

    total = int(input("Total: "))
    A = int(input("A: "))
    B = int(input("B: "))
    C = int(input("C: "))
    print("-"*50)
    AB = int(input("A y B: "))
    BC = int(input("B y C: "))
    AC = int(input("A y C: "))
    print("-"*50)
    ABC = int(input("ABC: "))
    print("-"*50)

    conjuntos(total, A, B, C, AB, BC, AC, ABC)


# entrada()
conjuntos(80, 10, 20, 50, 4, 10, 7, 4)
