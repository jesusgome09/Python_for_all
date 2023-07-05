import tkinter as tk
from tkinter import PhotoImage, messagebox
import customtkinter as ct

import Inicio
import sqlite_conect


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

    colorPrimario, colorSegundario, colorT = "#2271b3", "#B37A22", "#663E00"

    window = tk.Tk()
    window.title("Gestor Administrativo")
    window.configure(bg=colorPrimario)
    window.geometry("300x240+500+220")
    # window.iconbitmap('icono.ico')
    try:
        icon = PhotoImage(file="icono.png")
        window.iconphoto(True, icon)
    except tk.TclError:
        print("No se encuentra el icono")
        print("Dirigete a la ubicacion del codigo fuente")
        print("Intentare corregirlo...")
        try:
            icon = PhotoImage(file="Gestor-AdministrativoV2/icono.png")
            window.iconphoto(True, icon)
        except tk.TclError:
            print("No pude, intentalo tu")

    titulo = ct.CTkLabel(
        window,
        text="Gestor de Usuarios",
        bg_color=colorPrimario,
        font=("Inter", 20),
        text_color="white",
    )
    titulo.pack(pady=13)

    label_nombre = ct.CTkLabel(
        window,
        text=f"Nombre: {datos[1]}",
        bg_color=colorPrimario,
        font=("Inter", 16),
        text_color="white",
    )
    label_nombre.pack()

    label_apellido = ct.CTkLabel(
        window,
        text=f"Apellido: {datos[2]}",
        bg_color=colorPrimario,
        font=("Inter", 16),
        text_color="white",
    )
    label_apellido.pack()

    label_email = ct.CTkLabel(
        window,
        text=f"Email: {datos[3]}",
        bg_color=colorPrimario,
        font=("Inter", 12),
        text_color="white",
    )
    label_email.pack()

    label_id = ct.CTkLabel(
        window,
        text=f"Id: {datos[0]}",
        bg_color=colorPrimario,
        font=("Inter", 16),
        text_color="white",
    )
    label_id.pack()

    frame_botones = tk.Frame(window, background=colorPrimario)
    frame_botones.pack(pady=8)
    boton_eliminar = ct.CTkButton(
        frame_botones,
        text="Eliminar",
        command=eliminar,
        fg_color=colorSegundario,
        hover_color=colorT,
    )
    boton_eliminar.pack(side="left", padx=8)
    boton_volver_a_buscar = ct.CTkButton(
        frame_botones,
        text="Volver a buscar",
        command=volver_a_buscar,
        fg_color=colorSegundario,
        hover_color=colorT,
    )
    boton_volver_a_buscar.pack(side="left", padx=8)

    window.mainloop()
