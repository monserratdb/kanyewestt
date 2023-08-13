import sys
from server import Servidor
from jason import data


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("dar puerto como argumento :]")
        sys.exit(1)

    port = int(sys.argv[1])
    host = data("HOST")

    # instanciamos server
    servidor = Servidor(host, port)
    try:
        # inicia
        servidor.comienza()
    except KeyboardInterrupt:
        # parar cn Ctrl+C ¿
        servidor.fin()
