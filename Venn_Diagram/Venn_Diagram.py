# Created by: Jesus Gomez

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Función para graficar el diagrama de Venn
def graficador(*datos):
    # Desempaquetar los datos
    a = datos[1]
    b = datos[2]
    c = datos[3]
    ab = datos[4]
    bc = datos[5]
    ac = datos[6]
    abc = datos[7]
    universal = datos[0]

    # Graficar el diagrama de Venn
    venn3((a, b, ab, c, ac, bc, abc), set_labels=("A", "B", "C"), normalize_to=1.0)
    plt.text(0.8, 0.1, f"Universal: {universal}", fontsize=10, transform=plt.gca().transAxes)  # Agrega el texto "Universal" en la posición deseada
    plt.show()
    

# Función para calcular los valores de los conjuntos
def conjuntos(*valores: int):
    # Desempaquetar los valores
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

    # Verificar si los cálculos son correctos
    if (A+B+C+AB+BC+AC+ABC)+universal != total:
        print("Algo salió mal!")
    else:
        print("Todo bien!")
        graficador(total, A, B, C, AB, BC, AC, ABC)

# Función para solicitar información al usuario
def entrada():
    print("-"*50)
    print("Bienvenido a nuestro creador de conjuntos")
    print("""
    Los conjuntos se nombran desde (A, B y C)
    te pediremos unos datos, agradecemos que los coloques correctamente.
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
#Empieza el juego
#entrada()

# Llamar a la función conjuntos con valores específicos
conjuntos(80, 10, 20, 50, 4, 10, 7, 4)
