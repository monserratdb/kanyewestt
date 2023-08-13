#Este archivo es para leer y elegir de manera aleatoria los contenidos de los archivos
#con estensión .csv entregados según lo delimitado en parametros.py
#además de instanciar los archivos como sus correspondientes clases
#y por último, tiene a la función crear archivo que permite escribir "DCCavaCava"

import random
from parametros import ARENA_INICIAL, CANTIDAD_EXCAVADORES_INICIALES

arenas_archivo_v1 = []
arenas_archivo = []
with open("arenas.csv", "r", encoding="UTF-8") as archivo:
    for linea in archivo:
        linea = linea.rstrip()
        separador = ","
        lista = linea.strip(",")
        arenas_archivo_v1.append(lista)
arenas_archivo_v1 = arenas_archivo_v1[1:] #elimino la primera fila del archivo
for strings in arenas_archivo_v1:
    lista = strings.split(",")
    arenas_archivo.append(lista)

excavadores_archivo_v1 = []
excavadores_archivo = []
with open("excavadores.csv", "r", encoding="UTF-8") as archivo:
    for linea in archivo:
        linea = linea.rstrip()
        separador = ","
        lista = linea.strip(",")
        excavadores_archivo_v1.append(lista)
excavadores_archivo_v1 = excavadores_archivo_v1[1:]
for i in excavadores_archivo_v1:
    lista = i.split(",")
    excavadores_archivo.append(lista)

consumibles_archivo_v1 = []
consumibles_archivo = []
with open("consumibles.csv", "r", encoding="UTF-8") as archivo:
    for linea in archivo:
        linea = linea.rstrip()
        separador = ","
        lista = linea.strip(",")
        consumibles_archivo_v1.append(lista)
consumibles_archivo_v1 = consumibles_archivo_v1[1:]
for i in consumibles_archivo_v1:
    lista = i.split(",")
    consumibles_archivo.append(lista)
 
tesoros_archivo_v1 = []
tesoros_archivo = []
with open("tesoros.csv", "r", encoding="UTF-8") as archivo:
    for linea in archivo:
        linea = linea.rstrip()
        separador = ","
        lista = linea.strip(",")
        tesoros_archivo_v1.append(lista)
tesoros_archivo_v1 = tesoros_archivo_v1[1:]
for i in tesoros_archivo_v1:
    lista = i.split(",")
    tesoros_archivo.append(lista)

#######################################
#de aquí en adelante sólo instanciaré cada una de las listas finales donde leo los archivos
#de modo que sean instancias de sus respectivas clases :)
import arenas
import excavadores
import items

arenas_instanciadas = []
for i in range(len(arenas_archivo)):
    nombre = arenas_archivo[i][0]
    tipo = arenas_archivo[i][1]
    rareza = arenas_archivo[i][2]
    humedad = arenas_archivo[i][3]
    dureza = arenas_archivo[i][4]
    estatica = arenas_archivo[i][5]
    if tipo == "normal":
        arena_i = arenas.ArenaNormal(nombre, tipo, rareza, humedad, dureza, estatica)
        arenas_instanciadas.append(arena_i)
    elif tipo == "mojada":
        arena_i = arenas.ArenaMojada(nombre, tipo, rareza, humedad, dureza, estatica)
        arenas_instanciadas.append(arena_i)
    elif tipo == "magnetica":
        arena_i = arenas.ArenaMagnetica(nombre, tipo, rareza, humedad, dureza, estatica)
        arenas_instanciadas.append(arena_i)
    elif tipo == "rocosa":
        arena_i = arenas.ArenaRocosa(nombre, tipo, rareza, humedad, dureza, estatica)
        arenas_instanciadas.append(arena_i)
    arena_i = arenas.Arena(nombre, tipo, rareza, humedad, dureza, estatica)
    arenas_instanciadas.append(arena_i)

#me faltó la parte de elegir una arena según ARENA_INICIAL siendo que ya las arenas estaban
#instanciadas. de todas formas dejo un código que logra hacer eso, pero con la arena como
#un elemento de una lista (para la que se extrae información desde el archivo arenas.csv)

# #para elegir una arena que sea del tipo especificado de manera random:
# largo_total_arenas = len(arenas_archivo)
# cumplen_tipo = []
# for i in range(largo_total_arenas):
#     if arenas_archivo[i][1] == ARENA_INICIAL:
#         cumplen_tipo.append(arenas_archivo[i]) #agrego a la arena y sus características
# largo_tipo = len(cumplen_tipo)
# posicion_aleatoria = random.randint(0, largo_tipo - 1)
# arena_aleatoria = cumplen_tipo[posicion_aleatoria]

excavadores_instanciados = []
for i in range(len(excavadores_archivo)):
    nombre = excavadores_archivo[i][0]
    tipo = excavadores_archivo[i][1]
    edad = excavadores_archivo[i][2]
    energia = excavadores_archivo[i][3]
    fuerza = excavadores_archivo[i][4]
    suerte = excavadores_archivo[i][5]
    felicidad = excavadores_archivo[i][6]
    if tipo == "docencio":
        excavador_i = excavadores.Docencio(nombre, tipo, edad, energia, fuerza, suerte, felicidad)
        excavadores_instanciados.append(excavador_i)
    elif tipo == "tareo":
        excavador_i = excavadores.Tareo(nombre, tipo, edad, energia, fuerza, suerte, felicidad)
        excavadores_instanciados.append(excavador_i)
    elif tipo == "hibrido":
        excavador_i = excavadores.Hibrido(nombre, tipo, edad, energia, fuerza, suerte, felicidad)
        excavadores_instanciados.append(excavador_i)
print(excavadores_instanciados)

#para elegir a los excavadores de manera random:
k = CANTIDAD_EXCAVADORES_INICIALES
equipo_aleatorio = random.SystemRandom().sample(excavadores_instanciados, k)
#al ser de random espero que se pueda usar :(

tesoros_instanciados = []
for i in range(len(tesoros_archivo)):
    nombre = tesoros_archivo[i][0]
    descripcion = tesoros_archivo[i][1]
    calidad = tesoros_archivo[i][2]
    cambio = tesoros_archivo[i][3]
    tesoro_i = items.Tesoros(nombre, descripcion, calidad, cambio)
    tesoros_instanciados.append(tesoro_i)

consumibles_instanciados = []
for i in range(len(consumibles_archivo)):
    nombre = consumibles_archivo[i][0]
    descripcion = consumibles_archivo[i][1]
    energia = consumibles_archivo[i][2]
    fuerza = consumibles_archivo[i][3]
    suerte = consumibles_archivo[i][4]
    felicidad = consumibles_archivo[i][5]
    consumible_i = items.Consumibles(nombre, descripcion, energia, fuerza, suerte, felicidad)
    consumibles_instanciados.append(consumible_i)

items_arena = [] #lista con dos listas :)
items_arena.append(consumibles_instanciados)
items_arena.append(tesoros_instanciados)

###########################################################
#finalmente la función que crea o sobreescribe el archivo DCCavaCava.txt
import os
#esto me crea archivo en la carpeta dnde se esté trabajando
def crear_archivo(nombre: str):
    with open(nombre, "w", encoding="UTF-8") as archivo:
        archivo.write("a")

auxiliar = True
if os.path.isfile("DCCavaCava.txt") == True:
    auxiliar
else:
    crear_archivo("DCCavaCava.txt")