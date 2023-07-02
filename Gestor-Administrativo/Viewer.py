import tkinter as tk
import sqlite_conect
import Inicio
from tkinter import messagebox



def abrir(nombre, apellido):

    def volver_a_buscar():
        window.destroy()
        Inicio.abrir()

    datos = sqlite_conect.devuelve_datos(nombre, apellido)

    def eliminar():
        if sqlite_conect.eliminar(datos[0]):
            messagebox.showinfo("Mensaje","Se a eliminado con exito!")
            window.destroy()
            Inicio.abrir()
        else:
            messagebox.showerror("Error","A ocurrido un error")

    window = tk.Tk()
    window.title("Gestor Administrativo")
    window.configure(bg='#2271b3', width=300, height=240)
    window.geometry("300x240+500+220")
    window.iconbitmap('icono.ico')

    titulo = tk.Label(window, text="Gestor de Usuarios",background='#2271b3', font=('Inter',16,'normal'), fg='white')
    titulo.place(x=56, y=13, width=183, height=16)

    label_nombre = tk.Label(window, text=f"Nombre: {datos[1]}", background='#2271b3', font=('Inter',16), fg='white')
    label_nombre.place(x=24, y=44)

    label_apellido = tk.Label(window, text=f"Apellido: {datos[2]}", background='#2271b3', font=('Inter',16), fg='white')
    label_apellido.place(x=24, y=71)

    label_email = tk.Label(window, text=f"Email: {datos[3]}", background='#2271b3', font=('Inter',12), fg='white')
    label_email.place(x=24, y=98)

    label_id = tk.Label(window, text=f"Id: {datos[0]}", background='#2271b3', font=('Inter',16), fg='white')
    label_id.place(x=24, y=125)

    boton_volver_a_buscar = tk.Button(window, text="Volver a buscar", width=15, height=2)
    boton_volver_a_buscar.place(x=171, y=185)
    boton_volver_a_buscar.config(command=volver_a_buscar)

    boton_eliminar = tk.Button(window, text="Eliminar", width=10, height=2)
    boton_eliminar.place(x=32, y=185)
    boton_eliminar.config(command=eliminar)



    window.mainloop()
