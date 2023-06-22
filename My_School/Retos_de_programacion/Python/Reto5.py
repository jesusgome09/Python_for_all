 #Crea un programa que se encargue de calcular el aspect ratio de una
 #imagen a partir de una url.
 #Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 #mouredev/master/mouredev_github_profile.png
 #Por ratio hacemos referencia por ejemplo a los "16:9" de una
 #imagen de 1920*1080px.

import requests
from PIL import Image
from io import BytesIO

def calcular_aspect_ratio(url):
    # Descargar la imagen desde la URL
    response = requests.get(url)
    imagen = Image.open(BytesIO(response.content))

    # Obtener las dimensiones de la imagen
    ancho = imagen.width
    alto = imagen.height

    # Calcular el máximo común divisor (mcd) de las dimensiones
    def mcd(a, b):
        while b:
            a, b = b, a % b
        return a

    divisor_comun = mcd(ancho, alto)

    # Calcular el aspect ratio
    aspect_ratio = f"{ancho // divisor_comun}:{alto // divisor_comun}"

    return aspect_ratio

# URL de ejemplo
url_ejemplo = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

# Calcular el aspect ratio de la imagen
aspect_ratio = calcular_aspect_ratio(url_ejemplo)

print(f"El aspect ratio de la imagen es: {aspect_ratio}")


#esto no lo hice yo, lo hizo ChatGPT, cuando aprendo como, seguire