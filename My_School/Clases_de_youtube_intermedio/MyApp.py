"""
nose ni que hacer
"""


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
    if valores[1] > AB+ABC+AC:
        A = valores[1] - (AB+ABC+AC)
    else:
        A = valores[1]

    print(valores)

    for i in valores:
        print(i)


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


entrada()
