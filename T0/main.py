import os
import functions
import tablero
camino = "Archivos"
archivos_existentes: list = os.listdir(camino)

#defino antes el menu_de_accion porque lo usaré de inmediato en un caso específico de menu_de_inicio
def menu_de_accion():
    visible = int(input("   Menú de acciones   \n" +
                        "1. Mostrar tablero\n" +
                        "2. Validar tablero\n" +
                        "3. Validar solución\n" +
                        "4. Solucionar tablero\n" +
                        "5. Salir del programa\n"
                        "\n" +
                        "Indique su opción:\n"))
    return visible

archivo = input("   Menú de inicio   \n" +
                "Ingrese nombre de archivo\n")
if archivo in archivos_existentes:
    print("Abriendo Menú de Acciones")
    opcion_escogida = 0
    while opcion_escogida != 5:
        opcion_escogida = menu_de_accion()

        if opcion_escogida == 1:
            info_tablero = functions.cargar_tablero(archivo)
            tablero.imprimir_tablero(info_tablero)
        
        if opcion_escogida == 2:
            info_tablero = functions.cargar_tablero(archivo)
            bombas = functions.verificar_valor_bombas(info_tablero) #regla 2
            tortugas = functions.verificar_tortugas(info_tablero) #regla 4
            if bombas == 0 and tortugas == 0:
                print("Tablero válido")
            else:
                print("Tablero inválido")
        
        if opcion_escogida == 3:
            info_tablero = functions.cargar_tablero(archivo)
            bombas = functions.verificar_valor_bombas(info_tablero) #regla2
            tortugas = functions.verificar_tortugas(info_tablero) #regla 4
            regla_3 = functions.verifica_regla_3(info_tablero) #regla 3
            regla_1 = functions.verifica_regla_1(info_tablero) #regla 1
            if bombas == 0 and tortugas == 0 and regla_3 == 0 and regla_1 == True:
                print("Tablero válido")
            else:
                print("Tablero inválido")

        if opcion_escogida == 4:
            info_tablero = functions.cargar_tablero(archivo)
            solucion = functions.solucionar_tablero(info_tablero)
            if solucion != None:
                guarda_sol = functions.guardar_tablero(archivo, solucion)
                tablero.imprimir_tablero(solucion)
            else:
                print("El tablero no tiene solución")

        if opcion_escogida == 5:
            print("Saliendo del programa . . .")

        no_es_numero = opcion_escogida.isdigit()
        if opcion_escogida > 5 or no_es_numero == False:
            print("Opción inválida, intente nuevamente")

else:
    print("Archivo inexistente")
    print("Cerrando programa")
