# coincide con ?

patrones = [
    'coco','coca','seco','piso'
    'gato','gata','gecko','palo',
    'perro',
    'jirafa',
]

palabra = input("Introduce una palabra: ")


for opcion in patrones:
    if opcion[0] == palabra[0]:
        if opcion[1] == palabra[1]:
            if opcion[2] == palabra[2]:
                if opcion[3] == palabra[3]:
                    print(f"{palabra} coincide con {opcion}")
                else:
                    print(f"{palabra} coincide con {opcion} por las tres primeras letra")
            else:
                print(f"{palabra} coincide con {opcion} por las dos primeras letra")
        else:
            print(f"{palabra} coincide con {opcion} por la primera letra")


