import tkinter as tk
from tkinter import PhotoImage, TclError, messagebox

import customtkinter as ct
import Inicio
import sqlite_conect


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

    colorPrimario, colorSegundario, colorT = "#2271b3", "#B37A22", "#663E00"

    window = ct.CTk()
    window.config(background=colorPrimario)
    window.title("Gestor Administrativo")
    window.geometry("300x240+500+220")
    # window.iconbitmap('icono.ico')
    try:
        icon = PhotoImage(file="icono.png")
        window.iconphoto(True, icon)
    except TclError:
        print("No se encuentra el icono")
        print("Dirigete a la ubicacion del codigo fuente")
        print("Intentare corregirlo...")
        try:
            icon = PhotoImage(file="Gestor-AdministrativoV2/icono.png")
            window.iconphoto(True, icon)
        except TclError:
            print("No pude, intentalo tu")

    titulo = ct.CTkLabel(
        window,
        text="Registro de Usuarios",
        bg_color=colorPrimario,
        font=("Inter", 20, "normal"),
        text_color="white",
    )
    titulo.pack(pady=13)

    frame_nombre = tk.Frame(window)
    frame_nombre.pack(pady=8)
    frame_nombre.config(bg=colorPrimario)
    label_nombre = ct.CTkLabel(
        frame_nombre,
        text="Nombre:",
        bg_color=colorPrimario,
        font=("Inter", 20),
        text_color='white',
    )
    label_nombre.pack(side="left")
    caja_nombre = ct.CTkEntry(
        frame_nombre, placeholder_text="Juan", bg_color=colorPrimario
    )
    caja_nombre.pack(side="left", padx=8)
    caja_nombre.bind("<Return>", mover_a_apellido)

    frame_apellido = tk.Frame(window)
    frame_apellido.config(background=colorPrimario)
    frame_apellido.pack(pady=8)
    label_apellido = ct.CTkLabel(
        frame_apellido,
        text="Apellido:",
        font=("Inter", 20),
        text_color='white',
    )
    label_apellido.pack(side="left")
    caja_apellido = ct.CTkEntry(
        frame_apellido, placeholder_text="Perez", bg_color=colorPrimario
    )
    caja_apellido.pack(side="left", padx=8)
    caja_apellido.bind("<Return>", mover_a_email)

    frame_email = tk.Frame(window, background=colorPrimario)
    frame_email.pack(pady=8)
    label_email = ct.CTkLabel(
        frame_email,
        text="Email:",
        font=("Inter", 20),
        text_color='white',
    )
    label_email.pack(side="left")
    caja_email = ct.CTkEntry(
        frame_email, placeholder_text="juanperez@gmail.com", bg_color=colorPrimario
    )
    caja_email.pack(side="left", padx=8)
    caja_email.bind("<Return>", finalizar)

    frame_botones = tk.Frame(window, background=colorPrimario)
    frame_botones.pack(pady=8)
    boton_cancelar = ct.CTkButton(
        frame_botones,
        text="Cancelar",
        command=cancelar,
        fg_color=colorSegundario,
        hover_color=colorT,
    )
    boton_cancelar.pack(side="left", padx=8)
    boton_registrar = ct.CTkButton(
        frame_botones,
        text="Registrar",
        command=registrar,
        fg_color=colorSegundario,
        hover_color=colorT,
    )
    boton_registrar.pack(side="left", padx=8)

    window.mainloop()
