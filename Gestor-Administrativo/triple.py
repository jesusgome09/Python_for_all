import threading
import os

def funcion1():
    os.system("python3 Main.py")
def funcion2():
    os.system("python3 Main.py")
def funcion3():
    os.system("python3 Main.py")

t1 = threading.Thread(target=funcion1)
t2 = threading.Thread(target=funcion2)
t3 = threading.Thread(target=funcion3)

t1.start()
t2.start()
t3.start()
