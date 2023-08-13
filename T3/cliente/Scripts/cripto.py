from collections import deque


def encriptar(msg: bytearray, N: int) -> bytearray:
    encr = bytearray(msg)
    longitud = len(encr)
    N_PONDERADOR = N % longitud
    # mover
    for i in range(longitud):
        encr[(i + N_PONDERADOR) % longitud] = msg[i]
    # intercambiar 
    encr[0], encr[N_PONDERADOR] = encr[N_PONDERADOR], encr[0]

    return encr


def desencriptar(msg: bytearray, N: int) -> bytearray:
    # intercambiar
    msg[0], msg[N] = msg[N], msg[0]
    msg_deque = deque(msg)
    # mover
    msg_deque.rotate(-N)
    # lo convertí en deque sólo para poder usar rotate:(
    msg_desencriptado = bytearray(msg_deque)

    return msg_desencriptado


if __name__ == "__main__":
    # Testear encriptar
    N = 1
    msg_original = bytearray(b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x00\x01\x02\x03\x04\x05')
    msg_esperado = bytearray(b'\x01\x05\x02\x03\x04\x05\x06\x07\x08\x09\x00\x01\x02\x03\x04')
    msg_encriptado = encriptar(msg_original, N)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")

    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado, N)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")