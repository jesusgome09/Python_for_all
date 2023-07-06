import tkinter as tk

import customtkinter as ct
import Operaciones
import webbrowser


def Panel():
    # agregamos funciones

    def num0():
        caja_Operaciones.insert("end", "0")

    def num1():
        caja_Operaciones.insert("end", "1")

    def num2():
        caja_Operaciones.insert("end", "2")

    def num3():
        caja_Operaciones.insert("end", "3")

    def num4():
        caja_Operaciones.insert("end", "4")

    def num5():
        caja_Operaciones.insert("end", "5")

    def num6():
        caja_Operaciones.insert("end", "6")

    def num7():
        caja_Operaciones.insert("end", "7")

    def num8():
        caja_Operaciones.insert("end", "8")

    def num9():
        caja_Operaciones.insert("end", "9")

    def operacion_suma():
        caja_Operaciones.insert("end", "+")

    def operacion_resta():
        caja_Operaciones.insert("end", "-")

    def operacion_multiplicacion():
        caja_Operaciones.insert("end", "*")

    def operacion_division():
        caja_Operaciones.insert("end", "/")

    def coma():
        caja_Operaciones.insert("end", ".")

    def eliminar():
        contenido_actual = caja_Operaciones.get()
        nuevo_contenido = contenido_actual[:-1]
        caja_Operaciones.delete(0, "end")
        caja_Operaciones.insert(0, nuevo_contenido)

    def operacion_enviar():
        datos = caja_Operaciones.get()
        resultado = Operaciones.funcion(datos)
        caja_Operaciones.delete(0, "end")
        caja_Operaciones.insert(0, resultado)

    def operacion_enviarr(event):
        datos = caja_Operaciones.get()
        resultado = Operaciones.funcion(datos)
        caja_Operaciones.delete(0, "end")
        caja_Operaciones.insert(0, resultado)

    color_principal = "#d9d9d9"
    color = "#d9d9d9"

    def fondo_blanco():
        caja_Operaciones.configure(bg_color="white")
        window.config(background="white")
        titulo.configure(bg_color="white", text_color="black")
        frame1.configure(background="white")
        frame2.configure(background="white")
        frame3.configure(background="white")
        frame4.configure(background="white")
        menu.configure(background="white")

    def fondo_negro():
        caja_Operaciones.configure(bg_color="black")
        window.config(background="black")
        titulo.configure(bg_color="black", text_color="white")
        frame1.configure(background="black")
        frame2.configure(background="black")
        frame3.configure(background="black")
        frame4.configure(background="black")
        menu.configure(
            background="black",
        )

    def default():
        caja_Operaciones.configure(bg_color=color)
        window.config(background=color)
        titulo.configure(bg_color=color, text_color="black")
        frame1.configure(background=color)
        frame2.configure(background=color)
        frame3.configure(background=color)
        frame4.configure(background=color)
        menu.configure(background=color)

    def Youtube():
        url = "https://www.youtube.com/channel/UCqVmDF4sLF8umTHAiIr1uTA?sub_confirmation=1"
        webbrowser.open(url)
    def Github():
        url = "https://github.com/Joseph-Garcia"
        webbrowser.open(url)

    # creamos una ventana y configuramos
    window = tk.Tk()
    window.title("Calculatore")
    window.geometry("360x470+500+120")
    window.config(background=color_principal)

    # Creamos un menu principal y configuramos
    menu = tk.Menu(window)
    window.config(menu=menu)
    menu.configure(background=color_principal)


    opciones_menu = tk.Menu(menu)
    menu.add_cascade(label="Ver", menu=opciones_menu)
    opciones_menu.add_command(label="Fondo blanco", command=fondo_blanco)
    opciones_menu.add_command(label="Fondo negro", command=fondo_negro)
    opciones_menu.add_command(label="Fondo por defecto", command=default)
    opciones_menu2 = tk.Menu(menu)
    menu.add_cascade(label='Create By', menu=opciones_menu2)
    opciones_menu2.add_command(label="Youtube")
    opciones_menu2.add_command(label="GitHub")
    menu.add_command(label="Salir", command=window.destroy)

    # Creamos un titulo y configuramos
    titulo = ct.CTkLabel(
        window,
        text="CALCULATOR",
        font=("Inter", 20),
        bg_color=color_principal,
    )
    titulo.pack(fill="x")

    # Creamos y configuramos un entry principal
    caja_Operaciones = ct.CTkEntry(
        window,
        justify="right",
        placeholder_text="5+5",
        font=("Inter", 50),
    )
    caja_Operaciones.pack(fill="x", padx=10)
    caja_Operaciones.focus_set()
    caja_Operaciones.bind("<Return>", operacion_enviarr)

    # creamos la primera columna de botones
    frame1 = tk.Frame(window, background=color_principal)
    frame1.pack(
        side="left",
    )
    # agregamos botones 0,1,4 y 7
    boton_1 = ct.CTkButton(
        frame1, text="1", font=("Inter", 40), width=70, height=70, command=num1
    )
    boton_0 = ct.CTkButton(
        frame1, text="0", font=("Inter", 40), width=70, height=70, command=num0
    )
    boton_4 = ct.CTkButton(
        frame1, text="4", font=("Inter", 40), width=70, height=70, command=num4
    )
    boton_7 = ct.CTkButton(
        frame1, text="7", font=("Inter", 40), width=70, height=70, command=num7
    )
    # inicializamos botones
    boton_0.pack(padx=10, pady=10)
    boton_1.pack(padx=10, pady=10)
    boton_4.pack(padx=10, pady=10)
    boton_7.pack(padx=10, pady=10)

    # creamos la segunda columna de botones
    frame2 = tk.Frame(window, background=color_principal)
    frame2.pack(side="left")
    # creamos botones 8,5,2 y ,
    boton_8 = ct.CTkButton(
        frame2, text="8", font=("Inter", 40), width=70, height=70, command=num8
    )
    boton_5 = ct.CTkButton(
        frame2, text="5", font=("Inter", 40), width=70, height=70, command=num5
    )
    boton_2 = ct.CTkButton(
        frame2, text="2", font=("Inter", 40), width=70, height=70, command=num2
    )
    boton_coma = ct.CTkButton(
        frame2, text=".", font=("Inter", 40), width=70, height=70, command=coma
    )
    # inicializamos botones
    boton_8.pack(padx=10, pady=10)
    boton_5.pack(padx=10, pady=10)
    boton_2.pack(padx=10, pady=10)
    boton_coma.pack(padx=10, pady=10)
    # creamos tercera columna de botones
    frame3 = tk.Frame(window, background=color_principal)
    frame3.pack(side="left")
    # creamos botones 9,6,3,/
    boton_9 = ct.CTkButton(
        frame3, text="9", font=("Inter", 40), width=70, height=70, command=num9
    )
    boton_6 = ct.CTkButton(
        frame3, text="6", font=("Inter", 40), width=70, height=70, command=num6
    )
    boton_3 = ct.CTkButton(
        frame3, text="3", font=("Inter", 40), width=70, height=70, command=num3
    )
    boton_div = ct.CTkButton(
        frame3,
        text="/",
        font=("Inter", 40),
        width=70,
        height=70,
        command=operacion_division,
    )
    # inicializamos botones
    boton_9.pack(padx=10, pady=10)
    boton_6.pack(padx=10, pady=10)
    boton_3.pack(padx=10, pady=10)
    boton_div.pack(padx=10, pady=10)
    # creamos cuarta columna de botones
    frame4 = tk.Frame(window, background=color_principal)
    frame4.pack(side="left")
    # creamos botones del, suma, resta, multi, igual
    boton_del = ct.CTkButton(
        frame4,
        text="<-",
        font=("Inter", 40),
        width=70,
        height=56,
        fg_color="#f40403",
        hover_color="#b20000",
        command=eliminar,
    )
    boton_suma = ct.CTkButton(
        frame4,
        text="+",
        font=("Inter", 40),
        width=70,
        height=56,
        command=operacion_suma,
    )
    boton_resta = ct.CTkButton(
        frame4,
        text="-",
        font=("Inter", 40),
        width=70,
        height=56,
        command=operacion_resta,
    )
    boton_mult = ct.CTkButton(
        frame4,
        text="x",
        font=("Inter", 40),
        width=70,
        height=56,
        command=operacion_multiplicacion,
    )
    boton_enviar = ct.CTkButton(
        frame4,
        text="=",
        font=("Inter", 40),
        width=70,
        height=56,
        command=operacion_enviar,
    )
    # inicializamos botones
    boton_del.pack(padx=10, pady=8)
    boton_suma.pack(padx=10, pady=8)
    boton_resta.pack(padx=10, pady=8)
    boton_mult.pack(padx=10, pady=8)
    boton_enviar.pack(padx=10, pady=8)

    # iniciamos loop
    window.mainloop()
