import tkinter as tk
import sqlite_conect
import Inicio
from tkinter import messagebox
from tkinter import PhotoImage


def abrir(nombre, apellido):

    def volver_a_buscar():
        window.destroy()
        Inicio.abrir()

    datos = sqlite_conect.devuelve_datos(nombre, apellido)

    def eliminar():
        if sqlite_conect.eliminar(datos[0]):
            messagebox.showinfo("Mensaje", "Se ha eliminado con éxito!")
            window.destroy()
            Inicio.abrir()
        else:
            messagebox.showerror("Error", "Ha ocurrido un error")

    window = tk.Tk()
    window.title("Gestor Administrativo")
    window.configure(bg='#2271b3')
    window.geometry("300x240+500+220")
    # window.iconbitmap('icono.ico')
    icon = PhotoImage(file="icono.png")
    window.iconphoto(True, icon)

    titulo = tk.Label(window, text="Gestor de Usuarios", background='#2271b3', font=('Inter', 16, 'normal'), fg='white')
    titulo.pack(pady=13)

    label_nombre = tk.Label(window, text=f"Nombre: {datos[1]}", background='#2271b3', font=('Inter', 16), fg='white')
    label_nombre.pack()

    label_apellido = tk.Label(window, text=f"Apellido: {datos[2]}", background='#2271b3', font=('Inter', 16), fg='white')
    label_apellido.pack()

    label_email = tk.Label(window, text=f"Email: {datos[3]}", background='#2271b3', font=('Inter', 12), fg='white')
    label_email.pack()

    label_id = tk.Label(window, text=f"Id: {datos[0]}", background='#2271b3', font=('Inter', 16), fg='white')
    label_id.pack()

    frame_botones = tk.Frame(window, background='#2271b3')
    frame_botones.pack(pady=8)
    boton_eliminar = tk.Button(frame_botones, text="Eliminar", width=10, height=2, command=eliminar)
    boton_eliminar.pack(side='left', padx=8)
    boton_volver_a_buscar = tk.Button(frame_botones, text="Volver a buscar", width=15, height=2, command=volver_a_buscar)
    boton_volver_a_buscar.pack(side='left', padx=8)

    window.mainloop()
