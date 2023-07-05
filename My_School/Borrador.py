from customtkinter import (CTk, CTkButton, CTkFrame)

# Función para cambiar el frame
def cambiar_frame(frame):
    global f # Usamos una variable global para el frame actual
    f.destroy() # Destruimos el frame actual
    f = frame(master=root) # Creamos el nuevo frame con la clase que recibimos como parámetro
    f.pack(fill="both", expand=True) # Empaquetamos el nuevo frame

# Clase para el primer frame, con dos botones
class Frame1(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        button1 = CTkButton(self, text="Botón 1", command=lambda: print("Botón 1 presionado"))
        button1.pack()
        button2 = CTkButton(self, text="Ir al Frame 2", command=lambda: cambiar_frame(Frame2))
        button2.pack()

# Clase para el segundo frame, con un botón
class Frame2(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        button3 = CTkButton(self, text="Ir al Frame 1", command=lambda: cambiar_frame(Frame1))
        button3.pack()

# Creamos la ventana raíz
root = CTk()
root.geometry("300x200")

# Creamos el primer frame y lo empaquetamos
f = Frame1(master=root)
f.pack(fill="both", expand=True)

# Iniciamos el bucle principal
root.mainloop()
