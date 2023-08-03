import datetime

def hora(hora_inicial, tiempo):
    hora_actual = datetime.datetime.now()

    hora_inicial_obj = datetime.datetime.strptime(hora_inicial, "%H:%M")
    hora_final_obj = hora_inicial_obj + datetime.timedelta(hours=tiempo)

    if hora_actual > hora_final_obj:
        return "Listo"

    tiempo_restante_obj = hora_final_obj - hora_actual
    tiempo_restante = str(tiempo_restante_obj).split('.')[0]

    return tiempo_restante
