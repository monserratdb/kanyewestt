ANCHO_GRILLA = 11 # NO EDITAR
LARGO_GRILLA = 16 # NO EDITAR

# Complete con los demás parámetros
CANTIDAD_VIDAS = 4
TIEMPO_CUENTA_REGRESIVA = 45 #son segundos
MULTIPLICADOR_PUNTAJE = 2

#para el nombrede usuario que juega 
MIN_CARACTERES = 3
MAX_CARACTERES = 10

#velocidad luigi
MIN_VELOCIDAD = 0.2
MAX_VELOCIDAD = 0.8

#para el modo constructor
MAXIMO_VERTICAL = 3
MAXIMO_HORIZONTAL = 4
MAXIMO_PARED = 2
MAXIMO_ROCA = 3
MAXIMO_FUEGO = 3
LUIGI = 1
ESTRELLA = 1

#rutas / paths
import os

maps = "mapas"
mapas: list = os.listdir(maps)
MAPA_1 = mapas[0]
MAPA_2 = mapas[1]
MAPA_3 = mapas[2]
MAPA_4 = mapas[3]

sonidos = "sounds"
sounds: list = os.listdir(sonidos)
SONIDO_PIERDE = sounds[0]
SONIDO_GANA = sounds[1]

# elements = "./sprites/Elementos"
# Elementos: list = os.listdir(elements)

# background = "./sprites/Fondos"
# Fondos: list = os.listdir(background)
RUTA_FONDO_INICIO = "./sprites/Fondos/fondo_inicio.png"

RUTA_BORDERMAP = "./sprites/Elementos/bordermap.png"
RUTA_FIRE = "./sprites/Elementos/fire.png"
RUTA_LOGO = "./sprites/Elementos/logo.png"
RUTA_OSSTAR = "./sprites/Elementos/osstar.png"
RUTA_ROCK = "./sprites/Elementos/rock.png"
RUTA_WALL = "./sprites/Elementos/wall.png"


# characters = "./sprites/Elementos"
# Personajes: list = os.listdir(characters)

# print(Elementos, Fondos, Personajes)