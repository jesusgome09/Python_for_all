import tkinter as tk
from tkinter import ttk

window = tk.Tk()
def saludar(event):
    print("Hola")
def saludarr(event):
    print("pepe")
def salir(event):
    window.quit()

boton = tk.Button(window, text="haz click")
boton.pack()
botons = tk.Button(window, text="salir")
botons.pack()
boton.bind('<Button-1>', saludar) #click
boton.bind('<Double-1>', saludarr) #doble-clik
botons.bind('<Button-1>', salir) #click

window.mainloop()

"""
from tkinder import filedialog
filename = filedialog.askopenfilename()
"""
