# Tarea 1: DCCavaCava 🎒

## Consideraciones generales :octocat:
No implementé las funciones de torneo en el módulo ```main.py``` porque no alcancé a cumplir con todo lo pedido de la clase Torneo. Por lo tanto, para demostrar que el menú sí funciona con sus respectivas opciones, sólo se imprime un string con lo que debiese hacer cada opción, pero no se ejecuta el juego como tal.
No sé si es válido hacerlo, pero para no perder el menú preferí dejarlo así :(

### Cosas implementadas y no implementadas 

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

* Clase Arenas: Hecha completa
* Clase Excavadores: Me faltó hacer el método consumir
* Clase Items: Hecha completa
* Clase Torneo: Tiene muchos errores y uno de los principales por los que no puedo especificar los errores uno por uno es el hecho de que tiene problema de importación circular (me sale un error en la consola que dice lo siguiente: "cannot import name 'nombre' from partially initialized module 'modulo' (most likely due to a circular import)" u_U)

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```archivos.py``` en la misma carpeta en que esté ```main.py``` (T1)
2. ```arenas.py```, ```excavadores.py```, ```items.py``` y ```torneo.py``` en la misma carpeta en que esté ```main.py``` (T1)
3. También se debe contar con cuatro archivos del formato .csv: ```arenas.csv```, ```consumibles.csv```, ```excavadores.csv``` y ```tesoros.csv```
4. ```parametros.py``` en la misma carpeta en que esté ```main.py``` (T1)

* Respecto al punto 2. es más que nada porque separé cada clase en un archivo .py distinto como he mencionado antes


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint()```
2. ```random```: ```random()```
3. ```os```: ```path``` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```arenas.py```, ```excavadores.py```, ```items.py``` y ```torneo.py```: Donde cada uno de los archivos corresponde a una de las entidades que se debían crear para el programa
2. ```archivos.py```: Hecha para leer los archivos en formato .csv otorgados para la realización de la tarea y permite también crear/sobreescribir el archivo "DCCavaCava.txt"
3. ```parametros.py```: Un archivo que contiene todos los parámetros presentados en el enunciado con formato ESTE_FORMATO

## Supuestos y consideraciones adicionales 🤔
Los supuestos que realicé durante la tarea son los siguientes:

1. Que siempre las arenas, excavadores, consumibles y tesoros que están en los archivos con formato .csv se deben instanciar según lo definido en mi programa, es decir, que no podía simplemente usar los elementos de la lista de listas que me generaba cada archivo. Es válido porque de otra forma no tendría sentido trabajar con clases (creo)

PD: El diagrama de clases y su respectiva explicación (en formato .txt) se encuentra dentro de una carpeta adjunta llamada "diagrama de clases" ya que así evitaba tener tantos archivos dispersos en la Tarea y su respectiva carpeta


-------


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://parzibyte.me/blog/2020/11/09/leer-archivo-csv-python: este permite leer un archivo
de formato .csv sin la necesidad de usar la librería csv (que estaba prohibida para la tarea). se implementa
en las líneas de la 8 a la 59 del archivo <archivos.py>

2. https://www.techiedelight.com/es/randomly-select-element-from-list-python/#:~:text=Seleccionar%20aleatoriamente%20elementos%20de%20una%20lista%20de%20Python,Descargar%20Ejecutar%20c%C3%B3digo%20...%202%202.%20Usando%20m%C3%B3dulo: este permite elegir una cantidad
k de elementos aleatorios de una lista. se implementa en la línea 127 en el archivo <archivos.py>

3. https://es.stackoverflow.com/questions/335650/c%C3%B3mo-validar-si-existe-un-archivo-en-python-3: facilita el saber si un archivo existe dentro de una carpeta. se implementa en la línea 22 del archivo <main.py> y en la 169 del archivo <archivos.py>

4. https://www.delftstack.com/es/howto/python/python-overwrite-file/: que permite escribir y sobreescribir un archivo extensión .txt y se implementa en las líneas 158-160 del archivo <archivos.py>
