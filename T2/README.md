# Tarea 2: DCCazafantasmas 👻🧱🔥

Quiero partir el readme mencionando que todos mis códigos se basaron
en experiencias y ayudantías del ramo, pero no sabía si debía citar
porque una vez en una issue leí que si usábamos, por ejemplo, código de la sala de ayuda, no había que citarlo :(
no recuerdo la issue específica pero era de la tarea 0, espero que esto no cause mayor problema U___u

Por otro lado, para que el movimiento de las imágenes fuese continuo, separé la carpeta Personajes en 7 carpetas distintas D: donde cada una corresponde a una dirección tanto de un fantasma o de Luigi (de esta forma fue cómo lo vimos en la sala de ayuda mediante el método zapping)

Además, los comandos que no están en los contenidos los saqué principalmente de la página oficial de PyQt5 donde enseñaban brevemente cómo usarlos y cómo funcionaban sus parámetros, por lo mismo, no vi necesidad en citar cada comando (por ejemplo el que agrega una foto al botón) porque tendría que haber citado, en ese caso, cada comando para la grilla al ser un QFrame :( 

En el modo de los mapas pre hechos, no pude lograr ponerle borde a la grilla porque tuve que crear un código distinto al que había hecho para el front_end del modo constructor y tuve problemas con las señales así que sólo se abre el mapa "mapa enunciado.txt" entregado en la carpeta "mapas"

Finalmente me gustaría mencionar que el juego evidentemente no funciona porque no logré implementar lo necesario para que se moviera, pero sí abre las ventanas específicas en caso de que se deba leer un mapa o si se debe abrir el modo constructor. Funciona el timer de cuenta regresiva hasta que sea 0. Se revisa correctamente si el username ingresado es inválido o no. Se conectan algunas señales. 

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```front_end.py``` en la misma carpeta en que esté ```main.py```
2. ```back_end.py``` en la misma carpeta en que esté ```main.py```
3. ```mapas_hechos.py``` en la misma carpeta en que esté ```main.py```
4. las carpetas: mapas, sounds y sprites en la misma carpeta en que esté ```main.py```
5. Además, sprites tiene que divirse en las siguientes carpetas: Elementos, Fondos y Personajes.
6. Adicionalmente, la carpeta Personajes se divide en 7 carpetas mencionadas al inicio del README

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: Utilicé practicamente todas sus funciones vistas e incluso algunas que no vimos directamente

2. ```sys```: Utilicé el módulo ``os``


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```front_end```: Contiene a las clases ```VEntanaInicio```, ```VentajaJuego``` y ```Grilla``` 
2. ```back_end```: Contiene a las clases ``Luigi``, ``Fantasmas``, ``FantasmaVertical``, ``FantasmaHorizontal``, ``Bloques``, ``Pared``, ``Roca``, ``Fuego`` y ```JuegoConstructor```
3. ``mapas_hechos``: Contiene a la clase ``VentanaJuegoMapas``
4. ```parametros```: Contiene todos los parámetros fijos que se utilizaron en la tarea, tales como cantidad de fantasmas, tiempo, cantidad de vidas, etc.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Que cada vez que se apriete un botón en el modo constructor, entonces se presionará únicamente la grilla y no cualquier otro lugar de la pantalla. Es decir, no se puede presionar el botón y no presionar luego la ventana en la parte de la grilla para que funcione correctamente el contador del botón


-------



## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://doc.qt.io/qtforpython-5/contents.html>: la información proporcionada por este link se presenta en básicamente todas las líneas de la tarea ya que explica principalmente cómo utilizar los comandos de la librería PyQt5, por lo mismo, no citaré cada línea en que se usó porque no es código literal, sino sólo ejemplos que se dan para explicar cómo funciona el comando y/o los atributos que recibe.
2. Ayudantías 4 y 6, Experiencias 3, 4 y 5 (la última es Sala de Ayuda para la tarea). Tenía entendido que no es necesario citar sobre el material que está en el Syllabus del curso, por lo que no están especificadas dentro del código :(


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
