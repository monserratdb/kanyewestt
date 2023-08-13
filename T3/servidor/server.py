import socket
from threading import Thread
import json
from Scripts import cripto
from validar import Logica
import random
from jason import data


class Servidor:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_server = None
        self.clientes = {}
        self.j1 = False
        self.j2 = False
        self.j3 = False
        self.j4 = False
        self.j1_nombre = None
        self.j2_nombre = None
        self.j3_nombre = None
        self.j4_nombre = None
        self.jugando = False
        self.listos = {1: False, 2: False, 3: False, 4: False}
        self.validar = Logica()

    def comienza(self):
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"server escuchando en {self.host}: {self.port}")

        try:
            while True:
                thread = Thread(target=self.acepta_clientes, daemon=True)
                thread.start()
        except KeyboardInterrupt:
            self.fin()

    def log(self, mensaje: str):
        print(mensaje.center(80, ' '))

    def fin(self):
        if self.socket_server:
            self.socket_server.close()
            print("Servidor cerrado")

    def acepta_clientes(self):
        while True:
            jugador = 0
            try:
                socket_cliente, addr = self.socket_server.accept()
                print(f"conexión aceptada desde {addr[0]}:{addr[1]}")

                if not self.j1:
                    jugador = 1
                    self.j1 = True
                elif not self.j2:
                    jugador = 2
                    self.j2 = True
                elif not self.j3:
                    jugador = 3
                    self.j3 = True
                elif not self.j4:
                    jugador = 4
                    self.j4 = True

                if jugador != 0:
                    thread = Thread(target=self.escuchar_cliente,
                                    args=(jugador, socket_cliente),
                                    daemon=True)
                    thread.start()
                    self.clientes[jugador] = socket_cliente
                else:
                    data = {"acción": "sala llena"}
                    self.enviar_mensaje(socket_cliente, data)
                    self.log("un jugador quería entrar, pero" +
                             "la sala estaba llena")

            except ConnectionError:
                print("error")

    def escuchar_cliente(self, id_cliente, socket_cliente: socket):
        self.log(f"escuchando a jugador {id_cliente}")
        try:
            while True:

                mensaje = self.recibir_mensaje(socket_cliente)

                if not mensaje:
                    raise ConnectionError

                respuesta = self.validar.procesar(mensaje)
                if respuesta:
                    self.enviar(socket_cliente, respuesta)
                if respuesta["acción"] == "comenzar":
                    self.listos[id_cliente] = True
                    aleatorio = random.randint(0, 3)
                    nombres_disponibles = data("NOMBRES_DISPONIBLES")
                    nombre = nombres_disponibles[aleatorio]
                    dic = {"acción": "nombre asignado", "nombre": nombre}
                    self.enviar(socket_cliente, dic)
                    if id_cliente == 1:
                        self.j1_nombre = nombre
                    elif id_cliente == 2:
                        self.j2_nombre = nombre
                    elif id_cliente == 3:
                        self.j3_nombre = nombre
                    else:
                        self.j4_nombre = nombre

                if self.listos[1] and self.listos[2] and self.listos[3] and \
                        self.listos[4] and not self.jugando:
                    self.jugando = True
                    self.log("comenzando la partida con 4 jugadores")
                    mensaje = {"acción": "partida"}
                    self.enviar(socket_cliente, mensaje)
                    self.log("un jugador quería entrar, pero" +
                             "había una partida en juego")

        except ConnectionError:
            print("error de conexión")
            self.log(f"se ha cerrado la conexión con {id_cliente}")
            self.jugando = False

    def enviar(self, socket_cliente, mensaje):
        msj_bytes = self.codificar(mensaje)
        msj_bytes = cripto.encriptar(msj_bytes)
        largo = len(msj_bytes)
        largo_bytes = largo.to_bytes(4, byteorder='little')
        chunks = largo // 128

        if chunks % 32 != 0 and chunks > 0:
            chunks += 1
        msj_enviar = bytearray(b'')

        for chunk in chunks(1, chunks + 1):
            msj_chunk = msj_bytes[(128 * (chunk - 1)):chunk * 128]
            while len(msj_chunk) % 128 != 0:
                msj_chunk += b'\x00'

            msj_enviar += chunk.to_bytes(4, byteorder='big') + msj_chunk

        socket_cliente.send(largo_bytes + msj_enviar)

    def recibir_mensaje(self, socket_cliente: socket):
        largo_bytes = socket_cliente.recv(4)
        largo_msj = int.from_bytes(largo_bytes, byteorder="little")
        msj_bytes = bytearray()

        while len(msj_bytes) < largo_msj:
            # num_bloque = socket_cliente.recv(4)
            recibe_chunk = socket_cliente.recv(128)
            msj_bytes += recibe_chunk

        bytes_sin_cero = msj_bytes.rstrip(b'\x00')
        N = data("N_PONDERADOR")
        bytes_sin_cero = cripto.desencriptar(bytes_sin_cero, N)
        mensaje = self.decodificar(bytes_sin_cero)
        return mensaje

    def codificar(self, mensaje):
        try:
            msj_json = json.dumps(mensaje)
            msj_bytes = msj_json.encode()
            return msj_bytes
        except json.JSONDecodeError:
            self.log("no se pudo codificar el mensaje!")
            return b''

    def decodificar(self, mensaje):
        try:
            msj = json.loads(mensaje)
            return msj
        except json.JSONDecodeError:
            self.log("no se pudo decodificar el mensaje!")

# lo que falta son cosas del juego cmo tal y hacer los logs
