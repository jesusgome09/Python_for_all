import tkinter as tk
from tkinter import PhotoImage
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
            messagebox.showerror("Error", "Usuario no encontrado")

    def on_enter(event):
        buscar()

    def mover(event):
        caja_apellido.focus_set()

    def registrar():
        window.destroy()
        Registro.abrir()

    window = tk.Tk()
    window.title("Gestor Administrativo")
    window.configure(bg='#2271b3')
    window.geometry("300x240+500+220")
    #window.iconbitmap('icono.ico')
    icon = PhotoImage(file="icono.png")
    window.iconphoto(True, icon)

    titulo = tk.Label(window, text="Gestor de Usuarios", background='#2271b3', font=('Inter', 16, 'normal'), fg='white')
    titulo.pack(pady=13)

    frame_nombre = tk.Frame(window, background='#2271b3')
    frame_nombre.pack(pady=8)
    label_nombre = tk.Label(frame_nombre, text="Nombre:", background='#2271b3', font=('Inter', 16), fg='white')
    label_nombre.pack(side='left')
    caja_nombre = tk.Entry(frame_nombre)
    caja_nombre.pack(side='left', padx=8)
    caja_nombre.bind('<Return>', mover)

    frame_apellido = tk.Frame(window, background='#2271b3')
    frame_apellido.pack(pady=8)
    label_apellido = tk.Label(frame_apellido, text="Apellido:", background='#2271b3', font=('Inter', 16), fg='white')
    label_apellido.pack(side='left')
    caja_apellido = tk.Entry(frame_apellido)
    caja_apellido.pack(side='left', padx=8)
    caja_apellido.bind('<Return>', on_enter)

    frame_botones = tk.Frame(window, background='#2271b3')
    frame_botones.pack(pady=8)
    boton_registrar = tk.Button(frame_botones, text="Registrar", width=10, height=2, command=registrar)
    boton_registrar.pack(side='left', padx=8)
    boton_buscar = tk.Button(frame_botones, text="Buscar", width=10, height=2, command=buscar)
    boton_buscar.pack(side='left', padx=8)

    window.mainloop()
