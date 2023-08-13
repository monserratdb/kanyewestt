
import os
from parametros import DIAS_TOTALES_TORNEO, ARENA_INICIAL
#import archivos
#primero trabajo con un menú manager cuyo código
#se basa en el que nos dieron en la Sala de Ayuda

VOLVER = "volver"
SALIR = "salir"
def menu_de_inicio():
    while True:
        print("""
        *** Menú de Inicio ***
        ----------------------
        [1] Nueva partida
        [2] Cargar partida
        [3] Salir
        """)
        eleccion = input("Indique su opción (1, 2 o 3): ")
        if eleccion == "1":
            return "acción"
        elif eleccion == "2":
            if os.path.isfile("DCCavaCava.txt") == True:
                print("DCCavaCava.txt")
                return "acción"
            else:
                print("DCCavaCava no existe! Seleccione 1 para jugar o 3 para salir")
        elif eleccion == "3":
            print("Saliendo del programa . . .")
            return SALIR
        else:
            print("Opción inválida, intente nuevamente")

def menu_de_accion():
    while True:
        dia = 1
        #equipo = archivos.equipo_aleatorio
        #arena = "normal"
        #torneo_actual = torneo.Torneo(arena, equipo)
        print("  *** Menú Principal ***  \n" +
              "--------------------------\n" +
              #f"Día torneo DCCavaCava: {torneo_actual.dia_actual}/{DIAS_TOTALES_TORNEO}\n"
              f"Día torneo DCCavaCava: {dia}/{DIAS_TOTALES_TORNEO}\n" +
              #f"Tipo de arena: {torneo_actual.arena_actual}\n"
              f"Tipo de arena: {ARENA_INICIAL}\n" +
              "\n" +
              "[1] Simular día torneo \n" +
              "[2] Ver estado torneo\n" +
              "[3] Ver ítems\n" +
              "[4] Guardar partida\n" +
              "[5] Volver\n" +
              "[6] Salir del programa\n" +
              "\n"
            )
        eleccion = input("Indique su opción (1, 2, 3, 4, 5 o 6): ")
        if eleccion == "1":
            #torneo_actual.simular_dia_torneo()
            print("simulando día")
            dia += 1
        elif eleccion == "2":
            #torneo.mostrar_estado_torneo()
            #torneo_actual.mostrar_estado_torneo()
            print("viendo estado torneo")
        elif eleccion == "3":
            #torneo_actual.ver_mochila()
            print("viendo items")
        elif eleccion == "4":
            print("guardando partida")
            #strings_archivo = torneo_actual.simular_dia_torneo()
            #archivos.crear_archivo(strings_archivo)
        elif eleccion == "5":
            return VOLVER
        elif eleccion == "6":
            print("Saliendo del programa . . .")
            return SALIR
        else:
            print("opción inválida, intente nuevamente")

def menu_manager():
    retorno_menu = None
    historial = ["ir_menu_1"]
    respuesta = ""
    while respuesta != SALIR:
        estado_actual = historial[-1]

        if estado_actual == "ir_menu_1":
            respuesta = menu_de_inicio()
        
        elif estado_actual == "acción":
            respuesta = menu_de_accion()
            
        if respuesta == VOLVER:
            historial.pop()
            
        elif respuesta.startswith("acc"):
            historial.append(respuesta)

menu_manager()