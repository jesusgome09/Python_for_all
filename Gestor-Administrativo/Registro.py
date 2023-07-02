import tkinter as tk
import sqlite_conect
import Inicio
from tkinter import messagebox



def abrir():

    def registrar():
        name = caja_nombre.get()
        surname = caja_apellido.get()
        correo = caja_email.get()

        if sqlite_conect.agregar(name, surname, correo):
            messagebox.showinfo("Mensaje","Se a registrado con exito!")
            window.destroy()
            Inicio.abrir()
        else:
            messagebox.showerror("Error","A ocurrido un error")
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
    window.configure(bg='#2271b3', width=300, height=240)
    window.geometry("300x240+500+220")
    window.iconbitmap('icono.ico')

    titulo = tk.Label(window, text="Registro de Usuarios",background='#2271b3', font=('Inter',16,'normal'), fg='white')
    titulo.place(x=56, y=13, width=200, height=16)

    label_nombre = tk.Label(window, text="Nombre:", background='#2271b3', font=('Inter',16), fg='white')
    label_nombre.place(x=24, y=59)

    caja_nombre = tk.Entry(window)
    caja_nombre.place(x=115, y=65, width=157, height=19)
    caja_nombre.bind('<Return>', mover_a_apellido)

    label_apellido = tk.Label(window, text="Apellido:", background='#2271b3', font=('Inter',16), fg='white')
    label_apellido.place(x=24, y=96)

    caja_apellido = tk.Entry(window)
    caja_apellido.place(x=115, y=102, width=157, height=19)
    caja_apellido.bind('<Return>', mover_a_email)

    label_email = tk.Label(window, text="Email:", background='#2271b3', font=('Inter',16), fg='white')
    label_email.place(x=24, y=133)

    caja_email = tk.Entry(window)
    caja_email.place(x=90, y=139, width=182, height=19)
    caja_email.bind('<Return>', finalizar)

    boton_registrar = tk.Button(window, text="Registrar", width=12, height=2)
    boton_registrar.place(x=171, y=185)
    boton_registrar.config(command=registrar)

    boton_cancelar = tk.Button(window, text="Cancelar", width=10, height=2)
    boton_cancelar.place(x=32, y=185)
    boton_cancelar.config(command=cancelar)



    window.mainloop()
