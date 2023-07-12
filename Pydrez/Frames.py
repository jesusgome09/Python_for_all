import tkinter as tk
import customtkinter as ct

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500+400+100')
        self.title('Pydrez')

        self.inicio = Inicio(self)
        self.inicio.pack(fill='both', expand=True)


class Inicio(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=500, height=500, bg='#E2A146')

        # creacion de label titulo
        label = Clabel(self, text='Pydrez', font=('Arial',80), text_color='black', fg_color='transparent')
        label.pack()
        #creacion de botones
        inciar_juego = Cboton(self, text='Iniciar Juego')
        creditos = Cboton(self, text='Creditos')
        inciar_juego.pack(ipadx=5, ipady=5, pady=50)
        creditos.pack(ipadx=5, ipady=5, pady=10)

class Clabel(ct.CTkLabel):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
class Cboton(ct.CTkButton):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs, font=('Inter',50), text_color='black', hover_color='grey', fg_color='white')




if __name__ == '__main__':
    window = Window()
    frame = Inicio(window)
    window.frame = frame
    window.mainloop()
