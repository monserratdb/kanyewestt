from PyQt5.QtCore import QObject, pyqtSignal


class Backend(QObject):
    senal_comenzar = pyqtSignal()
    senal_log = pyqtSignal(dict)
    senal_llena = pyqtSignal(bool)
    senal_partida = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def manejar_mensaje(self, event):
        try:
            accion = event["acción"]
        except KeyError:
            print("falló la llave")
        if accion == "comenzar":
            self.senal_comenzar.emit()

        elif accion == "sala llena":
            dic = {"estado": "sala llena"}
            self.senal_log.emit(dic)

        elif accion == "partida":
            dic = {"estado": "partida"}
            self.senal_log.emit(dic)

    def cambiar(self, event):
        if event == "sala llena":
            self.senal_llena.emit()
        elif event == "partida":
            self.senal_partida.emit()
