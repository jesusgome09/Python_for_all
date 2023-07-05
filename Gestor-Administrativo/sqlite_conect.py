from sqlite3 import connect


def agregar(nombre, apellido, correo_electronico):
    nonn = connect("sqlite_conect.db", isolation_level=None)
    cursor = nonn.cursor()

    cursor.execute(
        f"INSERT INTO usuarios_universal(NOMBRE, APELLIDO, EMAIL) VALUES('{nombre}','{apellido}','{correo_electronico}')"
    )

    nonn.commit()
    cursor.close()
    nonn.close()
    return True


def verificador(nombre, apellido):
    nonn = connect("sqlite_conect.db")
    cursor = nonn.cursor()

    tam = cursor.execute(
        f"SELECT id FROM usuarios_universal WHERE NOMBRE='{nombre}' AND APELLIDO='{apellido}'"
    )
    resultado = tam.fetchone()

    cursor.close()
    nonn.close()

    if resultado == None:
        return False
    else:
        return True


def crear_tabla(name_table, campo1_key, campo2, campo3, campo4):
    nonn = connect("sqlite_conect.db", isolation_level=None)
    cursor = nonn.cursor()

    cursor.execute(
        f"CREATE TABLE '{name_table}'('{campo1_key}' INTEGER NOT NULL UNIQUE,'{campo2}' TEXT NOT NULL, '{campo3}'TEXT NOT NULL, '{campo4}' TEXT NOT NULL, PRIMARY KEY('{campo1_key}' AUTOINCREMENT))"
    )
    return "Tabla creada con exito"
    cursor.close()
    nonn.close()


def devuelve_datos(nombre, apellido):
    nonn = connect("sqlite_conect.db")
    cursor = nonn.cursor()

    tam = cursor.execute(
        f"SELECT ID,NOMBRE,APELLIDO,EMAIL FROM usuarios_universal WHERE NOMBRE='{nombre}' AND APELLIDO='{apellido}'"
    )
    resultado = tam.fetchone()

    cursor.close()
    nonn.close()

    return resultado


def eliminar(id):
    nonn = connect("sqlite_conect.db", isolation_level=None)
    cursor = nonn.cursor()

    cursor.execute(f"DELETE FROM usuarios_universal WHERE ID='{id}'")

    cursor.close()
    nonn.close()

    return True


# crear_tabla("usuarios_universal","ID","NOMBRE","APELLIDO","EMAIL")
# agregar("Jesus Elia", "Gomez Cogollo", "jesuseliasgomezcogollo@gmail.com")
# id = devuelve_datos("Jesus Elia","Gomez Cogollo")
# print(id[3])
