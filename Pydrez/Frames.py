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
        super().__init__(parent, width=500, height=500)

        # creacion de label titulo
        label = Clabel(self, text='Pydrez', font=('Arial',80), text_color='black', fg_color='transparent')
        label2 = Clabel(self, text='Pydrez', font=('Arial',80), text_color='white', fg_color='transparent')
        label.place(x=90, y=20)
        label2.place(x=100, y=20)

class Clabel(ct.CTkLabel):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)



if __name__ == '__main__':
    window = Window()
    frame = Inicio(window)
    window.frame = frame
    window.mainloop()
