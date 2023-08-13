from abc import ABC
from arenas import ArenaMagnetica, ArenaMojada, ArenaNormal, ArenaRocosa
from parametros import PROB_ENCONTRAR_ITEM, FELICIDAD_ADICIONAL_DOCENCIO, \
    FUERZA_ADICIONAL_DOCENCIO, ENERGIA_PERDIDA_DOCENCIO, ENERGIA_ADICIONAL_TAREO, \
    SUERTE_ADICIONAL_TAREO, EDAD_ADICIONAL_TAREO, FELICIDAD_PERDIDA_TAREO

class Excavadores(ArenaNormal, ArenaMagnetica, ArenaRocosa, ArenaMojada, ABC):
    def __init__(self, nombre, tipo, edad, energia, fuerza, suerte, felicidad, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self.tipo = tipo
        self.__edad = int(edad) 
        self.__energia = int(energia) 
        self.__fuerza = int(fuerza) 
        self.__suerte = int(suerte) 
        self.__felicidad = int(felicidad)

        @property
        def edad(self):
            return self.__edad
        @edad.setter
        def edad(self, valor):
            if valor < 18:
                self.__edad = 18
            elif valor > 60:
                self.__edad = 60

        @property
        def energia(self):
            return self.__energia
        @energia.setter
        def energia(self, valor):
            if valor < 0:
                self.__energia = 0
            elif valor > 100:
                self.__energia = 100

        @property
        def fuerza(self):
            return self.__fuerza
        @fuerza.setter
        def fuerza(self, valor):
            if valor < 1:
                self.__fuerza = 1
            elif valor > 10:
                self.__fuerza = 10

        @property
        def suerte(self):
            return self.__suerte
        @suerte.setter
        def suerte(self, valor):
            if valor < 1:
                self.__suerte = 1
            elif valor > 10:
                self.__suerte = 10

        @property
        def felicidad(self):
            return self.__felicidad
        @felicidad.setter
        def felicidad(self, valor):
            if valor < 1:
                self.__felicidad = 1
            elif valor > 10:
                self.__felicidad = 10
        
    def descansar(self):
        if self.__energia == 0:
                dias_descanso = int((self.__edad)/20)
                return self.nombre, dias_descanso
        else:
            return 0
        
    def encontrar_item(self):
        prob_encontrar_item = PROB_ENCONTRAR_ITEM*(self.__suerte/10)
        return self.nombre, prob_encontrar_item
    
    def gastar_energia(self):
        energia_gastada = int((10/self.__fuerza) + (self.__edad/6))
        self.__energia -= energia_gastada
        return self.nombre, energia_gastada
    
    def consumir(self):
        #no supe implementarlo :(
        return True


########################################################################
#TIPOS DE EXCAVADORES

class Docencio(Excavadores):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.cavar() != 0:
            self.__felicidad += FELICIDAD_ADICIONAL_DOCENCIO
            self.__fuerza += FUERZA_ADICIONAL_DOCENCIO
            self.__energia -= ENERGIA_PERDIDA_DOCENCIO

class Tareo(Excavadores):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.consumir() == True:
            self.__energia += ENERGIA_ADICIONAL_TAREO
            self.__suerte += SUERTE_ADICIONAL_TAREO
            self.__edad += EDAD_ADICIONAL_TAREO
            self.__felicidad -= FELICIDAD_PERDIDA_TAREO

class Hibrido(Tareo, Docencio, Excavadores):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gastar_energia = (self.gastar_energia)/2
        if self.__energia < 20:
            self.__energia = 20