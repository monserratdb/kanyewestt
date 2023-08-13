# ventana de juego pero en modo mapas hechos
from PyQt5.QtWidgets import QWidget, QLabel, QMainWindow, QPushButton, \
    QVBoxLayout, QFrame
from PyQt5.QtGui import QPixmap, QFont, QMouseEvent
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
import parametros as p


class VentanaJuegoMapas(QMainWindow):
    senal_click_pantalla = pyqtSignal(int, int)  # dónde clickea el mouse
    senal_zapping = pyqtSignal(bool)  # para mover luigi cn teclas

    def __init__(self):
        self.alto = 16
        self.ancho = 11
        self.celda = 25
        self.data = []  # guarda los elementos del .txt en una lista
        self.path = "./mapas/mapa enunciado.txt"
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("ventana juego")
        self.setMouseTracking(True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        # creamos el layout y agregamos todo
        layout = QVBoxLayout()
        self.central = QWidget()
        self.central.setLayout(layout)
        self.setCentralWidget(self.central)

        # botón "jugar"
        self.jugar = QPushButton("jugar", self.central)
        self.jugar.setGeometry(410, 500, 50, 30)
        self.jugar.clicked.connect(self.empieza_tiempo)

        # ############ cuando está en modo juego ###############
        # label vida
        self.vida = QLabel(f"Vidas: {p.CANTIDAD_VIDAS}", self)
        self.vida.setFont(QFont("Arial", 10))
        self.vida.setGeometry(410, 320, 100, 30)
        self.vida.setStyleSheet("color: black")

        # label tiempo
        self.tiempo = QLabel(f"Tiempo: {p.TIEMPO_CUENTA_REGRESIVA}", self)
        # 45 segundos
        self.tiempo.setFont(QFont("Arial", 10))
        self.tiempo.setGeometry(410, 360, 100, 30)
        self.tiempo.setStyleSheet("color: black")
        self.timer = QTimer()
        self.timer.timeout.connect(self.cambia_tiempo)

        # botón pausar
        self.pausa = QPushButton("pausar", self.central)
        self.pausa.setGeometry(410, 400, 100, 30)
        self.pausa.setEnabled(False)
        self.pausa.clicked.connect(self.pausar)

        # agrego la grilla que lee de un texto
        self.grilla = QFrame(self)
        self.grilla.setFixedSize(
            self.celda * self.ancho,
            self.celda * self.alto
        )

        self.grilla_data(self.path)
        self.rellena_grilla()
        self.grilla.setGeometry(50, 100, 100, 100)

    def grilla_data(self, path):
        with open(path, "r") as file:
            self.texto_grilla = [list(line.strip()) for line in file]

    def rellena_grilla(self):
        for row in range(len(self.texto_grilla)):
            for col in range(len(self.texto_grilla[row])):
                label = QLabel(self.grilla)
                if self.texto_grilla[row][col] == "P":
                    pixmap = QPixmap("./sprites/Elementos/wall.png")
                elif self.texto_grilla[row][col] == "L":
                    pixmap = QPixmap("./sprites/Personajes/luigi_front.png")
                elif self.texto_grilla[row][col] == "S":
                    pixmap = QPixmap("./sprites/Elementos/osstar.png")
                elif self.texto_grilla[row][col] == "H":
                    ruta_a = "./sprites/Personajes/white_ghost_rigth_1.png"
                    pixmap = QPixmap(ruta_a)
                elif self.texto_grilla[row][col] == "V":
                    ruta_b = "./sprites/Personajes/red_ghost_vertical_1.png"
                    pixmap = QPixmap(ruta_b)
                elif self.texto_grilla[row][col] == "F":
                    pixmap = QPixmap("./sprites/Elementos/fire.png")
                elif self.texto_grilla[row][col] == "R":
                    pixmap = QPixmap("./sprites/Elementos/rock.png")
                elif self.texto_grilla[row][col] == "-":
                    pixmap = QPixmap(self.celda, self.celda)
                    pixmap.fill(Qt.black)
                    label.setStyleSheet("border: 1px solid white;")
                else:
                    continue
                pixmap = pixmap.scaled(self.celda, self.celda)
                label.setPixmap(pixmap)
                label.setFixedSize(self.celda, self.celda)
                label.move(col * self.celda, row * self.celda)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            self.senal_click_pantalla.emit(x, y)

    def empieza_tiempo(self):
        inicial = int(self.tiempo.text().split(":")[1])
        self.tiempo.setText(f"Tiempo: {inicial}")
        self.timer.start(1000)  # actualiza cada un segundo
        self.jugar.setEnabled(False)
        self.pausa.setEnabled(True)

    def cambia_tiempo(self):
        current_time = int(self.tiempo.text().split(":")[1])
        actual = current_time - 1
        self.tiempo.setText(f"Tiempo: {actual}")

        if actual == 0:
            self.timer.stop()
            self.jugar.setEnabled(True)
            self.pausa.setEnabled(False)

    def pausar(self):
        self.timer.stop()
        self.jugar.setEnabled(True)
        self.pausa.setEnabled(False)

    def recibe_path(self, path):
        if path != "":
            self.path += path

    def mostrar(self):
        self.show()
