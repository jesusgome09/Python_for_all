import tkinter as tk

import customtkinter as ct


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600+260+50")
        self.title("Spash Car")

        self.inicio = Inicio(self)
        self.inicio.pack(fill="both", expand=True)

        self.how = How(self)

        # self.rastreo = Login(self)
        # self.rastreo.pack(fill="both", expand=True, padx=60)


# creo una variable para almacenar una informacion
informacion = "Bienvenido al mejor lavadero de autos de toda colombia"


class Inicio(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # agrego items

        self.titulo = tk.Label(
            self, text="LAVADERO DE AUTOS", font=("Comic Sans MS", 35, "italic")
        )
        self.titulo.pack(fill="x", pady=15)

        global informacion  # Importo una variable

        self.information = tk.Label(self, text=informacion, font=("Arial", 14))
        self.information.pack(fill="both")

        self.tamano = 40
        # Creo entry
        self.entry_mi_id = ct.CTkEntry(
            self,
            placeholder_text="MI ID CAR",
            height=45,
            width=350,
            font=("Arial", self.tamano),
        )
        self.entry_mi_id.pack(padx=20, pady=20)

        # Creo boton buscar
        self.buscar_button = ct.CTkButton(
            self, text="Buscar", width=350, height=45, font=("Arial", self.tamano)
        )
        self.buscar_button.pack(padx=20, pady=20)

        # Creo boton Iniciar seccion
        self.login_button = ct.CTkButton(
            self,
            text="Iniciar Seccion",
            width=350,
            height=45,
            font=("Arial", self.tamano),
        )
        self.login_button.pack(padx=20, pady=20)
        # Creo boton como encontrarnos
        self.how_button = ct.CTkButton(
            self,
            text="Como entontrarnos",
            width=350,
            height=45,
            font=("Arial", self.tamano),
            command=self.como_encontrarnos,
        )
        self.how_button.pack(padx=20, pady=20)

    def como_encontrarnos(self):
        self.pack_forget()
        parent = self.master
        parent.how.pack(expand=True, fill="both")


class Rastreo(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # variables

        self.idInteger = 12345678912345
        self.id = str(self.idInteger)
        self.cliente = "Juan Gonsalez"
        self.marca = "Honda"
        self.trabajador = "David Gomez"
        self.valorInteger = 12.456
        self.valor = str(self.valorInteger)
        self.fecha_final = "26/07/2023"
        self.fecha_inicial = "01/10/2005"
        self.tiempo_restante = "01:22"

        # frames

        self.frame1 = tk.Frame(self, height=120)
        self.frame2 = tk.Frame(self, height=120)
        self.frame3 = tk.Frame(self, height=120)

        # labels

        self.label_titulo = tk.Label(
            self, text="RASTREAR VEHÍCULO", font=("Comic Sans MS", 35, "italic")
        )
        self.label_id = tk.Label(self.frame1, text=f"Id: {self.id}", font=("Arial", 20))
        self.label_dueño = tk.Label(
            self.frame1, text=f"Cliente: {self.cliente}", font=("Arial", 20)
        )
        self.label_marca = tk.Label(
            self.frame2, text=f"Marca: {self.marca}", font=("Arial", 20)
        )
        self.label_trabajador = tk.Label(
            self.frame2, text=f"Trabajador(a): {self.trabajador}", font=("Arial", 20)
        )
        self.label_valor = tk.Label(
            self, text=f"Valor: ${self.valor}", font=("Arial", 20)
        )
        self.label_fecha_inicial = tk.Label(
            self,
            text=f"Fecha y hora de entrada: {self.fecha_inicial}",
            font=("Arial", 20),
        )
        self.label_fecha_final = tk.Label(
            self, text=f"Fecha y hora de salida: {self.fecha_final}", font=("Arial", 20)
        )
        self.label_tiempo_restante = tk.Label(
            self,
            text=f"Tiempo restante: {self.tiempo_restante} minutos",
            font=("Arial", 20),
        )

        # botones

        self.boton_llamar = ct.CTkButton(
            self.frame3, text="Llamar", font=("Arial", 35), width=200
        )
        self.boton_retroceder = ct.CTkButton(
            self.frame3, text="Retroceder", font=("Arial", 35), width=200
        )

        # empezamos a llamar a pack()

        self.label_titulo.pack(pady=10)
        self.label_id.pack(side="left")
        self.label_dueño.pack(side="right")
        self.frame1.pack(fill="x", pady=12)
        self.label_marca.pack(side="left")
        self.label_trabajador.pack(side="right")
        self.frame2.pack(fill="x", pady=12)
        self.label_valor.pack(pady=12)
        self.label_fecha_inicial.pack(pady=12)
        self.label_fecha_final.pack(pady=12)
        self.label_tiempo_restante.pack(pady=12)
        self.boton_llamar.pack(side="right")
        self.boton_retroceder.pack(side="left")
        self.frame3.pack(fill="x", pady=20, padx=60)


class Login(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # frames

        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        self.frame3 = tk.Frame(self)

        # labels

        self.label_titulo = tk.Label(
            self, text="Iniciar Seccion", font=("Comic Sans MS", 40, "italic")
        )
        self.label_usuario = tk.Label(
            self.frame1, text="Usuario: ", font=("Comic Sans MS", 26, "italic")
        )
        self.label_contrasena = tk.Label(
            self.frame2, text="Contraseña: ", font=("Comic Sans MS", 26, "italic")
        )
        self.label_advertencia = tk.Label(
            self,
            text="Recuerda cerrar seccion al terminar\n"
            + "Mantengamos el entorno libre de hackers",
            font=("Comic Sans MS", 12, "italic"),
        )
        self.imagen = tk.PhotoImage(file="Splash_Car\\advertencia.png")
        self.imagen = self.imagen.subsample(7, 7)
        self.icono_advertencia = tk.Label(self, image=self.imagen)

        # entrys

        self.entry_usuario = ct.CTkEntry(
            self.frame1,
            placeholder_text="Usuario o Correo electronico",
            font=("Comic Sans MS", 26, "italic"),
            width=400,
        )
        self.entry_contrasena = ct.CTkEntry(
            self.frame2,
            placeholder_text="************",
            font=("Comic Sans MS", 26, "italic"),
            width=400,
        )

        # botones

        self.boton_retroceder = ct.CTkButton(
            self.frame3,
            text="Retroseder",
            font=("Comic Sans MS", 30, "italic"),
            width=200,
        )
        self.boton_registrarse = ct.CTkButton(
            self.frame3,
            text="Registrarse",
            font=("Comic Sans MS", 30, "italic"),
            width=200,
        )
        self.boton_iniciar_seccion = ct.CTkButton(
            self.frame3,
            text="Iniciar seccion",
            font=("Comic Sans MS", 30, "italic"),
            width=200,
        )

        # llamar elementos

        self.label_titulo.pack(pady=20)
        self.label_usuario.pack(side="left")
        self.label_contrasena.pack(side="left")
        self.frame1.pack(fill="x", padx=116, pady=20)
        self.frame2.pack(fill="x", padx=60)
        self.icono_advertencia.pack(pady=15)
        self.label_advertencia.pack()

        self.entry_usuario.pack(side="left")
        self.entry_contrasena.pack(side="left")

        self.boton_retroceder.pack(side="left", padx=35)
        self.boton_registrarse.pack(side="left", padx=25)
        self.boton_iniciar_seccion.pack(side="left", padx=20)

        self.frame3.pack(fill="x", pady=40)


class How(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # frames

        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)

        # labels

        self.label_titulo = tk.Label(
            self, text="¿Como encontrarnos?", font=("Comic Sans MS", 35, "italic")
        )
        self.label_informacion = tk.Label(
            self,
            text="Nos encontramos en el punto mas cercano al sol",
            font=("Comic Sans MS", 20, "italic"),
        )
        self.imagen = tk.PhotoImage(file="Splash_Car\mapa.png")
        self.label_mapa = tk.Label(
            self.frame1,
            image=self.imagen,
            width=522,
            height=277,
            borderwidth=2,
            relief="solid",
        )

        # botones

        self.boton_llamar = ct.CTkButton(
            self.frame2, text="Llamar", font=("Comic Sans MS", 35), width=200
        )
        self.boton_chatear = ct.CTkButton(
            self.frame2, text="Chatear", font=("Comic Sans MS", 35), width=200
        )
        self.boton_retroceder = ct.CTkButton(
            self.frame2, text="Retroceder", font=("Comic Sans MS", 35), width=200
        )

        # llamamos elementos

        self.label_titulo.pack()
        self.label_informacion.pack()
        self.label_mapa.pack()
        self.frame1.pack(side="left")
        self.boton_llamar.pack(pady=20)
        self.boton_chatear.pack(pady=20)
        self.boton_retroceder.pack(pady=20)
        self.frame2.pack(side="right")


class Reg(tk.Frame):
    pass


class PanelAdmin(tk.Frame):
    pass


class Panel(tk.Frame):
    pass


class Añadir(tk.Frame):
    pass


class Entregar(tk.Frame):
    pass


class Emples(tk.Frame):
    pass


def run():
    window = Window()
    frame = Inicio(window)
    window.frame = frame
    window.mainloop()


run()  # eliminar
