from abc import ABC
import random
from parametros import POND_ARENA_NORMAL, PROB_ENCONTRAR_ITEM

class Arena(ABC):
    def __init__(self, nombre, tipo, humedad, rareza, dureza, estatica, *args, **kwargs):
        self.nombre = nombre
        self.tipo = tipo
        self.__humedad = int(humedad)
        self.__rareza = int(rareza)
        self.__dureza = int(dureza)
        self.__estatica = int(estatica)
        #self.items = items_arena
        numerador = (self.__rareza - self.__humedad + self.__dureza + self.__estatica)
        self.dificultad_arena = round((numerador/40), 2)

    @property
    def rareza(self) -> int:
        return self.__rareza
    @rareza.setter
    def rareza(self, valor):
        if valor < 1:
            self.__rareza = 1
        elif valor > 10:
            self.__rareza = 10

    @property
    def humedad(self) -> int:
        return self.__humedad
    @humedad.setter
    def humedad(self, valor):
        if valor < 1:
            self.__humedad = 1
        elif valor > 10:
            self.__humedad = 10

    @property
    def dureza(self) -> int:
        return self.__dureza
    @dureza.setter
    def rareza(self, valor):
        if valor < 1:
            self.__dureza = 1
        elif valor > 10:
            self.__dureza = 10

    @property
    def estatica(self) -> int:
        return self.__estatica
    @estatica.setter
    def estatica(self, valor):
        if valor < 1:
            self.__estatica = 1
        elif valor > 10:
            self.__estatica = 10

##################################################################
#TIPOS DE ARENAS
class ArenaNormal(Arena):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dificultad_arena = self.dificultad_arena * POND_ARENA_NORMAL

class ArenaMojada(Arena):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prob_encontrar_item = PROB_ENCONTRAR_ITEM
        self.prob_encontrar_tesoro = 0.5
        self.prob_encontrar_consumbible = 0.5 #tienen igual probabilidad de ser encontrados

class ArenaRocosa(Arena):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        numerador = self.__rareza + self.__humedad + 2*self.__dureza + self.__estatica
        self.dificultad_arena = round((numerador/50), 2)

class ArenaMagnetica(Arena):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.humedad = random.randint(1, 10)
        self.dureza = random.randint(1, 10) #redefinimos la propertie sg enunciado