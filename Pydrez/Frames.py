import tkinter as tk

def cambiar_a_azul():
    frame2.pack_forget()
    frame.pack(expand=True, fill='both')

def cambiar_a_rojo():
    frame.pack_forget()
    frame2.pack(expand=True, fill='both')

window = tk.Tk()
window.geometry('500x500+400+100')

frame = tk.Frame(window, bg='blue', width=500, height=500)
frame.pack(expand=True, fill='both')

boton_frame = tk.Button(frame, text='poner azul', command=cambiar_a_rojo)
boton_frame.pack()

frame2 = tk.Frame(window, bg='red', width=500, height=500)

boton_frame2 = tk.Button(frame2, text='poner rojo', command=cambiar_a_azul)
boton_frame2.pack()

window.mainloop()
