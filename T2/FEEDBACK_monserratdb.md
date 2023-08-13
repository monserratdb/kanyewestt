# FEEDBACK T2

**Repositorio de _monserratdb_**

## Resumen

| Puntaje Máximo | Puntaje Obtenido | Décimas Bonus | Décimas Descuento | Nota final |
| -------------- | ---------------- | ------------- | ----------------- | ---------- |
| 100            |  33              | 0,0            | 1,0                | **2.9**     |

## Comentario general 

Hola monserratdb! Lamentablemente te faltó implementar muchos aspectos de la tarea. La verdad es que ibas por muy buen camino, todo lo que tienes implementado se ve en orden y se nota que manejas la materia evaluada, pero al faltar mucho por implementar la nota baja drasticamente. Recuerda que si necesitas ayuda puedes contar con el equipo de ayudantes de bienestar del curso. Mucho éxito con lo que queda de semestre!



### Puntaje por sección

#### **Ventanas (27 pts)**

1. Ventana inicio: La ventana de inicio se visualiza correctamente. Se visualizan los elementos mínimos y estos no se superponen entre sí.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

Bien

--------------


2. Ventana inicio: Se verifica que el nombre sea alfanumérico, esté en el rango de caracteres y que no sea vacío. En caso contrario, se debe notificar el error mediante un mensaje o pop-up.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 3               |

Bien

--------------


3. Ventana inicio: Se puede seleccionar cualquier mapa de la carpeta "Mapa" o bien indicar que no se quiere cargar uno predefinido. Luego se ingresar a la Ventana de Juego.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

Bien

--------------


4. Ventana inicio: El botón de salir cierra la ventana y termina el programa.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 1              | 0               |

No implementado

--------------


5. Ventana juego: Se visualiza correctamente el mapa del juego y todos los elementos mínimos requeridos.
Los elementos no se superponen entre sí.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 4               |

Bien

--------------


6. Ventana juego: Las estadísticas se actualizan a medida que progresa el juego.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 2               |

Las vidas no se actualizan

--------------


7. Ventana juego: La ventana carga el mapa si se ha seleccionado uno, o comienza en un mapa vacío si está en modo constructor.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

bien!

--------------


8. Ventana juego: El panel de construcción contiene todas las entidades que se pueden poner en el mapa

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

bien!

--------------


9. Ventana juego: El panel de construcción señala cuántos elementos de cada entidad quedan disponibles para poner en el mapa.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

bien!

--------------


10. Ventana juego: El juego inicia cuando el botón para jugar el mapa es presionado.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 4               |

bien!

--------------


11. Ventana juego: El botón de salir cierra la ventana actual y sale del programa.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 1              | 0               |

No implementado

--------------



> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 27             | 23               |


#### **Mecánicas de juego (47 pts)**

1. Luigi: Al detectar la colisión entre Luigi y los Fantasmas o el Fuego, Luigi pierde una vida y vuelve al punto donde inició el nivel.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No implementado

--------------


2. Luigi: Al colisionar con una Pared, Luigi no puede seguir avanzando en esa dirección. Si colisiona con una Roca, debe poder arrastrarla.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 0               |

No implementado

--------------


3. Luigi: Se muestra consistencia con las teclas de movimiento que se presionan, y la dirección hacia donde Luigi avanza.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 2               |

se emite la señal, pero no ocasiona nada

--------------


4. Fantasmas: Cada fantasma se mueve de manera independiente de los demás, respetando su propia velocidad y dirección.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 0               |

No implementado el movimiento

--------------


5. Fantasmas: La velocidad con la cual cada fantasma se mueve se decide de manera aleatoria.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 1              | 1               |

Bien!

--------------


6. Fantasmas: Se implementan correctamente el Fantasma horizontal y el Fantasma vertical, con sus respectivas características.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 6              | 0               |

No se mueve

--------------


7. Fantasmas: Cuando un fantasma colisiona con un Fuego, el fantasma desaparece. Si colisiona con una Pared o Roca, invierte su sentido de dirección y sigue avanzando, respetando su propio movimiento.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 0               |

No se mueve

--------------


8. Modo Constructor: No se puede superponer un bloque en una casilla que ya está ocupada.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No se puede poner nada

--------------


9. Modo Constructor: El panel de construcción tiene un máximo de elementos por entidad que se pueden poner en el mapa.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 4               |

Bien!

--------------


10. Modo Constructor: Ninguna sprite tiene movimiento al no haber iniciado el juego.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No se puede poner nada por lo que no hay nada que mover

--------------


11. Modo Constructor: Al apretar el botón de Jugar, se verifica que exista un sólo Luigi y una sóla Estrella en el mapa. Si se cumple, el modo constructor queda deshabilitado, impidiendo la modificación del mapa, y el juego comienza junto a la cuenta regresiva.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 6              | 0               |

No implementado

--------------


12. Fin de ronda: Se calculan correctamente el puntaje al terminar la ronda.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No implementado

--------------


13. Fin de ronda: Se implementan las tres formas de terminar la ronda: cuando Luigi se queda sin vidas, cuando libera a Aossa de la Estrella, o cuando la cuenta regresiva llega a cero.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 0               |

no implementado

--------------


14. Fin de ronda: En caso de victoria o derrota, se notifica al usuario indicando el resultado, nombre del usuario y puntaje. Además suena el sonido correspondiente del caso.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No implementado

--------------


15. Fin de ronda: Aparece el botón de salir automáticamente al acabar el juego. Este botón termina el programa.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No implementado

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 47             | 7               |

#### **Interacción con el usuario (14 pts)**

1. Clicks: El modo constructor es implementado completamente y correctamente con el click izquierdo.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 8              | 0               |

No implementado

--------------


2. Animaciones: El movimiento de los personajes en el mapa es fluído y animado, según las sprites correspondientes.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 6              | 0               |

No implementado

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 14              | 0               |

#### **Funcionalidades con el teclado (8 pts)**

1. Pausa: Está implementado el botón Pausa y la letra P, al seleccionarlo se detienen todas las animaciones. Además, se deshabilita el movimiento de Luigi.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 0               |

No implementado

--------------


2.  K + I + L: Al escribir esta combinación de letras en orden o al mismo tiempo, elimina a todos los Fantasmas en el mapa.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No implementado

--------------


3. I + N + F: Al escribir esta combinación de letras en orden o al mismo tiempo, Luigi tiene vidas y tiempo infinito para completar el nivel.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No implementado

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 8             | 0               |


#### **Archivos (14 pts)**

1. Sprites: Trabaja correctamente con todos los archivos entregados.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 1               |

No se usan todos los sprites

--------------


2. Parametros.py: Utiliza e importa correctamente parametros.py.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

Bien!

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4             | 3               |

#### Bonus (8 **decimas**)

1. Volver a Jugar: Cumple con todos los requisitos de este bonus.

| Décimas Máximas | Décimas Obtenidas |
| --------------- | ----------------- |
| 2               | 0                |

No implementado

--------------


2. Follower villain: Cumple con todos los requisitos de este bonus.

| Décimas Máximas | Décimas Obtenidas |
| --------------- | ----------------- |
| 3               | 0                |

No implementado

--------------


3. Drag and Drop: Cumple con todos los requisitos de este bonus.

| Décimas Máximas | Décimas Obtenidas |
| --------------- | ----------------- |
| 3               | 0                |

No implementado

--------------


> **Resumen décimas**

| Décimas Máximas | Décimas Obtenidas |
| --------------- | ----------------- |
| 8              | 0                |


#### **Descuentos generales (34 décimas)**

#####  Descuentos generales (máximo 10 décimas)

1. Se descuenta hasta 5 décimas si el README no indica archivos los archivos necesarios para ejecutar la tarea ni información relevante para la corrección.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 5                | 1                 |

Favor usar los emoticones para explicar cada parte en detalle que se implementó o no

--------------


2. Se descuentan hasta 4 décimas por no respetar PEP8

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 4                | 0                 |



--------------


3. Se descuentan hasta 5 décimas si no se sigue el formato de entrega.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 5                | 0                 |



--------------


4. Se descuenta 5 décimas si uno o más archivos excede las 400 líneas de código.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 5                | 0                 |



--------------


5.  Se descuentan hasta 5 décimas por no usar correctamente el `.gitignore`.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 5                | 0                 |



--------------


6. Se descuentan 1-5 décimas por cambio de líneas.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 5                | 0                 |



--------------


##### Descuentos por utilizar alguna librería o Built-in no autorizado (5 décimas)

1. Se descuentan 1- 5 décimas por utilizar alguna librería o Built-in no autorizado. Tal como dice en cada enunciado de tarea, no se permite ninguna librería a no ser que nosotros especifiquemos lo contrario.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 5                | 0                 |



--------------


> **Resumen Descuento**

| Descuento máximo | Descuento Obtenido | Descuento Aplicados |
| ---------------- | ------------------ | ------------------- |
| 34               | 1                 | 1                  |
