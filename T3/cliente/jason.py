# sólo para obtener la info de parametros.json
import json


def data(llave):
    with open("parametros.json") as file:
        parametros = json.load(file)
    valor = parametros[llave]
    return valor
