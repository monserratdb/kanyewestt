import arenas
import items
import random
from parametros import DIAS_TOTALES_TORNEO, PROB_INICIAR_EVENTO, PROB_LLUVIA, PROB_TERREMOTO, \
    PROB_DERRUMBE, METROS_PERDIDOS_DERRUMBE, FELICIDAD_PERDIDA, METROS_META

class Torneo(): #hereda de los 3 creoooo, items, arena y excavadores 
    def __init__(self, arena, equipo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.metros_logrados = 0 #parte siendo 0
        self.dia_actual = 1 #parte siendo 1 y cambia cuando Simular día
        self.dias_totales_torneo = DIAS_TOTALES_TORNEO
        self.arena_actual = arena
        self.eventos = ["lluvia", "derrumbre", "terremoto"] #conjunto de eventos q pueden ocurrir
        self.equipo = equipo
        self.mochila = [] #"items encontrados durante excavación"
        self.metros_cavados = float(self.metros_logrados)
        self.meta = float(METROS_META)
        self.dias_transcurridos = int(self.dia_actual)
        self.dias_totales = int(DIAS_TOTALES_TORNEO)

    def lluvia(self):
        if self.arena.tipo == "normal":
            self.arena = arenas.ArenaMojada()
            #self.arena.tipo = "mojada"
        elif self.arena.tipo == "rocosa":
            self.arena = arenas.ArenaMagnetica()
            #self.arena.tipo == "magnetica"
        return self.arena
    
    def terremoto(self):
        if self.arena.tipo == "normal":
            self.arena = arenas.ArenaRocosa()
            #self.arena.tipo = "rocosa"
        elif self.arena.tipo == "mojada":
            self.arena = arenas.ArenaMagnetica()
            #self.arena.tipo = "magnetica"
        return self.arena
    
    def derrumbe(self):
        if self.arena.tipo != "normal":
            self.arena = arenas.ArenaNormal()
            #self.arena.tipo = "normal"
            self.metros_cavados -= METROS_PERDIDOS_DERRUMBE
        return self.arena, self.metros_cavados
    
    def felicidad_perdida(self): #independiente del evento, el equipo pierde felicidad
        felicidad_perdida_equipo = 0
        for i in range(len(self.equipo)): #cada cosa de esta lista es una instancia de Excavadores()
            self.equipo[i].felicidad -= FELICIDAD_PERDIDA
            felicidad_perdida_equipo += FELICIDAD_PERDIDA
        return felicidad_perdida_equipo
    
    def ocurrencia_evento(self):
        eventos = []
        arenas = []
        if random() == PROB_INICIAR_EVENTO:
            if random() == PROB_DERRUMBE:
                eventos.append("derrumbe")
                arenas.append(self.derrumbe())
            elif random() == PROB_LLUVIA:
                eventos.append("lluvia")
                arenas.append(self.lluvia())
            elif random() == PROB_TERREMOTO:
                eventos.append("terremoto")
                arenas.append(self.terremoto())
        arena_final = arenas[-1]
        return eventos, arena_final
    
    def cavar(self):
        for i in self.equipo: #cada i es instancia de algún tipo de Excavador
            if i.energia > 0:
                numerador = (30 / i.edad) + (i.felicidad + i.fuerza * 2) / 10
                denominador = 10 * self.arena_actual.dificultad_arena
                metros_cavados = round((numerador) / denominador, 2)
                self.metros_cavados += metros_cavados #sumo cada uno de estos a metros del equipo
                return metros_cavados, i.nombre
            else:
                return 0
    
    def simular_dia_torneo(self):
        print(f"                     Día {self.dia_actual}                           \n" +
              "-----------------------------------------------------\n" +
              "Metros Cavados:\n"
        )
        for i in self.equipo:
            descansan = []
            if i.cavar != 0:
                print(f"{i.cavar[1]} ha cavado {i.cavar[0]} metros")
                self.metros_cavados += int(i.cavar[0])
            else:
                descansan.append(i)
        print(f"El equipo ha conseguido excavar {self.metros_cavados} metros\n")

        print("Items Encontrados:\n")
        # def encontrar_item(self):
        # prob_encontrar_item = PROB_ENCONTRAR_ITEM*(self.__suerte/10)
        # return self.nombre, prob_encontrar_item
        for i in self.equipo:
            encuentra = i.encontrar_item()
            consumible = 0
            tesoro = 0
            if encuentra[1] > 0.59 and encuentra[1] < 0.64:
                tipo_item = "Consumible"
                for j in self.mochila:
                    if self.mochila[j][1].startswith("Otorga"):
                        nombre_item = self.mochila[j][0]
                        consumible += 1
            else:
                tipo_item = "Tesoro"
                for j in self.mochila:
                    if self.mochila[j][2] == "1" or self.mochila[j][2] == "2":
                        nombre_item = self.mochila[j][0]
                        tesoro += 1
            print(f"{encuentra[0]} consiguió {nombre_item} del tipo {tipo_item}")
        totales = consumible + tesoro

        print(f"Se han encontrado {totales} items:\n" +
              f"- {consumible} consumibles.\n" +
              f"- {tesoro} tesoros.")
        ocurrencia = self.ocurrencia_evento()

        for i in ocurrencia[0]:
            print(f"¡Durante el día de trabajo ocurrió un evento {i}!")
        print(f"La arena final es del tipo {ocurrencia[1]}")

        felicidad = self.felicidad_perdida()
        print(f"Tu equipo ha perdido {felicidad} de felicidad\n")

        for i in descansan:
            print(f"{i} decidió descansar...")
        self.dia_actual += 1

    def mostrar_estado_torneo(self):
        excavadores_texto = ""
        print(f"""                     *** Estado Torneo ***
                  ------------------------------------------------------------------
                  Día actual: {self.dia_actual}
                  Tipo de arena: {self.arena}
                  Metros excavados: {self.metros_cavados}/{self.meta}
                  ------------------------------------------------------------------
                                         Excavadores
                  ------------------------------------------------------------------
                    Nombre   |  Tipo  | Edad | Energia | Fuerza | Suerte | Felicidad""")
        for i in self.equipo: #se supone q equipo es una lista de listas
            nombre = i.nombre
            tipo = i.tipo
            edad = str(i.edad)
            energia = str(i.energia)
            fuerza = str(i.fuerza)
            suerte = str(i.suerte)
            felicidad = str(i.felicidad)
            excavadores_texto += f"{nombre:10.10s} | {tipo:6.6s} | {edad:4.4s} | {energia:7.7s} | "
            excavadores_texto += f"{fuerza:6.6s} | {suerte:6.6s} | {felicidad:9.9s}"
            print(excavadores_texto)

    def ver_mochila(self):
        items_texto = ""
        print(f"                            *** Menú Ítems ***                                \n" +
               "-------------------------------------------------------------------------------\n" +
               "     Nombre       |    Tipo    |                Descripción\n" +
               "-------------------------------------------------------------------------------\n")
        for i in range(len(self.mochila)):
            nombre = self.mochila[i][0]
            tipo = "" #aquí digo si es consumible o tesoro
            descripcion = self.mochila[i][1]
            items_texto += f"[{i+1}] {nombre:15.15s} | {tipo:12.12s} | {descripcion}"
        print("-------------------------------------------------------------------------------")

    def usar_consumible(self): #aplica efectos del consumible a cada excavador del equipo
        consumible = items.Consumibles()
        for i in self.equipo: #se supone q cada i es una instancia de self.equipo
            consumible.cambio_energia()
            consumible.cambio_fuerza()
            consumible.cambio_felicidad()
            consumible.cambio_suerte()

    def abrir_tesoro(self): #al seleccionar tesoro dentro de la mochila, se activa su efecto
        tesoro = items.Tesoros()
        for i in self.equipo:
            tesoro.self.equipo_agregar.append(i)
        tesoro.cambia()