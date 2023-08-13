from os import path 

def cargar_tablero(nombre_archivo: str) -> list:
    with open(path.join("Archivos", nombre_archivo), "r") as tab:
        linea = tab.readline()
        lista = linea.split(",")
        n_filas = int(lista.pop(0))
        tablero_final = [lista[i:i+n_filas] for i in range(0, len(lista), n_filas)]
    return tablero_final

def verificar_valor_bombas(tablero: list) -> int:
    contador_bombas_invalidas = 0
    n = len(tablero)
    for lista in tablero:
        for elemento in lista:
            if elemento != "-" and elemento != "T":
                elemento_numerico = int(elemento)
                if elemento_numerico < 2:
                    contador_bombas_invalidas += 1
                elif elemento_numerico >= 2 * n + 1:
                    contador_bombas_invalidas += 1
    return contador_bombas_invalidas

#aquí no respeté PEP8 porque cuando intenté usar las definiciones hechas en las líneas
#de la 31 a la 34, me falló el programa
def verificar_tortugas(tablero: list) -> int:
    largo = len(tablero)
    invalidas = 0
    for i in range(largo):
        for j in range(largo):
        #arriba=tablero[i-1][j]
        #abajo=tablero[i+1][j]
        #derecha=tablero[i][j+1]
        #izquierda=tablero[i][j-1]
            if tablero[i][j] == "T":
        #primera fila
                if i == 0:
                    if j == 0:
                        if tablero[i][j]==tablero[i][j+1] or tablero[i][j]==tablero[i+1][j]:
                            invalidas += 1
                    elif j > 0 and j < largo - 1:
                        if tablero[i][j]==tablero[i][j-1] or tablero[i][j]==tablero[i][j+1] or tablero[i][j]==tablero[i+1][j]:
                            invalidas += 1
                    elif j == largo - 1:
                        if tablero[i][j]==tablero[i+1][j] or tablero[i][j]==tablero[i][j-1]:
                            invalidas += 1
                #filas entremedio
                elif i > 0 and i < largo - 1:
                    if j == 0:
                        if tablero[i][j]==tablero[i][j+1] or tablero[i][j]==tablero[i+1][j] or tablero[i][j]==tablero[i-1][j]:
                            invalidas += 1
                    elif j > 0 and j < largo -1:
                        if tablero[i][j]==tablero[i][j-1] or tablero[i][j]==tablero[i][j+1] or tablero[i][j]==tablero[i+1][j] or tablero[i][j]==tablero[i-1][j]:
                            invalidas += 1
                    elif j == largo -1:
                        if tablero[i][j]==tablero[i+1][j] or tablero[i][j]==tablero[i][j-1] or tablero[i][j]==tablero[i-1][j]:
                            invalidas += 1
                #fila final
                elif i == largo - 1:
                    if j == 0:
                        if tablero[i][j]==tablero[i][j+1] or tablero[i][j]==tablero[i-1][j]:
                            invalidas+=1
                    elif j > 0 and j < largo - 1:
                        if tablero[i][j]==tablero[i][j-1] or tablero[i][j]==tablero[i][j+1] or tablero[i][j]==tablero[i-1][j]:
                            invalidas += 1
                    elif j == largo - 1:
                        if tablero[i][j]==tablero[i-1][j] or tablero[i][j]==tablero[i][j-1]:
                            invalidas += 1

    return invalidas


def verificar_alcance_bomba_vertical(tablero, coordenadas):
    i = coordenadas[0]
    j = coordenadas[1]
    borde = len(tablero) - 1
    alcance_vertical = 1 #parte siendo 1 porque considera el espacio donde está la bomba
    if tablero[i][j] == "T" or tablero[i][j] == "-":
        return 0
    else:
        arriba = True
        abajo = True
        while arriba:
            if i == 0:
                arriba = False
            else:
                i -= 1 #subí a la fila anterior 
                if tablero[i][j] != "T":
                    alcance_vertical += 1
                else:
                    arriba = False
        i = coordenadas[0] #ahora revisa abajo pero de la coordenada inicial
        while abajo:
            if i == borde:
                abajo = False
            else:
                i += 1 #baja a la fila siguiente 
                if tablero[i][j] != "T":
                    alcance_vertical += 1
                else:
                    abajo = False
    return alcance_vertical

def verificar_alcance_bomba_horizontal(tablero, coordenadas):
    i = coordenadas[0]
    j = coordenadas[1]
    borde = len(tablero) - 1
    alcance_horizontal = 0 #en vertical ya consideré a la celda donde está la bomba
    if tablero[i][j] == "T" or tablero[i][j] == "-":
        return 0
    else:
        derecha = True
        izquierda = True
        while derecha:
            if j == borde:
                derecha = False
            else:
                j += 1 #reviso la posición de la derecha 
                if tablero[i][j] != "T":
                    alcance_horizontal += 1
                else:
                    derecha = False
        j = coordenadas[1] #ahora revisa izquierda pero de la coordenada incial
        while izquierda:
            if j == 0:
                izquierda = False
            else:
                j -= 1 #reviso la posición de la izquierda
                if tablero[i][j] != "T":
                    alcance_horizontal += 1
                else:
                    izquierda = False
    return alcance_horizontal

def verificar_alcance_bomba(tablero: list, coordenadas: tuple) -> int:
    horizontal = verificar_alcance_bomba_horizontal(tablero, coordenadas)
    vertical = verificar_alcance_bomba_vertical(tablero, coordenadas)
    alcance_total = horizontal + vertical
    return alcance_total

def verifica_regla_1(tablero):
    largo = len(tablero)
    auxiliar = False
    for i in range(largo):
        for j in range(largo):
            if tablero[i][j].isdigit() == True:
                coordenadas = (i,j)
                alcance = verificar_alcance_bomba(tablero, coordenadas)
                if int(tablero[i][j]) == alcance:
                    auxiliar = True
                else:
                    auxiliar
            else:
                auxiliar
    return auxiliar

def verifica_regla_3(tablero: list) -> int:
    no_cumple_r3 = 0
    for lista in tablero:
        for elemento in lista:
            if len(elemento) > 1:
                no_cumple_r3 += 1
    return no_cumple_r3

def solucionar_tablero(tablero: list) -> list:
    regla_1 = verifica_regla_1(tablero)
    regla_2 = verificar_valor_bombas(tablero)
    regla_3 = verifica_regla_3(tablero)
    regla_4 = verificar_tortugas(tablero)
    largo = len(tablero)
    if regla_2 == 0:
        for i in range(largo):
            for j in range(largo):
                if tablero[i][j] == "-":
                    if regla_1 != True: #aún hay al menos una bomba en la que su alcance no es igual a su int
                        if regla_4 == 0: #no hay tortugas juntas
                            tablero[i][j] = "T" #modifica el - por un T
        return tablero
    else:
        return None
    
def guardar_tablero(nombre_archivo: str, tablero: list) -> None:
    separa_string = nombre_archivo.split(".")
    separa_string[0] = separa_string[0] + "_sol"
    nombre_final = ".".join(separa_string)
    vacio = ""
    largo = len(tablero)
    for i in range(largo):
        for j in range(largo):
            vacio += tablero[i][j]
            vacio += ","
    c_final = ","
    escribe = vacio.rstrip(c_final)
    nuevo_archivo = open(nombre_final, "w")
    nuevo_archivo.write(escribe)
    nuevo_archivo.close()
    return None

if __name__ == "__main__":
    tablero_2x2 = [
        ['-', 2],
        ['-', '-']
    ]
    resultado = verificar_valor_bombas(tablero_2x2)
    print(resultado)  # Debería ser 0

    resultado = verificar_alcance_bomba(tablero_2x2, (0, 1))
    print(resultado)  # Debería ser 3

    tablero_resuelto = solucionar_tablero(tablero_2x2)
    print(tablero_resuelto)

    tablero_2x2_sol = [
        ['T', "2"],
        ['-', '-']
    ]

    resultado = verificar_alcance_bomba(tablero_2x2, (0, 1))
    print(resultado)  # Debería ser 2

    resultado = verificar_tortugas(tablero_2x2_sol)
    print(resultado)  # Debería ser 0