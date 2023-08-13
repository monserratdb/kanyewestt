from front_end import VentanaInicio, VentanaJuego
from back_end import JuegoConstructor
from PyQt5.QtWidgets import QApplication
import sys
from mapas_hechos import VentanaJuegoMapas

class LuigisMansion:

    def __init__(self):

        self.ventana_inicial = VentanaInicio()
        self.ventana_juego_c = VentanaJuego()
        self.ventana_juego_m = VentanaJuegoMapas()
        self.backend = JuegoConstructor()

    def conectar(self):
        self.ventana_inicial.senal_usuario.connect(self.backend.comprobar_usuario)
        self.backend.senal_respuesta.connect(self.ventana_inicial.validacion)

        self.ventana_inicial.senal_abrir.connect(self.ventana_juego_c.mostrar)

    def iniciar(self):
        self.ventana_inicial.show()


if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    game = LuigisMansion()
    game.conectar()
    game.iniciar()

    sys.exit(app.exec())