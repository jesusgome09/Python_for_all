import csv

def ingresar_Datos(Fp_file="Direccion relativa del archivo", dato="Datos que quiere colocar"):
    with open(Fp_file, 'a') as csvfile:
        Writer = csv.writer(csvfile)
        Writer.writerow(dato)

def Crear_e_ingresar_Datos(Fp_file, user="Nombre de usuario", passw="COntraseña del nombre de usuario"):
    with open(Fp_file, 'a') as csvfile:
        Writer = csv.writer(csvfile)
        Writer.writerow([user, passw])

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