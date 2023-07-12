import tkinter as tk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500+400+100")
        self.title("Mi ventana favorita")

        self.inicio = Inicio(self)
        self.inicio.pack(expand=True, fill="both")

        self.finale = Finale(self)

class Inicio(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=500, height=500, bg="#e8a3a4")

        self.caja1 = tk.Entry(self, font=("Inter", 20))
        self.caja1.pack(fill="x", padx=20, pady=20, ipady=10)
        self.caja1.bind("<Return>", self.enviar)


        # Cargar la imagen
        imagen = Image.open("titulo.png")
        imagen = imagen.resize((200, 200))
        imagen = imagen.convert("RGBA")
        imagen = Image.alpha_composite(imagen, Image.new("RGBA", imagen.size, (0, 0, 0, 0)))
        imagen = Image.composite(imagen, (0, 0), mask=imagen)
        imagen_tk = ImageTk.PhotoImage(imagen)
        # Crear un Label y mostrar la imagen
        label_imagen = tk.Label(self, image=imagen_tk)
        label_imagen.image = imagen_tk
        label_imagen.pack()

    def enviar(self, event):
        if self.caja1.get() == "cambio":
            self.pack_forget()
            parent = self.master
            parent.finale.pack(expand=True, fill="both")

class Finale(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=500, height=500, bg="#e8e3a4")

        self.label = tk.Label(self, text="finalmente", font=("Inter", 20))
        self.label.pack(padx=50)

if __name__ == "__main__":
    window = Window()
    frame = Inicio(window)
    window.frame = frame
    window.mainloop()
