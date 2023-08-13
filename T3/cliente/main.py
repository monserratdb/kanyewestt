from backend import Backend
from cliente import Cliente
from frontend import VentanaInicio, VentanaJuego, SalaLlena, Partida
from PyQt5.QtWidgets import QApplication
from jason import data
import sys


if __name__ == "__main__":
    # Hood para imprimir errores
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)
    sys.__excepthook__ = hook

    try:
        app = QApplication(sys.argv)

        # Usamos nuestras constantes
        if len(sys.argv) != 2:
            print("dar puerto como argumento :]")
            sys.exit(1)

        HOST = data("HOST")
        PORT = int(sys.argv[1])

        # instanciamos nuestro backend y frontend
        backend = Backend()
        cliente = Cliente(HOST, PORT)
        inicio = VentanaInicio()
        juego = VentanaJuego()
        llena = SalaLlena()
        partida = Partida()

        # cliente
        cliente.senal_manejar_mensaje.connect(backend.manejar_mensaje)
        cliente.senal_cerrar.connect(app.exit)

        # conectamos señales interfaz
        inicio.senal_comienza.connect(backend.senal_comenzar)
        inicio.senal_comienza.connect(juego.mostrar)
        backend.senal_llena.connect(llena.mostrar)
        backend.senal_partida.connect(llena.mostrar)

        # mostramos la ventana de inicio
        inicio.show()
        sys.exit(app.exec())

    except ConnectionError:
        print("ocurrió un error de conexión")
