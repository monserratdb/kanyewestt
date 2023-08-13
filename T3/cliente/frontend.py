from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, \
    QWidget, QLineEdit, QMessageBox
from os.path import join
# from jason import data


class VentanaJuego(QMainWindow):
    senal_accion = pyqtSignal(str)
    senal_numero = pyqtSignal(str)
    # estas definiciones son temporales hasta
    # que tenga más avances el juego
    jugador = 2
    num = 12
    n_turno = 3
    anterior = 1

    def __init__(self):
        super().__init__()
        self.init_gui()
        self.anunciar()
        self.pasar()
        self.usar()
        self.cambiar()
        self.dudar()

    def init_gui(self):
        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle("ventana de juego")
        self.setMouseTracking(True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.background = QLabel(self)
        ruta_back = join("Sprites", "background", "juego")
        self.background.setPixmap(QPixmap(ruta_back))
        self.background.setGeometry(0, 0, 900, 600)
        self.background.setScaledContents(True)

        self.j1 = QLabel(self)
        ruta_j1 = join("Sprites", "extra", "user_profile.png")
        self.j1.setPixmap(QPixmap(ruta_j1))
        self.j1.setGeometry(410, 480, 50, 50)
        self.j1.setScaledContents(True)
        self.j1_texto = QLabel("jugador 1", self)
        self.j1_texto.setFont(QFont("Arial", 14))
        self.j1_texto.setGeometry(400, 530, 100, 20)
        self.j1_texto.setStyleSheet("color: black")
        self.j1_dado1 = QLabel(self)
        ruta_dado1 = join("Sprites", "dices", "dice_2.png")
        self.j1_dado1.setPixmap(QPixmap(ruta_dado1))
        self.j1_dado1.setGeometry(410, 425, 30, 30)
        self.j1_dado1.setScaledContents(True)
        self.j1_vidas = QLabel("3")
        self.j1_vidas.setFont(QFont("Arial", 11))
        self.j1_vidas.setGeometry(465, 480, 80, 20)
        self.j1_vidas.setStyleSheet("color: white")

        self.turno = QLabel(f"turno de: {self.jugador}", self)
        self.turno.setFont(QFont("Arial", 12))
        self.turno.setGeometry(400, 3, 90, 20)
        self.turno.setStyleSheet("color: white")

        self.anunciado = QLabel(f"numero mayor anunciado: {self.num}", self)
        self.anunciado.setFont(QFont("Arial", 12))
        self.anunciado.setGeometry(20, 40, 200, 20)
        self.anunciado.setStyleSheet("color: white")

        self.anterior = QLabel(f"turno anterior fue: {self.anterior}", self)
        self.anterior.setFont(QFont("Arial", 12))
        self.anterior.setGeometry(380, 40, 200, 20)
        self.anterior.setStyleSheet("color: white")

        self.numero = QLabel(f"numero de turno: {self.n_turno}", self)
        self.numero.setFont(QFont("Arial", 12))
        self.numero.setGeometry(740, 40, 200, 20)
        self.numero.setStyleSheet("color: white")

        self.anuncia = QPushButton("anunciar valor", self)
        self.anuncia.setGeometry(680, 500, 80, 20)
        self.anuncia.clicked.connect(self.anunciar)

        self.ingresa = QLineEdit("ingresa valor: ", self)
        self.ingresa.setGeometry(770, 500, 90, 20)

        self.pasa = QPushButton("pasar turno", self)
        self.pasa.setGeometry(680, 530, 80, 20)
        self.pasa.clicked.connect(self.pasar)

        self.usa = QPushButton("usar poder", self)
        self.usa.setGeometry(770, 530, 80, 20)
        self.usa.clicked.connect(self.usar)

        self.cambia = QPushButton("cambiar dados", self)
        self.cambia.setGeometry(680, 560, 80, 20)
        self.cambia.clicked.connect(self.cambiar)

        self.duda = QPushButton("dudar", self)
        self.duda.setGeometry(770, 560, 80, 20)
        self.duda.clicked.connect(self.dudar)

    def anunciar(self):
        numero = self.ingresa.text()
        self.senal_accion.emit("anunciar")
        self.senal_numero.emit(numero)

    def pasar(self):
        self.senal_accion.emit("pasar")

    def usar(self):
        self.senal_accion.emit("usar")

    def cambiar(self):
        self.senal_accion.emit("cambiar")

    def dudar(self):
        self.senal_accion.emit("dudar")

    def mostrar(self):
        self.show()


class VentanaInicio(QWidget):
    senal_comienza = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(20, 50, 900, 600)
        self.setWindowTitle("ventana de inicio")
        self.setMouseTracking(True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.background = QLabel(self)
        ruta_back = join("Sprites", "background", "inicio.png")
        self.background.setPixmap(QPixmap(ruta_back))
        self.background.setGeometry(0, 0, 900, 600)
        self.background.setScaledContents(True)

        self.j1 = QLabel(self)
        ruta_j1 = join("Sprites", "extra", "user_profile.png")
        self.j1.setPixmap(QPixmap(ruta_j1))
        self.j1.setGeometry(200, 280, 100, 100)
        self.j1.setScaledContents(True)
        self.j1_texto = QLabel("jugador 1", self)
        self.j1_texto.setFont(QFont("Arial", 17))
        self.j1_texto.setGeometry(200, 350, 100, 100)
        self.j1_texto.setStyleSheet("color: black")

        self.j2 = QLabel(self)
        self.j2.setPixmap(QPixmap(ruta_j1))
        self.j2.setGeometry(390, 280, 100, 100)
        self.j2.setScaledContents(True)
        self.j2_texto = QLabel("jugador 2", self)
        self.j2_texto.setFont(QFont("Arial", 17))
        self.j2_texto.setGeometry(390, 350, 100, 100)
        self.j2_texto.setStyleSheet("color: black")

        self.j3 = QLabel(self)
        self.j3.setPixmap(QPixmap(ruta_j1))
        self.j3.setGeometry(550, 280, 100, 100)
        self.j3.setScaledContents(True)
        self.j3_texto = QLabel("jugador 3", self)
        self.j3_texto.setFont(QFont("Arial", 17))
        self.j3_texto.setGeometry(550, 350, 100, 100)
        self.j3_texto.setStyleSheet("color: black")

        self.j4 = QLabel(self)
        self.j4.setPixmap(QPixmap(ruta_j1))
        self.j4.setGeometry(700, 280, 100, 100)
        self.j4.setScaledContents(True)
        self.j4_texto = QLabel("jugador 4", self)
        self.j4_texto.setFont(QFont("Arial", 17))
        self.j4_texto.setGeometry(700, 350, 100, 100)
        self.j4_texto.setStyleSheet("color: black")

        self.comienza = QPushButton('comenzar', self)
        self.comienza.setGeometry(390, 510, 70, 30)
        self.comienza.clicked.connect(self.comenzar)

        self.sale = QPushButton('salir', self)
        self.sale.setGeometry(390, 560, 70, 30)
        self.sale.clicked.connect(self.close)

        self.texto = QLabel("SALA DE ESPERA", self)
        self.texto.setFont(QFont("Arial", 38))
        self.texto.setGeometry(200, 50, 900, 40)
        self.texto.setStyleSheet("color: black")

    def comenzar(self):
        self.senal_comienza.emit()
        self.hide()


class SalaLlena(QWidget):

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("sala llena")
        QMessageBox.warning(self, "Sala llena", "espere un cupo")

    def mostrar(self):
        self.show()


class Partida(QWidget):

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("partida en juego")

        QMessageBox.warning(self, "Partida en juego", "intente después")

    def mostrar(self):
        self.show()
