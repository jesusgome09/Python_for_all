"""
invirtiendo cadenas
"""



def inversor(texto):
    textoAlRevz = ""
    for i in texto:
        textoAlRevz = i + textoAlRevz 
    print(textoAlRevz.lower())

inversor("oveuh noc zorra")