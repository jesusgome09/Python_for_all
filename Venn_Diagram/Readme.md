# Venn Diagrams

_Creado por: Jesus Gomez_

Para este programa utilicé la biblioteca `matplotlib_venn` para graficar los resultados.

```python
from matplotlib import pyplot as plt
from matplotlib_venn import venn3
```

El orden con el que matplotlib trabaja es el siguiente: a, b, ab, c, ac, bc, abc.

## Uso del programa

Para utilizar el programa, sigue los siguientes pasos:

1. Importa las bibliotecas necesarias:

```python
from matplotlib import pyplot as plt
from matplotlib_venn import venn3
```

2. Define los conjuntos y los valores de intersección:

```python
total = 80
A = 10
B = 20
C = 50
AB = 4
BC = 10
AC = 7
ABC = 4
```

3. Llama a la función `conjuntos()` con los valores de los conjuntos:

```python
conjuntos(total, A, B, C, AB, BC, AC, ABC)
```

Pero ay que tener en cuenta algo, hay una funcion llamada ```entrada()``` cuya funcion pide dato por dato desde la consola, valga la redundancia. Esta funcion no fue tomada al momento de subir el archivo para una rapida ejecucion, pero si gusta puede eliminar el ```#```  de donde aparece esto:

```python
    conjuntos(total, A, B, C, AB, BC, AC, ABC)
#Empieza el juego
#entrada()

# Llamar a la función conjuntos con valores específicos
conjuntos(80, 10, 20, 50, 4, 10, 7, 4)
```

Al final del codigo, a continuacion __Ejemplo de uso__ desde el metodo rapido.

4. El programa generará el gráfico de diagrama de Venn basado en los valores proporcionados y lo mostrará.

## Ejemplo de uso

Aquí tienes un ejemplo de cómo utilizar el programa con valores específicos:

```python
conjuntos(80, 10, 20, 50, 4, 10, 7, 4)
```

## Notas adicionales

- Asegúrate de tener instaladas las bibliotecas `matplotlib` y `matplotlib_venn` para poder ejecutar el programa correctamente.
- Los valores de intersección (AB, BC, AC, ABC) deben ser menores o iguales a los valores de los conjuntos individuales (A, B, C).
- Si hay discrepancias en los valores proporcionados, se mostrará el mensaje "Algo salió mal!".
- Si los cálculos son exitosos y no hay discrepancias, se mostrará el mensaje "Todo bien!" y se generará el gráfico de Venn.
- El programa solo tinen un problema y es que el circulo "C" sale mas grande en algunos       casos, espero solucionarlo pronto

¡Disfruta usando el programa y creando diagramas de Venn interactivos!

### Pronto lo mejorare, espero sigamos aprendiendo juntos
