import tkinter as tki
import random
from tkinter import ttk  # sirve para que los componentes tengan mas estilo
# practicamente el del sistema operativo

window = tki.Tk()

colors = ['blue', 'red', 'yellow', 'green', 'orange']

for c in range(0, 100):
    color = random.randint(0, len(colors))
    color2 = random.randint(0, len(colors))
    labelLoco = tki.Label(window, text="x")
    labelLoco.place(x=random.randint(0, 100), y=random.randint(0, 100))

label1 = tki.Label(window, text="Posicionamiento absoluto",
                   background="blue", foreground="white")
label1.place(x=10, y=50)

label2 = tki.Label(window, text="Otro mas",
                   background="blue", foreground="white")
label2.place(relx=0.10, rely=0.15)


window.mainloop()
