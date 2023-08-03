grado = 2

match grado:
    case 1:
        print("Hola")
    case 2:
        print("Melo")

fonts = pyfliglet.FligletFont.getfonts()
slecio0nar = ramdon.choises(fonts)
acsii = pyfiglet.figlet_format(mensaje, font=slecio0nar)
