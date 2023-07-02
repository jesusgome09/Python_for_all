#graphical user interface
import tkinter as tki

#creamos comopente o controles en un contenedor
window = tki.Tk() #creamos una ventana

label_saludo = tki.Label(window, text="Hola", bg="yellow", fg="blue") #sirve para crear una etiqueta
label_saludo.pack(ipadx=30, ipady=30 ) #Mostramos la etiqueta label_saludo y agregamos padding

label_adios = tki.Label(window, text="Adios", bg="red", fg="white") #sirve para crear una etiqueta
label_adios.pack(ipadx=30,ipady=30)
#side sirve para colocarle un lugar, derecha izquierda
#expand sirve para que se expanda
#fill sirve para que siga el tamaño de la ventana
#fill= both sirve para quetome el tamaño de la letra y y siga el ancho de la ventana
label3 = tki.Label(window, text="label3", bg="purple", fg="green")
label3.pack(ipadx=30,ipady=30)

label4 = tki.Label(window, text="label4", bg="black", fg="white")
label4.pack(ipadx=15,ipady=30, side="left")

label5 = tki.Label(window, text="label5", bg="green", fg="black")
label5.pack(ipadx=15,ipady=30, side="right")

label5 = tki.Label(window, text="label5", bg="red", fg="black")
label5.pack(ipadx=15,ipady=30, side="right")

window.mainloop()
