import tkinter as tk

import customtkinter as ct
import SqliteP
import Logica


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600+260+50")
        self.title("Spash Car")

        self.shared_data = {}

        self.inicio = Inicio(self)
        self.inicio.pack(fill="both", expand=True)

        self.how = How(self)
        self.rastreo = Rastreo(self)
        self.login = Login(self)
        self.reg = Reg(self)
        self.panel = Panel(self)

        # self.rastreo = Reg(self)
        # self.rastreo.pack(fill="both", expand=True, padx=60)


# creo una variable para almacenar una informacion
informacion = "Bienvenido al mejor lavadero de autos de toda colombia"


class Inicio(tk.Frame):  # Todavia falta arreglar el boton Buscar
    def __init__(self, parent):
        super().__init__(parent)

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
            self,
            text="Buscar",
            width=350,
            height=45,
            font=("Arial", self.tamano),
            command=self.buscar,
        )
        self.buscar_button.pack(padx=20, pady=20)

        # Creo boton Iniciar seccion
        self.login_button = ct.CTkButton(
            self,
            text="Iniciar Seccion",
            width=350,
            height=45,
            font=("Arial", self.tamano),
            command=self.iniciar_seccion,
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

        self.buscar_button.bind("<Return>", command=self.buscar_con_intro)
        self.inicializar = Rastreo(self)


    def como_encontrarnos(self):
        self.pack_forget()
        parent = self.master
        parent.how.pack(expand=True, fill="both")

    def buscar(self):
        id__ = self.entry_mi_id.get()
        if SqliteP.buscar_auto(id__):
            self.inicializar.agregar_datos(id__)
            self.pack_forget()
            parent = self.master
            parent.rastreo.pack(expand=True, fill="both")

        else:
            tk.messagebox.showerror(title="Error", message="No se a podido encontrar")

    def iniciar_seccion(self):
        self.pack_forget()
        parent = self.master
        parent.login.pack(expand=True, fill="both")

    def buscar_con_intro(self, event):
        print("holaaaa")
        self.buscar()


class Rastreo(tk.Frame):  # Todavia me falta mucho
    def __init__(self, parent):
        super().__init__(parent)

        # variables
        self.idInteger = 12345
        self.id = str(self.idInteger)
        self.cliente = "Juan Gonsalez"
        self.marca = "Honda"
        self.trabajador = "David Gomez"
        self.valorInteger = 12.456
        self.valor = str(self.valorInteger)
        self.fecha_final = "26/07/2023 10:12"
        self.fecha_inicial = "01/10/2005 21:30"
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
        self.frame1.pack(fill="x", pady=12, padx=35)
        self.label_marca.pack(side="left")
        self.label_trabajador.pack(side="right")
        self.frame2.pack(fill="x", pady=12, padx=35)
        self.label_valor.pack(pady=12)
        self.label_fecha_inicial.pack(pady=12)
        self.label_fecha_final.pack(pady=12)
        self.label_tiempo_restante.pack(pady=12)
        self.boton_llamar.pack(side="right")
        self.boton_retroceder.pack(side="left")
        self.frame3.pack(fill="x", pady=20, padx=60)

    def agregar_datos(self, id__):
        print("sucedio")

        datos = SqliteP.devolver_datos_carros(id__)

        self.label_id.config(text=f'Id: {datos[0]}')
        self.id = datos[0]
        self.cliente = datos[1]
        self.marca = datos[2]
        self.trabajador = datos[3]
        self.valorInteger = datos[4]
        if datos[5] != "":
            self.fecha_final = datos[5]
            self.fecha_final += f" {datos[9]}"
        else:
            self.fecha_final = "No Disponible"
        self.fecha_inicial = datos[6]
        self.fecha_inicial += f" {datos[7]}"
        # self.tiempo_restante = Logica.ver_tiempo_restante(datos[6],datos[8])



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
            command=self.iniciar_seccion
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

        self.boton_retroceder.pack(side="left", padx=45)
        self.boton_registrarse.pack(side="left", padx=35)
        self.boton_iniciar_seccion.pack(side="left", padx=30)

        self.frame3.pack(fill="x", pady=40)

    def iniciar_seccion(self):
        user = self.entry_usuario.get()
        passw = self.entry_contrasena.get()

        if SqliteP.verificar_correo(user, passw) or SqliteP.verificar_username(user, passw):
            self.pack_forget()
            parent = self.master
            parent.panel.pack(fill='both', expand=True)
        else:
            tk.messagebox.showerror(title='No puede iniciar seccion', message='Usuario o contraseña incorrecta')

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
        self.frame1.pack(side="left", padx=50)
        self.boton_llamar.pack(pady=20)
        self.boton_chatear.pack(pady=20)
        self.boton_retroceder.pack(pady=20)
        self.frame2.pack(side="right", padx=40)


class Reg(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # frames

        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        self.frame3 = tk.Frame(self)
        self.frame4 = tk.Frame(self)
        self.frame4_5 = tk.Frame(self)
        self.frame5 = tk.Frame(self)

        # labels

        self.label_titulo = tk.Label(
            self, text="Registrarse", font=("Comic Sans MS", 40, "italic")
        )
        self.label_nombre = tk.Label(
            self.frame1, text="Nombres: ", font=("Comic Sans MS", 18, "italic")
        )
        self.label_apellido = tk.Label(
            self.frame1, text="Apellidos: ", font=("Comic Sans MS", 18, "italic")
        )
        self.label_correo = tk.Label(
            self.frame2, text="Correo: ", font=("Comic Sans MS", 18, "italic")
        )
        self.label_celular = tk.Label(
            self.frame2, text="Celular: ", font=("Comic Sans MS", 18, "italic")
        )
        self.label_nombre_de_usuario = tk.Label(
            self.frame3,
            text="Nombre de usuario: ",
            font=("Comic Sans MS", 18, "italic"),
        )
        self.label_cc = tk.Label(
            self.frame3, text="C.C: ", font=("Comic Sans MS", 18, "italic")
        )
        self.label_fecha_de_nacimiento = tk.Label(
            self.frame4_5,
            text="Fecha de nacimiento",
            font=("Comic Sans MS", 18, "italic"),
        )
        self.label_como_lavas = tk.Label(
            self.frame4_5, text="¿Como lavas?", font=("Comic Sans MS", 18, "italic")
        )

        # entrys

        self.entry_nombres = ct.CTkEntry(
            self.frame1,
            placeholder_text="Juan Manuel",
            font=("Comic Sans MS", 18, "italic"),
            width=200,
        )
        self.entry_apellidos = ct.CTkEntry(
            self.frame1,
            placeholder_text="Perez Novoa",
            font=("Comic Sans MS", 18, "italic"),
            width=200,
        )
        self.entry_correo = ct.CTkEntry(
            self.frame2,
            placeholder_text="juanpereznova@gmail.com",
            font=("Comic Sans MS", 18, "italic"),
            width=250,
        )
        self.entry_celular = ct.CTkEntry(
            self.frame2,
            placeholder_text="1234567894",
            font=("Comic Sans MS", 18, "italic"),
            width=200,
        )
        self.entry_nombre_de_usuario = ct.CTkEntry(
            self.frame3,
            placeholder_text="juan12",
            font=("Comic Sans MS", 18, "italic"),
            width=200,
        )
        self.entry_cc = ct.CTkEntry(
            self.frame3,
            placeholder_text="1605549973",
            font=("Comic Sans MS", 18, "italic"),
            width=200,
        )

        # date piker

        self.date_piker_fecha_de_nacimiento = ct.CTkEntry(
            self.frame4,
            placeholder_text="01/10/2000",
            font=("Comic Sans MS", 18, "italic"),
            width=200,
        )

        # box

        self.var1 = tk.StringVar(self)
        self.var1.set("Manual")

        self.opciones = ["Manual", "Automatico"]
        self.box_como_lavas = ct.CTkOptionMenu(
            self.frame4,
            variable=self.var1,
            values=self.opciones,
            font=("Comic Sans MS", 18, "italic"),
            width=200,
        )

        # radiobutton

        self.var2 = tk.IntVar(value=0)
        self.radiobutton_tyc = ct.CTkRadioButton(
            self,
            text="Acepto los terminos y condiciones",
            variable=self.var2,
            value=1,
            font=("Comic Sans MS", 20, "italic"),
            command=self.acepto_terminos_y_condiciones,
        )

        # botones

        self.boton_retroceder = ct.CTkButton(
            self.frame5,
            text="Retroceder",
            font=("Comic Sans MS", 18, "italic"),
            width=220,
            height=45,
        )
        self.boton_registrarse = ct.CTkButton(
            self.frame5,
            text="Registrarse",
            font=("Comic Sans MS", 18, "italic"),
            width=220,
            height=45,
            state="normal",
        )

        # llamamos elementos

        self.label_titulo.pack()

        self.frame1.pack(fill="x", pady=20)
        self.frame2.pack(fill="x", pady=20)
        self.frame3.pack(fill="x", pady=30)
        self.frame4_5.pack(fill="x", padx=30)
        self.frame4.pack(fill="x", pady=10, padx=30)
        self.label_nombre.pack(side="left")
        self.entry_nombres.pack(side="left")
        self.entry_apellidos.pack(side="right")
        self.label_apellido.pack(side="right")
        self.label_correo.pack(side="left")
        self.entry_correo.pack(side="left", padx=30)
        self.entry_celular.pack(side="right")
        self.label_celular.pack(side="right", padx=30)
        self.label_nombre_de_usuario.pack(side="left")
        self.entry_nombre_de_usuario.pack(side="left")
        self.entry_cc.pack(side="right")
        self.label_cc.pack(side="right")

        self.label_fecha_de_nacimiento.pack(side="left", padx=39)
        self.date_piker_fecha_de_nacimiento.pack(side="left", padx=50)
        self.label_como_lavas.pack(side="right", padx=30)
        self.box_como_lavas.pack(side="right")
        self.radiobutton_tyc.pack(pady=15)
        self.frame5.pack(fill="x", pady=30, padx=30)
        self.boton_retroceder.pack(side="left")
        self.boton_registrarse.pack(side="right")

        self.boton_registrarse.configure(state="disabled")
        self.boton_retroceder.configure(command=self.retroceder)

    def acepto_terminos_y_condiciones(self):
        self.boton_registrarse.configure(state="normal")

    def retroceder(self):
        self.pack_forget()
        parent = self.master
        parent.inicio.pack(fill="both", expand=True)


class PanelAdmin(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


class Panel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


class Añadir(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


class Entregar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


class Emples(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


def run():
    window = Window()
    frame = Inicio(window)
    window.frame = frame
    window.mainloop()


run()  # eliminar
