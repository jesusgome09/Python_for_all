import os
from sqlite3 import connect, Error

absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
path+="\\"
ubicacion = path + "datebase.db"


def agregar_usuario(
    nombres,
    apellidos,
    correo,
    celular,
    username,
    identificacion,
    fecha_nacimiento,
    modo_lavado,
    rango,
):
    rango = 1
    file_ = connect(ubicacion, isolation_level=None)
    cursor = file_.cursor()
    try:
        cursor.execute(
            f"INSERT INTO usuarios(nombres, apellidos, correo, celular, username, identificacion, fecha_nacimiento, modo_lavado, rango) VALUES('{nombres}', '{apellidos}', '{correo}',{celular}, '{username}', {identificacion}, '{fecha_nacimiento}', '{modo_lavado}', {rango})"
        )
    except Error as e:
        return e
    file_.close()
    return True


def verificar_correo(correo, password):
    file_ = connect(ubicacion)
    cursor = file_.cursor()
    cursor.execute(
        f"SELECT identificacion FROM usuarios WHERE correo = '{correo}' AND password = '{password}'"
    )

    resultado = cursor.fetchall()
    file_.close()
    return resultado


def verificar_username(username, password):
    file_ = connect(ubicacion)
    cursor = file_.cursor()
    cursor.execute(
        f"SELECT identificacion FROM usuarios WHERE username = '{username}' AND password = '{password}'"
    )

    resultado = cursor.fetchall()
    file_.close()
    return resultado


def agregar_auto(
    id_,
    nombre_cliente,
    marca,
    valor,
    fecha_entrada,
    hora_entrada,
    tiempo,
    trabajador,
):
    file_ = connect(ubicacion)
    cursor = file_.cursor()
    cursor.execute(
        f"INSERT INTO carros (id, nombre_cliente, marca, valor, fecha_entrada, tiempo, trabajador, hora_entrada) VALUES({id_}, '{nombre_cliente}', '{marca}', {valor}, '{fecha_entrada}', {tiempo}, '{trabajador}','{hora_entrada}')"
    )
    file_.commit()
    file_.close()
    return True


def solicitar_marcas():
    file_ = connect(ubicacion, "r")
    cursor = file_.cursor()
    cursor.execute("SELECT DISTINCT marcas FROM carros WHERE fecha_salida IS NULL")
    marcas = [marca[0] for marca in cursor.fetchall()]
    file_.close()
    return marcas


def solicitar_clientes_segun_marcas(marca):
    file_ = connect(ubicacion, "r")
    cursor = file_.cursor()
    cursor.execute(
        f"SELECT nombre_cliente, id FROM carros WHERE marca = '{marca}' AND fecha_Salida IS NULL"
    )

    resultado = cursor.fetchall()
    nombres_clientes, id_ = zip(*resultado)
    file_.close()

    return list(nombres_clientes), list(id_)


def entregar_auto(id_, fecha_salida, hora_salida):
    file_ = connect(ubicacion, "a", isolation_level=None)
    cursor = file_.cursor()
    cursor.execute(
        f"UPDATE carros SET fecha_salida = '{fecha_salida}', hora_salida = '{hora_salida}' WHERE id = {id_}"
    )
    file_.close()

    return True


def solicitar_usuario():
    try:
        with connect(ubicacion) as file_:
            cursor = file_.cursor()
            cursor.execute("SELECT nombres, apellidos, identificacion FROM usuarios")

            respuesta = cursor.fetchall()

            return respuesta
    except Error as e:
        print(f"Error al solicitar usuarios: {e}")
        return []


def actualizar_usuario(identificacion, rango_nuevo):
    file_ = connect(ubicacion, "a", isolation_level=None)
    cursor = file_.cursor()

    cursor.execute(
        f"UPDATE usuarios SET rango = {rango_nuevo} WHERE identificacion = {identificacion}"
    )
    return True


def despedir_usuario(identificacion):
    file_ = connect(ubicacion, "a", isolation_level=None)
    cursor = file_.cursor()

    cursor.execute(f"DELETE FROM usuarios WHERE identificacion='{identificacion}'")

    file_.close()
    return True


def buscar_auto(id_):
    with connect(ubicacion) as file_:
        cursor = file_.cursor()
        cursor.execute(f"SELECT * FROM carros WHERE id={id_}")

        resultado = cursor.fetchall()
        return resultado


def devolver_datos_carros(id_):
    with connect(ubicacion) as file_:
        cursor = file_.cursor()
        cursor.execute(
            f"SELECT id,nombre_cliente,marca,trabajador, valor, fecha_salida,fecha_entrada, hora_entrada, tiempo, hora_salida FROM carros WHERE id= {id_}"
        )

        respuesta = cursor.fetchall()
        lista = []
        for i in respuesta:
            lista += i

        return lista


def agregar_columna_hora_entrada():
    # 1. Abrir la base de datos (si no existe, se creará automáticamente).
    conn = connect(ubicacion)

    try:
        # 2. Obtener un objeto cursor.
        cursor = conn.cursor()

        # 3. Ejecutar la consulta para agregar la nueva columna.
        cursor.execute("ALTER TABLE carros ADD COLUMN fecha_entrada TEXT NOT NULL ")

        # 4. Hacer commit para guardar los cambios en la base de datos.
        conn.commit()
    except Error as e:
        print(f"Error al agregar la columna: {e}")
    finally:
        # 5. Cerrar la conexión con la base de datos.
        conn.close()


#agregar_auto(12346578912345,'pedro lopez','Honda',12000,'30/07/2023','01:06',2,1068823310)
agregar_usuario("juan david", "lopez", "juandsemse@gmail.com",3131351351,"juandavid",1068814578,"30/07/2003","Manual",1)
