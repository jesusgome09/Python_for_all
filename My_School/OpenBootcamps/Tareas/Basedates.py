#las base de datos son como un almacen
from sqlite3 import connect
import getpass

def Basedates():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")

def verifica_credenciales(username, password):

    conn = connect("miaplicacion.db")
    cursor = conn.cursor()

    query = f'SELECT id FROM users WHERE username="{username}" AND password="{password}"' # WHERE username="jesus"
    #cursor.execute("SELECT * FROM users")
    print("query a ejecutar:",query)

    rows = cursor.execute(query)
    data = rows.fetchone()
    print("data es:",type(data))


    cursor.close()
    conn.close()

    if data == None:
        return False
    else:
        return True

def crear_usuario(username, password, id):
    conn = connect("miaplicacion.db")
    cursor = conn.cursor()

    query = '''INSERT INTO users(id, username, password) VALUES(?,?,?)'''#existe una manera mas facil xD
    cursor.execute(query, (id, username, password))
    conn.commit() #esto es un comit con en github anemos que en conn coloque isolation_nevel=None
    cursor.close()
    conn.close()

crear_usuario("juan","1351",4)
Basedates()

