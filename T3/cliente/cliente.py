from PyQt5.QtCore import QObject, pyqtSignal
import socket
from Scripts import cripto
import json
from jason import data
from threading import Thread
from time import sleep


class Cliente(QObject):
    senal_manejar_mensaje = pyqtSignal(dict)
    senal_cerrar = pyqtSignal()

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.iniciar()

    def iniciar(self):
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.escuchar()
        except ConnectionError:
            print("el servidor no está inicializado")
            self.socket_cliente.close()
            self.conectado = False

    def escuchar(self):
        thread = Thread(target=self.escuchar_servidor, daemon=True)
        thread.start()

    def escuchar_servidor(self):
        try:
            while self.conectado:
                mensaje = self.recibir()
                if mensaje:
                    self.senal_manejar_mensaje.emit(mensaje)
        except ConnectionError:
            print("se desconectó del servidor por error de conexión")
            sleep(4)
            self.senal_cerrar.emit()

    def enviar(self, mensaje):
        # primero encriptar y luego codificar
        mensaje = bytearray(mensaje)
        N = data("N_PONDERADOR")
        msj_bytes = cripto.encriptar(mensaje, N)
        msj_bytes = self.codificar(mensaje)
        largo = len(msj_bytes)
        largo_bytes = largo.to_bytes(4, byteorder="little")
        chunks = largo // 128

        if chunks % 128 != 0 and chunks > 0:
            chunks += 1
        msj_enviar = bytearray(b'')

        for chunk in range(1, chunks + 1):
            msj_bloque = msj_bytes[(128 * (chunk - 1)): chunk * 128]
            while len(msj_bloque) % 128 != 0:
                msj_bloque += b'\x00'

            msj_enviar += chunk.to_bytes(4, byteorder="big") + msj_bloque

        self.socket_cliente.send(largo_bytes + msj_enviar)

    def recibir(self):
        # desencriptar y decodificar
        largo_bytes = self.socket_cliente.recv(4)
        largo_msj = int.from_bytes(largo_bytes, byteorder="little")
        msj_bytes = bytearray()

        while len(msj_bytes) < largo_msj:
            num_bloque = self.socket_cliente.recv(4)
            print("numero bloque:", num_bloque)
            recibe_chunk = self.socket_cliente(128)
            msj_bytes += recibe_chunk

        bytes_sin_cero = msj_bytes.rstrip(b'\x00')
        mensaje = self.decodificar(bytes_sin_cero)
        N = data("N_PONDERADOR")
        mensaje = cripto.desencriptar(mensaje, N)
        return mensaje

    def codificar(self, mensaje):
        try:
            msj_json = json.dumps(mensaje)
            msj_bytes = msj_json.encode()
            return msj_bytes
        except json.JSONDecodeError:
            print("no se pudo codificar el msj")
            return b''

    def decodificar(self, mensaje):
        try:
            mensaje = json.loads(mensaje)
            return mensaje
        except json.JSONDecodeError:
            print("no se pudo decodificar el msj")

    def desconectarse(self):
        self.socket_cliente.close()
        print("conexión terminada")
