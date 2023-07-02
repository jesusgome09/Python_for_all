import tkinter as tk
import sqlite_conect
import Registro
import Viewer
from tkinter import messagebox



def abrir():

    def buscar():
        nombres = caja_nombre.get()
        apellido = caja_apellido.get()
        if sqlite_conect.verificador(nombres, apellido):
            window.destroy()
            Viewer.abrir(nombres, apellido)
        else:
            messagebox.showerror("Error","Usuario no encontrado")

    def on_enter(event):
        buscar()

    def mover(event):
        caja_apellido.focus_set()

    def registrar():

        window.destroy()
        Registro.abrir()

    window = tk.Tk()
    window.title("Gestor Administrativo")
    window.configure(bg='#2271b3', width=300, height=240)
    window.geometry("300x240+500+220")
    window.iconbitmap('icono.ico')


    titulo = tk.Label(window, text="Gestor de Usuarios",background='#2271b3', font=('Inter',16,'normal'), fg='white')
    titulo.place(x=56, y=13, width=183, height=16)

    label_nombre = tk.Label(window, text="Nombre:", background='#2271b3', font=('Inter',16), fg='white')
    label_nombre.place(x=24, y=59)

    label_apellido = tk.Label(window, text="Apellido:", background='#2271b3', font=('Inter',16), fg='white')
    label_apellido.place(x=24, y=96)

    caja_nombre = tk.Entry(window)
    caja_nombre.place(x=112, y=65, width=157, height=19)
    caja_nombre.bind('<Return>', mover)

    caja_apellido = tk.Entry(window)
    caja_apellido.place(x=112, y=101, width=157, height=19)
    caja_apellido.bind('<Return>', on_enter)

    boton_buscar = tk.Button(window, text="Buscar", width=10, height=2)
    boton_buscar.place(x=171, y=154)
    boton_buscar.config(command=buscar)

    boton_registrar = tk.Button(window, text="Registrar", width=10, height=2)
    boton_registrar.place(x=32, y=154)
    boton_registrar.config(command=registrar)



    window.mainloop()
