import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Imagen en Tk")
root.geometry("400x300")
# root.attributes('-transparentcolor', 'grey') #con esto se pone trasparente del todo

# Cargar imagen del disco.
image = tk.PhotoImage(file="titulo.png")
# Insertarla en una etiqueta.
label = ttk.Label(root, image=image)
label.pack()

root.mainloop()
