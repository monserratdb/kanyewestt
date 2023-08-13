# módulo solo para procesar y validar los resultados entregados
# por los jugadores

class Logica:
    # solo para verificar sumas y dados
    def __init__(self):
        pass

    def procesar(self, mensaje):
        try:
            accion = mensaje["acción"]
        except KeyError:
            print("no está la llave en el diccionario")

        if accion == "comenzar":
            estado = "comenzar juego"
            return estado

    def validar_numero(self, dado) -> bool:
        if len(dado) > 0 and len(dado) < 3:
            return dado.isdigit()
        else:
            return "imposible obtener 3 dígitos o 0"

    def sumar(self, dados):
        if self.validar_numero(dados):
            if dados > 12:
                print("imposible")
            elif dados < 2:
                print("imposible")
