def calculadora(año):
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        return True
    else:
        return False
if calculadora(2000):
    print("El año 2000 es bisiesto")
else:
    print("El año 2000 no es bisiesto")