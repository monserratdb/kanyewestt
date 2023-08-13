from PyQt5.QtCore import QObject, QTimer, pyqtSignal, Qt
from PyQt5.QtGui import QKeyEvent
from random import randint
import parametros as p


class Luigi(QObject):

    senal_zapping = pyqtSignal(bool)

    def __init__(self, x: int, y: int, senal_fin_luigi: pyqtSignal, senal_mover: pyqtSignal):
        super().__init__()
        self.x = x
        self.y = y
        self.senal_mover = senal_mover
        self.senal_fin_luigi = senal_fin_luigi
        self._muere = False
        self._vidas = p.CANTIDAD_VIDAS

    @property
    def muere(self):
        return self._muere

    @muere.setter
    def muere(self, new_value: bool):
        if new_value:
            self._muere = new_value
            self.senal_fin_luigi.emit(True)

    @property
    def vidas(self):
        return self._vidas

    @vidas.setter
    def vidas(self, new_value: int):
        self._vidas = new_value
        if self.vidas <= 0:
            self.senal_fin_luigi.emit("rip luigi </3")

    # movimiento hacia arriba [W]
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_W and not event.isAutoRepeat():
            self.senal_zapping.emit(True)

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_W and not event.isAutoRepeat():
            self.senal_zapping.emit(False)

    # movimiento hacia abajo [S]
    def keyPressEventS(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_S and not event.isAutoRepeat():
            self.senal_zapping.emit(True)

    def keyReleaseEventS(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_S and not event.isAutoRepeat():
            self.senal_zapping.emit(False)

    # movimiento hacia la derecha [D]
    def keyPressEventD(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_D and not event.isAutoRepeat():
            self.senal_zapping.emit(True)

    def keyReleaseEventD(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_D and not event.isAutoRepeat():
            self.senal_zapping.emit(False)

    # movimiento hacia la izquierda [A]
    def keyPressEventA(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_A and not event.isAutoRepeat():
            self.senal_zapping.emit(True)

    def keyReleaseEventA(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_A and not event.isAutoRepeat():
            self.senal_zapping.emit(False)


class Fantasmas(QObject):
    identificador = 0

    def __init__(self, x: int, y: int, senal_cambio_direccion: pyqtSignal, senal_mover: pyqtSignal):
        super().__init__()
        self.id = Fantasmas.identificador
        Fantasmas.identificador += 1
        self.x = x
        self.y = y
        self.senal_mover = senal_mover
        self.direccion = senal_cambio_direccion

        self.timer_movimiento = QTimer(self)
        ponderador_velocidad_fantasmas = randint(p.MIN_VELOCIDAD, p.MAX_VELOCIDAD)
        tiempo = 1 / ponderador_velocidad_fantasmas
        self.timer_movimiento.setInterval(tiempo)
        self.timer_movimiento.timeout.connect(self.mover)


class FantasmaVertical(Fantasmas):

    def __init__(self):
        super().__init__()

    def mover(self):
        self.y += 1
        self.senal_mover.emit(self.id, self.x, self.y)
        if self.y >= (p.LARGO_GRILLA - 2):
            self.y += 1
            # se empieza a mover hacia arriba
        # si choca cn algo IMPENETRABLE cambia dirección ! falta hacer eso
        # impenetrable != inamovible


class FantasmaHorizontal(Fantasmas):
    ANCHO_GRILLA = 11  # NO EDITAR
    LARGO_GRILLA = 16

    def __init__(self):
        super().__init__()

    def mover(self):
        self.x += 1
        self.senal_mover.emit(self.id, self.x, self.y)
        if self.x >= (p.ANCHO_GRILLA - 2):
            self.x -= 1
            # se mueve a la izquierda
        # si choca cn algo IMPENETRABLE cambia dirección, falta eso !
        # impenetrable != inamovible


class Bloques(QObject):
    identificador = 0

    def __init__(self, x: int, y: int):
        super().__init__()
        self.id = Bloques.identificador
        Bloques.identificador += 1
        self.x = x
        self.y = y


class Pared(Bloques):
    # inamovible e impenetrable 
    def __init__(self):
        super().__init__()
    # ni luigi ni los fantasmas pueden atravesar o mover el bloque
    # y solo puede haber un MAXIMO_PARED en el mapa


class Roca(Bloques):
    # solo impenetrable: fantasmas cambian dirección si lo chocan
    # si luigi lo choca desde el lado derecho, la roca se mueve 1 a la derecha
    # solo si esa casilla al lao no ta ocupada. si ta ocupa no semueve
    def __init__(self, senal_mover: pyqtSignal):
        self.senal_mover = senal_mover

    def mover(self):
        # primero hacer que no choque cn las paredes
        if self.x >= (p.ANCHO_GRILLA - 2):
            self.x = (p.ANCHO_GRILLA - 2) 
        if self.y >= (p.LARGO_GRILLA - 2):
            self.y = (p.LARGO_GRILLA - 2)
        return None


class Fuego(Bloques):
    # daño e inamovible 
    def __init__(self):
        super().__init__()
    # si luigi lo toca: pierde vida (o muere si no le kedan mas vidas)
    # si le kedan vidas se reinicia el nivel sin mover el bloque
    # si un fantasma lo toca: desaparece/muere en el juego






















# ####clase del juego##########
class JuegoConstructor(QObject):
    senal_validar_login = pyqtSignal()
    senal_empezar = pyqtSignal()
    senal_mover_fantasmas = pyqtSignal(int, int)
    senal_fin_luigi = pyqtSignal(bool)
    senal_mov_luigi = pyqtSignal(bool)  # bool pq es la señal del zapping
    senal_actualizar_vida = pyqtSignal(str)  # o int, aún no estoi segura
    senal_respuesta = pyqtSignal(bool)
    senal_timer_juego = pyqtSignal()
    senal_ventana_constructor = pyqtSignal()
    senal_ventana_mapa = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # inicializo luigi modo constructor cn sus coord iniciales, es decir
        # las de su botón
        self.luigi = Luigi(10, 40, self.senal_fin_luigi, self.senal_mov_luigi)

        # no distingo entre vertical y horizontal pq ¿
        self.fantasmas = []
        self.timer_fantasmas = QTimer(self)
        # self.timer_fantasmas.timeout.connect(self.timer_movimiento)

        # self.senal_fin_luigi.connect(self.choque)

    def comprobar_usuario(self, usuario, mapa):
        result = True
        if not usuario.isalnum():
            result = False
        else:
            if len(usuario) <= p.MIN_CARACTERES or len(usuario) >= p.MAX_CARACTERES:
                result = False
            else:
                if mapa == "crear mapa":
                    self.senal_ventana_constructor.emit()
                else:
                    if mapa == "mapa 1":
                        ruta = "./mapas/fantasma muere.txt"
                    elif mapa == "mapa 2":
                        ruta = "./mapas/mapa enunciado.txt"
                    elif mapa == "mapa 3":
                        ruta = "./mapas/mapa facil.txt"
                    else:
                        ruta = "./mapas/roca salva fantasma.txt"
                    self.senal_ventana_mapa.emit(ruta)
        self.senal_respuesta.emit(result)

    def modo_constructor(self):
        self.luigi._vidas = p.CANTIDAD_VIDAS
        self.senal_empezar.emit()
        self.timer_fantasmas.start()
