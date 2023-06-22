"""
invirtiendo cadenas
"""



def inversor(texto):
    textoAlRevz = ""
    for i in texto:
        textoAlRevz = i + textoAlRevz 
    print(textoAlRevz)

inversor("el rato es mas peresozo")