import tkinter as tk
import sqlite_conect
import Inicio
from tkinter import messagebox
from tkinter import PhotoImage

def abrir():
    def registrar():
        name = caja_nombre.get()
        surname = caja_apellido.get()
        correo = caja_email.get()

        if sqlite_conect.agregar(name, surname, correo):
            messagebox.showinfo("Mensaje", "Se ha registrado con éxito!")
            window.destroy()
            Inicio.abrir()
        else:
            messagebox.showerror("Error", "Ha ocurrido un error")

    def cancelar():
        window.destroy()
        Inicio.abrir()

    def mover_a_apellido(event):
        caja_apellido.focus_set()

    def mover_a_email(event):
        caja_email.focus_set()

    def finalizar(event):
        registrar()

    window = tk.Tk()
    window.title("Gestor Administrativo")
    window.configure(bg='#2271b3')
    window.geometry("300x240+500+220")
    # window.iconbitmap('icono.ico')
    icon = PhotoImage(file="icono.png")
    window.iconphoto(True, icon)

    titulo = tk.Label(window, text="Registro de Usuarios", background='#2271b3', font=('Inter', 16, 'normal'),
                      fg='white')
    titulo.pack(pady=13)

    frame_nombre = tk.Frame(window, background='#2271b3')
    frame_nombre.pack(pady=8)
    label_nombre = tk.Label(frame_nombre, text="Nombre:", background='#2271b3', font=('Inter', 16), fg='white')
    label_nombre.pack(side='left')
    caja_nombre = tk.Entry(frame_nombre)
    caja_nombre.pack(side='left', padx=8)
    caja_nombre.bind('<Return>', mover_a_apellido)

    frame_apellido = tk.Frame(window, background='#2271b3')
    frame_apellido.pack(pady=8)
    label_apellido = tk.Label(frame_apellido, text="Apellido:", background='#2271b3', font=('Inter', 16), fg='white')
    label_apellido.pack(side='left')
    caja_apellido = tk.Entry(frame_apellido)
    caja_apellido.pack(side='left', padx=8)
    caja_apellido.bind('<Return>', mover_a_email)

    frame_email = tk.Frame(window, background='#2271b3')
    frame_email.pack(pady=8)
    label_email = tk.Label(frame_email, text="Email:", background='#2271b3', font=('Inter', 16), fg='white')
    label_email.pack(side='left')
    caja_email = tk.Entry(frame_email)
    caja_email.pack(side='left', padx=8)
    caja_email.bind('<Return>', finalizar)

    frame_botones = tk.Frame(window, background='#2271b3')
    frame_botones.pack(pady=8)
    boton_cancelar = tk.Button(frame_botones, text="Cancelar", width=10, height=2, command=cancelar)
    boton_cancelar.pack(side='left', padx=8)
    boton_registrar = tk.Button(frame_botones, text="Registrar", width=12, height=2, command=registrar)
    boton_registrar.pack(side='left', padx=8)

    window.mainloop()
