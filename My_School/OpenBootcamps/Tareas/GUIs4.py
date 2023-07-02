import tkinter as tki
from tkinter import ttk  # sirve para que los componentes tengan mas estilo
# practicamente el del sistema operativo

window = tki.Tk()

#   0  1  2
# 0 x  x  x
# 1 x  x  x
# 2 x  x  x

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

listas = ["windows 10", "MacOS", "Linux"]
listass = tki.StringVar(value=listas)
listBox = tki.Listbox(window,height=20, listvariable=listass)
frame = ttk.Frame(window)
label = ttk.Label(window, text="Hola")
label.grid(column=0, row=0, sticky=tki.W)
frame.grid(column=0, row=0, sticky=tki.W)
listBox.grid(column=0, row=0, sticky=tki.W)
def mifuncion():
    print("Hola")
selected = tki.StringVar()
radioButton1 = tki.Radiobutton(window, text="si", value='1', variable=selected, state="disabled")
radioButton2 = tki.Radiobutton(window, text="no", value='2', variable=selected,state="disabled")
radioButton3 = tki.Radiobutton(window, text="tal vez", value='3', variable=selected)
radioButton1.grid(column=0, row=1, padx=5, pady=5)
radioButton2.grid(column=0, row=2, padx=10, pady=10)
radioButton3.grid(column=0, row=3, padx=15, pady=15)
#tambien existe checkbutton
#hay que crealo, spera
cb = tki.Checkbutton(window, text="salir", variable=selected, command=mifuncion(), state="normal")
cb.grid(column=2, row=2)
window.mainloop()

# etiqueta user
user_label = ttk.Label(window, text="Username: ")
user_label.grid(column=0, row=0, sticky=tki.W, padx=5, pady=5)
# NTRY user
user_entry = ttk.Entry(window)
user_entry.grid(column=1, row=0, sticky=tki.W)
# stikt.W la letra W significa Sur en ingles, es como Norte, sur, este y oeste
# etiqueta user
passw_label = ttk.Label(window, text="Pasword: ")
passw_label.grid(column=0, row=1, sticky=tki.E, padx=5, pady=5)
# entry password
user_entry = ttk.Entry(window, show="*")
user_entry.grid(column=1, row=1, sticky=tki.W)

# boton

login_button = ttk.Button(window, text="Log in")
login_button.grid(sticky=tki.E, column=1, row=2)

exit_button = ttk.Button(window, text="Exit")
exit_button.grid(sticky=tki.W, column=0, row=2)
