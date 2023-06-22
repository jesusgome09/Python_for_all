from tkinter import Tk, Label, Entry, Button

def obtener_valores():
    total = int(total_entry.get())
    A = int(a_entry.get())
    B = int(b_entry.get())
    C = int(c_entry.get())
    AB = int(ab_entry.get())
    BC = int(bc_entry.get())
    AC = int(ac_entry.get())
    ABC = int(abc_entry.get())

    #conjuntos(total, A, B, C, AB, BC, AC, ABC)

# Crear la ventana principal
ventana = Tk()
ventana.title("Creador de Conjuntos")

# Etiquetas
Label(ventana, text="Total:").grid(row=0, column=0)
Label(ventana, text="A:").grid(row=1, column=0)
Label(ventana, text="B:").grid(row=2, column=0)
Label(ventana, text="C:").grid(row=3, column=0)
Label(ventana, text="A y B:").grid(row=4, column=0)
Label(ventana, text="B y C:").grid(row=5, column=0)
Label(ventana, text="A y C:").grid(row=6, column=0)
Label(ventana, text="ABC:").grid(row=7, column=0)

# Campos de entrada
total_entry = Entry(ventana)
a_entry = Entry(ventana)
b_entry = Entry(ventana)
c_entry = Entry(ventana)
ab_entry = Entry(ventana)
bc_entry = Entry(ventana)
ac_entry = Entry(ventana)
abc_entry = Entry(ventana)

total_entry.grid(row=0, column=1)
a_entry.grid(row=1, column=1)
b_entry.grid(row=2, column=1)
c_entry.grid(row=3, column=1)
ab_entry.grid(row=4, column=1)
bc_entry.grid(row=5, column=1)
ac_entry.grid(row=6, column=1)
abc_entry.grid(row=7, column=1)

# Botón
Button(ventana, text="Generar gráfico", command=obtener_valores).grid(row=8, columnspan=2)

# Iniciar el bucle principal de la ventana
ventana.mainloop()