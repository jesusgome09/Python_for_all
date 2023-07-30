import datetime

id_carro = 78945612378945
Status = False

def agregar_id(nuevo_id):
    id_carro = nuevo_id

def cambiar_status(status):
    if status == 'on':
        Status = True
    elif status == 'off':
        Status = False
