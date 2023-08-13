import sys
import os
from os.path import join
import typing
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QMainWindow, QComboBox, QPushButton, \
QVBoxLayout, QHBoxLayout, QApplication, QGridLayout, QFrame
from PyQt5.QtGui import QPixmap, QFont, QMouseEvent, QKeyEvent
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
import parametros as p

#parto haciendo la grilla para luego agregarla a la Ventana de Juego
class Grilla(QFrame):

    def __init__(self):
        super().__init__()
        self.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        self.grilla = QGridLayout(self)
        self.grilla.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

        self.crear()

    def crear(self):
        for fila in range(16):
            for columna in range(11):
                label = QLabel(self)
                label.setFixedSize(25, 25)
                #label.setAlignment(Qt.AlingCenter)
                if fila == 0 or columna == 0 or fila == 15 or columna == 10:
                    pixmap = QPixmap("./sprites/Elementos/bordermap.png")
                    label.setPixmap(pixmap.scaled(25, 25, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
                else:
                    label.setStyleSheet("background-color: black; border: 1px solid white")
                
                self.grilla.addWidget(label, fila, columna)

class VentanaJuego(QMainWindow):
    senal_click_pantalla = pyqtSignal(int, int) #dónde clickea el mouse
    senal_zapping = pyqtSignal(bool) #para mover luigi cn teclas

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("ventana juego")
        self.setMouseTracking(True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        #creamos el layout y agregamos todo
        layout = QVBoxLayout()
        self.central = QWidget()
        self.central.setLayout(layout)
        self.setCentralWidget(self.central)

        #modo constructor cn sus botones
        self.selector = QComboBox(self.central)
        self.selector.addItems(["todos", "bloques", "entidades"])
        self.selector.setGeometry(410, 10, 100, 30)

        #botón que envia información seleccionada por el QComboBox
        self.muestra = QPushButton("enviar", self.central)
        self.muestra.setGeometry(520, 10, 50, 30)

        #botón luigi
        max_luigi = int(p.LUIGI)
        self.luigi = QPushButton(f"({max_luigi})", self.central)
        self.luigi.setGeometry(410, 40, 100, 30)
        self.luigi.setIcon(QtGui.QIcon("./sprites/Personajes/luigi_front.png"))
        self.luigi.setIconSize(QtCore.QSize(25, 25))
        self.luigi.clicked.connect(lambda: self.boton_clickeado(max_luigi, self.luigi))

        #botón pared
        pared = int(p.MAXIMO_PARED)
        self.pared = QPushButton(f" ({p.MAXIMO_PARED})", self.central)
        self.pared.setGeometry(410, 80, 100, 30)
        self.pared.setIcon(QtGui.QIcon("./sprites/Elementos/wall.png"))
        self.pared.setIconSize(QtCore.QSize(25, 25))
        self.pared.clicked.connect(lambda: self.boton_clickeado(pared, self.pared))

        #boton roca
        roca = int(p.MAXIMO_ROCA)
        self.roca = QPushButton(f" ({p.MAXIMO_ROCA})", self.central)
        self.roca.setGeometry(410, 120, 100, 30)
        self.roca.setIcon(QtGui.QIcon("./sprites/Elementos/rock.png"))
        self.roca.setIconSize(QtCore.QSize(25, 25))
        self.roca.clicked.connect(lambda: self.boton_clickeado(roca, self.roca))

        #boton estrella
        star = int(p.ESTRELLA)
        self.estrella = QPushButton(f" ({p.ESTRELLA})", self.central)
        self.estrella.setGeometry(410, 160, 100, 30)
        self.estrella.setIcon(QtGui.QIcon("./sprites/Elementos/osstar.png"))
        self.estrella.setIconSize(QtCore.QSize(25, 25))
        self.estrella.clicked.connect(lambda: self.boton_clickeado(star, self.estrella))

        #botón fantasma horizontal
        hor = int(p.MAXIMO_HORIZONTAL)
        self.horizontal = QPushButton(f" ({p.MAXIMO_HORIZONTAL})", self.central)
        self.horizontal.setGeometry(410, 200, 100, 30)
        self.horizontal.setIcon(QtGui.QIcon("./sprites/Personajes/white_ghost_rigth_1.png"))
        self.horizontal.setIconSize(QtCore.QSize(25, 25))
        self.horizontal.clicked.connect(lambda: self.boton_clickeado(hor, self.horizontal))

        #botón fantasma vertical
        ver = int(p.MAXIMO_VERTICAL)
        self.vertical = QPushButton(f" ({p.MAXIMO_VERTICAL})", self.central)
        self.vertical.setGeometry(410, 240, 100, 30)
        self.vertical.setIcon(QtGui.QIcon("./sprites/Personajes/red_ghost_vertical_1.png"))
        self.vertical.setIconSize(QtCore.QSize(25, 25))
        self.vertical.clicked.connect(lambda: self.boton_clickeado(ver, self.vertical))

        #botón fuego
        fuego = int(p.MAXIMO_FUEGO)
        fuegoi = QPixmap("./sprites/Elementos/fire.png")
        self.fuego = QPushButton(f" ({p.MAXIMO_FUEGO})", self.central)
        self.fuego.setGeometry(410, 280, 100, 30)
        self.fuego.setIcon(QtGui.QIcon("./sprites/Elementos/fire.png"))
        self.fuego.setIconSize(QtCore.QSize(25, 25))
        self.fuego.clicked.connect(lambda: self.boton_clickeado(fuego, self.fuego))
        self.fuego.clicked.connect(lambda: self.cambiar_imagen(fuegoi))

        #botón "jugar"
        self.jugar = QPushButton("jugar", self.central)
        self.jugar.setGeometry(410, 500, 50, 30)
        self.jugar.clicked.connect(self.empieza_tiempo)

        #botón "limpiar"
        self.limpiar = QPushButton("limpiar", self.central)
        self.limpiar.setGeometry(470, 500, 50, 30)

        ############# cuando está en modo juego ###############
        #label vida
        self.vida = QLabel(f"Vidas: {p.CANTIDAD_VIDAS}", self)
        self.vida.setFont(QFont("Arial", 10))
        self.vida.setGeometry(410, 320, 100, 30)
        self.vida.setStyleSheet("color: black")

        #label tiempo
        self.tiempo = QLabel(f"Tiempo: {p.TIEMPO_CUENTA_REGRESIVA}", self)
        #45 segundos
        self.tiempo.setFont(QFont("Arial", 10))
        self.tiempo.setGeometry(410, 360, 100, 30)
        self.tiempo.setStyleSheet("color: black")
        self.timer = QTimer()
        self.timer.timeout.connect(self.cambia_tiempo)

        #botón pausar
        self.pausa = QPushButton("pausar", self.central)
        self.pausa.setGeometry(410, 400, 100, 30)
        self.pausa.setEnabled(False)
        self.pausa.clicked.connect(self.pausar)

        self.grilla = Grilla()
        self.grilla.setFixedSize(300, 400)
        layout.addWidget(self.grilla)

    def boton_clickeado(self, maximo: int, boton: QPushButton):
        if maximo > 0:
            maximo -= 1
            boton.setText(f"({maximo})")

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            self.senal_click_pantalla.emit(x, y)
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        x = event.pos().x()
        y = event.pos().y()

    # Agregar un botón para cambiar la imagen al hacer clic en una celda
    def cambiar_imagen(self, imagen: QPixmap):
        
        return None

    def empieza_tiempo(self):
        inicial = int(self.tiempo.text().split(":")[1])
        self.tiempo.setText(f"Tiempo: {inicial}")
        self.timer.start(1000) #actualiza cada un segundo
        self.jugar.setEnabled(False)
        self.limpiar.setEnabled(False)
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

    def mostrar(self):
        self.show()

#### clase ventana inicio ###
class VentanaInicio(QWidget):
    senal_usuario = pyqtSignal(str, str)
    senal_mapas_hechos = pyqtSignal(str)
    senal_constructor = pyqtSignal()
    senal_abrir = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(50, 30, 590, 680)
        self.setWindowTitle("ventana inicio")

        #Qlabel para el fondo
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("./sprites/Fondos/fondo_inicio.png"))

        #Qlabel para el logo
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap("./sprites/Elementos/logo.png"))
        self.logo.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.logo.setGeometry(30, 200, 520, 100)

        #Qlabel para el texto
        self.texto = QLabel("ingrese username:", self) 
        self.texto.setGeometry(10, 500, 90, 30)  
        self.texto.setStyleSheet("color: white")    

        #Qlabel para input usuario
        self.input = QLineEdit("", self)
        self.input.setGeometry(100, 505, 190, 20)      

        #Selector de mapas hechos o sin mapa hecho
        self.selector = QComboBox(self)
        self.selector.addItems(["crear mapa", "mapa 1", "mapa 2", "mapa 3", "mapa 4"])
        self.selector.setGeometry(10, 535, 280, 20)      

        #botón para "ingresar"
        self.boton = QPushButton("ingresar", self)
        self.boton.setGeometry(10, 560, 280, 25)      
        #conectamos 
        self.boton.clicked.connect(self.login)
        #primero sólo pruebo si es q el usuario es incorrecto
        #y envío la opción elegida por el selector

        #creo layout y agrego todo
        layout = QVBoxLayout()
        layout.addWidget(self.background)
        layout.addWidget(self.logo)
        layout.addWidget(self.texto)
        layout.addWidget(self.input)
        layout.addWidget(self.selector)
        layout.addWidget(self.boton)

    def login(self):
        usuario = self.input.text()
        opcion = self.selector.currentText()
        self.senal_usuario.emit(usuario, opcion)
    
    def validacion(self, result):
        if result:
            print(result)
            self.hide()
            self.senal_abrir.emit()
        else:
            self.input.setText("")
            self.input.setPlaceholderText("username inválido")

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.enviar_info_selector


    def mostrar(self):
        self.show()
    