# IMPORTANTE
estuve probando mi código y eventualmente se abre y se ejecutan las ventanas (no necesariamente en el momento correcto), pero resulta que en mi computador luego de ejecutar el cliente, se quedaba pegado en la consola. Tuve que aprender a que se ejecutara, ver las ventanas y cerrar de inmediato la ventana de consola porque sino tenía que reiniciar mi computador. Honestamente no sé por qué pasa eso, pero probé en el computador de mi papá y le pasaba lo mismo. Luego de ejecutar main.py de la carpeta cliente se quedó pegado y el computador de mi papá es de este año:( Pongo esto al inicio de todo porque no me gustaría dejar pegado el computador de la persona que me tenga que revisar la tarea y la verdad no sé qué cosa de mi código podría generar algo así. Lo siento mucho U______u

# Tarea 3: DCCachos 🎲


hola:] ns si siempre revisa la misma persona, pero quería decir que antes [T1 y T2] no usé lo de los emojis porque parece que estaba ocupando otro README :( 
lo siento mxo U__________u

## Consideraciones generales :octocat:

No hay implementación de ninguna regla del juego como tal, pero sí hay correcto uso de la conexión cliente-servidor considerando una interfaz gráfica del cliente.


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Networking: 18 pts (16%)
##### ✅ Protocolo
##### ✅ Correcto uso de sockets
##### ✅ Conexión
##### 🟠 Manejo de Clientes
* todos deben ingresar el mismo número de puerto que se le asignó al Servidor al ser ejecutado en main.py. Si la primera vez que se ejecuta main.py del servidor se da como puerto 12345, entonces para cada cliente se ejecuta "py main.py 12345"
* tampoco funcionan de manera correcta los avisos de "sala llena" o "partida en juego"
* solo se aceptan 4 jugadores y en el quinto, el cliente tira un error y no se puede ejecutar. El servidor tira un error, pero no se cae
##### ✅ Desconexión Repentina
#### Arquitectura Cliente - Servidor: 18 pts (16%)
##### ✅ Roles
##### 🟠 Consistencia
* no utilicé locks
##### ✅ Logs
#### Manejo de Bytes: 26 pts (22%)
##### ✅ Codificación
##### ✅ Decodificación
##### ✅ Encriptación
##### ✅ Desencriptación
##### ✅ Integración
#### Interfaz Gráfica: 22 pts (19%)
##### 🟠 Ventana de Inicio
* creo que sí se asigna nombre a los jugadores, pero esto no pude probarlo bien debido a que mi computador se pegaba ***
##### 🟠 Ventana de juego
* está hecha para sólo 1 jugador y los botones no hacen mucho
#### Reglas de DCCachos: 22 pts (19%)
##### ❌ Inicio del juego
##### ❌ Bots
##### ❌ Ronda
##### ❌ Termino del juego
#### Archivos: 10 pts (9%)
##### ✅ Parámetros (JSON)
##### ✅ main.py
##### ✅ Cripto.py
* en cripto.py no usé N_PONDERADOR como una constante de parametros.json, pero funciona bien. Para lo demás, N se obtiene de N_PONDERADOR definido como entero en parametros.json
#### Bonus: 4 décimas máximo
##### ❌ Cheatcodes
##### ❌ Turno con tiempo

*** me gustaría aclarar que mi computador se empezó a quedar pegado literalmente el día de hoy (viernes) y por eso no hablé con nadie porque ya es el plazo máximo de entrega :(
    Además de que es muy probable que sea error de mi código :(

## Ejecución :computer:
Hay dos módulos principales a ejecutar en la tarea que son ```main.py``` tanto del servidor como del cliente.
En ambos al ejecutar se debe poner el puerto como argumento en la consola (cmd)
```
python/py/python3 main.py PUERTO
```
siento PUERTO una combinación de cuatro-cinco números, al ejecutar mi tarea normalmente usaba 12345 ó 5050. 

Además se debe contar con los siguientes archivos y directorios adicionales:
1. `backend.py` y `frontend.py` en la carpeta cliente
2. Una carpeta Scripts que contiene a `cripto.py` dentro de la carpeta cliente y dentro de la carpeta servidor
3. Una carpeta Sprites que contiene todas las fotos necesarias en formato .png dentro de la carpeta cliente
4. Un archivo `jason.py` dentro de la carpeta cliente y servidor, que sirve para leer el archivo parametros.json
5. Un archivo `parametros.json` con la información descrita en el enunciado
6. Un archivo `validar.py` dentro de la carpeta servidor, que sirve únicamente para validar los resultados enviados por los jugadores. Por ejemplo, que efectivamente sean números y que no pueden sumar menos de 2 o más de 12 porque es imposible. 
6. `cliente.py` dentro de la carpeta cliente

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```socket```: todas las funciones vistas en clases
2. ```PyQt5```: todas las funciones vistas en clases
3. ```json```: todas las funciones vistas en clases
4. ```threading```: módulo ```Thread```
5. ```collections```: módulo ```deque```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```backend```: Contiene a ```Backend```.

2. ``cliente``: Contiene a ``Cliente``.

3. ```server```: Contiene a ``Servidor``.

4. ``jason``: Hecha para guardar los parámetros descritos en el archivo parametros.json

5. ``cripto``: Contiene las funciones ``encriptar`` y ``desencriptar`` muy utilizadas para el envío de información mediante servidor y cliente.

6. ``frontend``: Contiene a las ventanas necesarias para el juego


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Que siempre se conectan 4 jugadores porque no hice la implementación de los bots :(
2. Que todos se conectan al mismo puerto que se le asignó al servidor al ser creado
3. Que el valor N_PONDERADOR será siempre 1 como se plantea en el archivo ``cripto.py`` al definir "N = 1" para testear. Por lo mismo, se define como un entero igual a 1 en parametros.json
4. Que el puerto se entrega mediante consola al ejecutar main.py tanto del servidor como del cliente. Ejemplo:

```
py main.py 5050
```

PD: Por alguna razón al importar cripto.py en backend.py y en server.py no me dejaba simplemente esto en VSCode: 
```
from Scripts import cripto
```
Eso no funcionaba, ni siquiera reconocía las funciones dentro de cripto. Luego utilicé:
```
from .Scripts import cripto
```
En ese caso funcionaba que me reconocía las funciones y todo en VSCode, pero en consola me tiraba error. Por lo tanto lo dejé para que funcionara en consola [primer caso] y no en Visual porque sino no se ejecutaba nada del código :( Sé que la Integración se revisa por código, pero si no hacía esto no me podrían revisar la interfaz gráfica y otras cosas :(
necesito 4.42 para aprobar así que necesitaba priorizar cualquier cosa que ya tuviera medianamente en funcionamiento TT


PD 2: en el gitignore usé todas las formas que encontré en internet para ignorar carpetas :D

PD 3: agregué flake8 a mi visual, pero resulta que no sigue estrictamente pep8 porque el máximo de caracteres por línea es 79 [creo] y no supe cambiarlo. debido a esto, para que no me tirara errores de formato y poder centrarme en los errores para la ejecución, cambié algunas imágenes de nombre [background_inicio y background_juego, que se convirtieron en inicio y juego simplemente]. no sé si es válido hacerlo :(

-------


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://www.youtube.com/watch?v=3QiPPX-KeSc>: para tener distintos ejemplos de la estructura cliente-servidor. Este código es base de mi estructura de cliente y de servidor por lo que se encuentra en bastantes líneas.
