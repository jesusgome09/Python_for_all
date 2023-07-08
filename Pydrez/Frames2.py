import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500+400+100')

        self.frame = FrameAzul(self)
        self.frame.pack(expand=True, fill='both')

class FrameAzul(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='blue', width=500, height=500)

        self.boton = tk.Button(self, text='poner azul', command=self.cambiar_a_rojo)
        self.boton.pack()

    def cambiar_a_rojo(self):
        self.pack_forget()
        parent = self.master
        parent.frame2.pack(expand=True, fill='both')

class FrameRojo(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='red', width=500, height=500)

        self.boton = tk.Button(self, text='poner rojo', command=self.cambiar_a_azul)
        self.boton.pack()

    def cambiar_a_azul(self):
        self.pack_forget()
        parent = self.master
        parent.frame.pack(expand=True, fill='both')

if __name__ == "__main__":
    app = Aplicacion()
    frame2 = FrameRojo(app)
    app.frame2 = frame2
    app.mainloop()
