#Crear una función para calcular el IMC
def masa_corporal():
    #Obtener datos
    peso = input("Peso(Kg): ")
    altura = input("Altura(m): ")
    #Calcular los datos
    imc = float(peso) / float(altura) ** 2
    # redondear ims a dos decimales
    imc = round(imc, 2)
    #imprimir imc
    print(f"Tu indice de masa corporal es: {imc}")

#Llamar funcion 
masa_corporal()
