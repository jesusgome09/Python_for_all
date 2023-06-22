# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS
# las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

def funcion(texto1: str, texto2: str):
    texto1 = texto1.lower()
    texto2 = texto2.lower()
#este modelo no funciona con espacios
    tam1 = 0
    tam2 = 0
    pase = 0
    for i in texto1:
        tam1 += 1
        if i in texto2:
            pase += 1
    for e in texto2:
        tam2 += 1
        if e in texto1:
            pase += 1
    suma = tam1 + tam2
    if pase == suma:
        return True
    else:
        return False

texto1 = input("Escribe el texto1: ")
texto2 = input("Escribe el texto2: ")

resultado = funcion(texto1, texto2)
print(resultado)

# probado con: caso, caso = True
# probado con: perro, orrep = True
# probado con: poole, picos = False
# probado con: Panzon, zonaPN = True
# probado con: chapon, perrito = False
# Status: Superado


#el profe lo soluciono y fue mucho mas corto en (7 lineas)
#return sorted(texto1.lower()) == sorted(texto2.lower())
#en este caso ordenamos las letras se ordenan y revisan si es igual a la otra