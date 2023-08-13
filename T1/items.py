from abc import ABC
import arenas
import excavadores
from  torneo import equipo, arena_actual

class Items(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__()

class Consumibles(Items):
    def __init__(self, nombre, descripcion, energia, fuerza, suerte, felicidad, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self.descripcion = descripcion
        self.energia = int(energia)
        self.fuerza = int(fuerza)
        self.suerte = int(suerte)
        self.felicidad = int(felicidad)

    def cambio_energia(self):
        excavador = excavadores.Excavadores() #esto está mal pero no me da tiempo de cambiarlo:(
        excavador.self.__energia += self.energia 
        return excavador.self.__energia #valor en que queda la energia dsp de consumir
    
    def cambio_fuerza(self):
        excavador = excavadores.Excavadores() #esto está mal pero no me da tiempo de cambiarlo:(
        excavador.self.__fuerza += self.fuerza 
        return excavador.self.__fuerza
    
    def cambio_suerte(self):
        excavador = excavadores.Excavadores() #esto está mal pero no me da tiempo de cambiarlo:(
        excavador.self.__suerte += self.suerte 
        return excavador.self.__suerte
    
    def cambio_felicidad(self):
        excavador = excavadores.Excavadores() #esto está mal pero no me da tiempo de cambiarlo:(
        excavador.self.__felicidad += self.felicidad
        return excavador.self.__felicidad

class Tesoros(Items):
    def __init__(self, nombre, descripcion, calidad, cambio, *args, **kwargs):
        super().__init__()
        self.nombre = nombre
        self.descripcion = descripcion
        self.calidad = calidad
        self.cambio = cambio #str q dice un tipo de arena o de excavador
        self.equipo_agregar = []

    def cambia(self):
        if self.calidad == "1":
            if self.cambio == "hibrido":
                hibrido = excavadores.Hibrido()
                equipo.append(hibrido)
                return equipo

            elif self.cambio == "docencio":
                docencio = excavadores.Docencio()
                equipo.append(docencio)

            elif self.cambio == "tareo":
                tareo = excavadores.Tareo()
                equipo.append(tareo)
#################calidad 2
        elif self.calidad == "2":
            if self.cambio == "normal":
                arena_actual = arenas.ArenaNormal()
                #arena.self.tipo = "normal"
                return arena_actual

            elif self.cambio == "magnetica":
                arena_actual = arenas.ArenaMagnetica()
                #arena.self.tipo = "magnetica"
                return arena_actual

            elif self.cambio == "mojada":
                arena_actual = arenas.ArenaNormal()
                #arena.self.tipo = "mojada"
                return arena_actual

            elif self.cambio == "rocosa":
                arena_actual = arenas.ArenaRocosa()
                #arena.self.tipo = "rocosa"
                return arena_actual
