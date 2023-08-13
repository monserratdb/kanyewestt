# sólo para obtener la info de parametros.json
import json


def data(llave):
    with open("parametros.json") as file:
        parametros = json.load(file)
    valor = parametros[llave]
    return valor
# HOST = parametros["HOST"]
# N_PONDERADOR = parametros["N_PONDERADOR"]
# BUFFER_SIZE = parametros["BUFFER_SIZE"]
# NUMERO_VIDAS = parametros["NUMERO_VIDAS"]
# NUMERO_JUGADORES = parametros["NUMERO_JUGADORES"]
# NOMBRES_DISPONIBLES = parametros["NOMBRES_DISPONIBLES"]
