"""
from matplotlib import pyplot as plt
from matplotlib_venn import venn3

venn3((1, 2, 3, 4, 5, 6, 7))

print("Listo")
"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3
from PIL import Image

A = [1, 2, ]
B = [4, 5, ]
C = [7, 8, ]

# Crear el diagrama de tres círculos
venn3(A, B, C)

# Guardar el gráfico en un archivo
plt.savefig("venn_diagram.png")

# Abrir y mostrar la imagen utilizando PIL
image = Image.open("venn_diagram.png")
image.show()
