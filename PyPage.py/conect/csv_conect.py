import csv
import random

def ingresar_Datos(Fp_file, dato):
    with open(Fp_file, 'a') as csvfile:
        Writer = csv.writer(csvfile)
        Writer.writerow(dato)

def Crear_e_ingresar_Datos(Fp_file, user, passw):
    with open(Fp_file, 'a') as csvfile:
        Writer = csv.writer(csvfile)
        ids = random.randrange(1000, 9999)
        Writer.writerow([user, passw, ids])
        return ids

def Leer_Datos(Fp_file):
    with open(Fp_file, 'r') as csvfile:
        Reader = csv.reader(csvfile)
        for row in Reader:
            print(row)
        
def verificar_Datos(Fp_file, user, passw):
    with open(Fp_file, 'r') as csvfile:
        Reader = csv.reader(csvfile)
        passw = f"{passw}"
        for row in Reader:
            if row[0] == user and row[1] == passw:
                print("Datos correctos")
                return True
        print("Datos incorrectos")
        return False
    
def verificador_avanzado(Fp_file, user, passw):
    with open(Fp_file, 'r') as csvfile:
        Reader = csv.reader(csvfile)
        passw = f"{passw}"
        for row in Reader:
            if row[0] == user and row[1] == passw:
                print("Usuario y contraseña en base de datos")
                return True
            elif row[0] == user and row[1]!= passw:
                print("Usuario en base de datos")
            elif row[1] == passw and row[0]!= user:
                print("Contraseña en base de datos")
        print("Usuario y contraseña desconocidos")
        return False

def verificador_user(Fp_file, user):
    with open(Fp_file, 'r') as csvfile:
        Reader = csv.reader(csvfile)
        for row in Reader:
            if row[0] == user:
                return True
        return False

def pedir_Datos(Fp_file,ids):
    with open(Fp_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == ids:
                return row[1]

def pedir_ids(Fp_file,user, passw):
    with open(Fp_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == user and row[1] == passw:
                return row[2]

def agregar_ids_a_BDI(Fp_file,ids):
    with open(Fp_file, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([ids])

def agregar_datos_a_BDI(Fp_file, ids, datos):
    filas = []
    with open(Fp_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            filas.append(row)

    for row in filas:
        if row[0] == ids:
            row.insert(1, datos)

    with open(Fp_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(filas)
                
agregar_datos_a_BDI("PyPage.py/conect/file.csv",3621,"Este es mi amigo juan")
    
    

#Crear_e_ingresar_Datos("PyPage.py/conect/file.csv","mijo",4561)
#verificar_Datos("PyPage.py/conect/file.csv","Jesus",3621)

        
