import tkinter as tk
from tkinter import PhotoImage, TclError, messagebox

import customtkinter as ct
import Registro
import sqlite_conect
import Viewer


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

    colorPrimario, colorSegundario, colorT = "#2271b3", "#B37A22", "#663E00"

    window = ct.CTk()
    window.title("Gestor Administrativo")
    window.config(background=colorPrimario)
    window.geometry("300x240+500+220")

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
        text="Gestor de Usuarios",
        font=("Inter", 20, "normal"),
        text_color="white",
        bg_color=colorPrimario,
    )
    titulo.pack(pady=13)

    frame_nombre = tk.Frame(window, background=colorPrimario)
    frame_nombre.pack(pady=8)
    label_nombre = ct.CTkLabel(
        frame_nombre,
        text="Nombre:",
        font=("Inter", 20, "normal"),
        text_color="white",
        bg_color=colorPrimario,
    )
    label_nombre.pack(side="left")
    caja_nombre = ct.CTkEntry(
        frame_nombre, placeholder_text="nombre", bg_color=colorPrimario
    )
    caja_nombre.pack(side="left", padx=8)
    caja_nombre.bind("<Return>", mover)

    frame_apellido = tk.Frame(window, background=colorPrimario)
    frame_apellido.pack(pady=8)
    label_apellido = ct.CTkLabel(
        frame_apellido,
        text="Apellido:",
        bg_color=colorPrimario,
        font=("Inter", 20),
        text_color="white",
    )
    label_apellido.pack(side="left")
    caja_apellido = ct.CTkEntry(
        frame_apellido, placeholder_text="apellido", bg_color=colorPrimario
    )
    caja_apellido.pack(side="left", padx=8)
    caja_apellido.bind("<Return>", on_enter)

    frame_botones = tk.Frame(window, background=colorPrimario)
    frame_botones.pack(pady=8)
    boton_registrar = ct.CTkButton(
        frame_botones,
        text="Registrar",
        command=registrar,
        fg_color=colorSegundario,
        hover_color=colorT,
    )
    boton_registrar.pack(side="left", padx=8)
    boton_buscar = ct.CTkButton(
        frame_botones,
        text="Buscar",
        command=buscar,
        fg_color=colorSegundario,
        hover_color=colorT,
    )
    boton_buscar.pack(side="left", padx=8)

    window.mainloop()
