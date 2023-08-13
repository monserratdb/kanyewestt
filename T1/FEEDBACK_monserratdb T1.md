# FEEDBACK T1

**Repositorio de _monserratdb_**

## Resumen

| Puntaje Máximo | Puntaje Obtenido | Décimas Avance | Décimas Bonus | Décimas Descuento | Nota final |
| -------------- | ---------------- | -------------- | ------------- | ----------------- | ---------- |
| 120            |  82,5              | 0,0             | 0,0            | 5,0                | **4.63**     |

## Comentario general 

Respecto al código, lo que tenías se veía muy bien, solamente faltó implementar el flujo del programa :(, pero ya tenías todo armado, solo faltaba juntar las piezas. Respecto al pep8, podrías instalar alguna librería como autopep8 y algún linter para vscode para que te avise cuando no estás respetando las normas del pep8. En las instrucciones del curso en alguna parte se menciona esto. Respecto a la modularización, estaba muy buena! Muy bien que hayas separado las clases respectivas en archivos distintos, se facilita la corrección y también te puede ayudar a ti a descubrir potenciales errores. Mucho ánimo!



### Puntaje por sección

#### **Modelación programa (42 pts)**

1. Diagrama: Entrega el diagrama respetando el formato solicitado.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

Bien

--------------


2. Diagrama: El diagrama contiene suficientes clases para modelar las entidades y funcionalidades pedidas. Cada clase contiene atributos y métodos respectivos para modelar el programa.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 4               |

Bien

--------------


3. Diagrama: El diagrama contiene relaciones (agregación, composición y herencia) entre las clases incluídas, y mantiene consistencia de modelación.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 4               |

Bien

--------------


4. Definición de clases, atributos, métodos y properties: El Torneo está bien modelado.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 6              | 6               |

Bien

--------------


5. Definición de clases, atributos, métodos y properties: La Arena está bien modelada.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 6              | 6               |

Bien

--------------


6. Definición de clases, atributos, métodos y properties: Los Excavadores están bien modelados.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 6              | 6               |

Bien, aunque no entendí muy bien porque en la clase Excavador heredaste de las arenas.

--------------


7. Definición de clases, atributos, métodos y properties: Los Ítems están bien modelados.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 6              | 6               |

Bien, aunque recuerda que todos los ítems tienen nombre tipo y descripción, por lo que es una característica común a todos ellos, por lo que lo podrías haber definido en el init de la clase abstracta y así todas las clases de las que heredan de Item, ya tendrían estos atributos.

--------------


8. Relaciones entre clases: Se utilizan clases abstractas cuando corresponde.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 4               |

Bien

--------------


9. Relaciones entre clases: Utiliza consistentemente relaciones de agregación y composición.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 4               |

Bien

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 42             | 42               |


#### **Creación de partidas (11 pts)**

1. Se pueden crear una o más partidas de DCCavaCava.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

Bien

--------------


2. Se instancian los excavadores correctamente, respetando los valores del archivo.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 3               |

Bien

--------------


3. Se instancian las arenas correctamente, respetando los valores del archivo.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 3               |

Bien

--------------


4. Se instancian los tesoros y consumibles correctamente, respetando los valores de los archivos.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 3               |

Bien

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 11             | 11               |

#### **Entidades (22 pts)**

1. Excavador: Está implementada la acción de cavar. Se respeta la fórmula dependiendo de cada tipo de excavador.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 2               |

Está implementado en la parte de torneo, pero no específicamente para cada excavador.

--------------


2. Excavador: Está implementada la acción de descansar. El excavador descansa si su energía llega a 0. El descanso dura la cantidad de días correspondientes a la fórmula.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 3               |

Bien

--------------


3. Excavador: Los excavadores pueden encontrar ítems. La probabilidad cumple con la fórmula establecida y se respeta la probabilidad de encontrar Tesoros y Consumibles. Todo lo anterior utiliza las fórmulas correspondientes al tipo de Arena.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 2               |

Está implementado en el archivo de torneo, pero no considera los distintos tipos de arena

--------------


4. Excavador: Los excavadores pierden energía al momento de cavar. Se respeta la fórmula de pérdida de energía y se modifican las características según el tipo de excavador.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No está implementada la pérdida de energía al momento de cavar

--------------


5. Excavador: Está implementada la acción de utilizar consumibles. Los efectos varían según el tipo de excavador.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 1               |

Está creado el método, pero no se incluye una implementación específica para cada excavador

--------------


6. Arena: La arena posee un nivel de dificultad que se calcula a partir de la fórmula establecida. La dificultad varía según el tipo de Arena.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

Bien

--------------


7. Arena: Se cambian aleatoriamente las características de la Arena magnética al inicio de cada día.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 1               |

Solo se tienen los valores random cuando se crea la clase, pero no se cambia día a día

--------------


8. Torneo: Al simular el día, se calcula correctamente la probabilidad de que ocurra un evento. En caso de que ocurra uno, se aplican los efectos correspondientes.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 1,5               |

Hay una implementación a nivel de código, pero no está funcional cuando se intenta probar con el menú

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 22              | 12,5               |

#### **Menus (31 pts)**

1. Menú de Inicio: Se muestran todas las opciones mínimas pedidas en el menú de inicio.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 1              | 1               |

Bien

--------------


2. Menú de Inicio: Al seleccionar 'Nueva Partida', se inicia una nueva partida.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

Bien

--------------


3. Menú de Inicio: Al seleccionar 'Cargar Partida', se carga la partida con los datos almacenados en el archivo DCCavaCava.txt.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No funcional

--------------


4. Menú Principal: Se muestran todas las opciones mínimas pedidas para el menú principal.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 1              | 1               |

Bien

--------------


5. Simulación día Torneo: Se muestra la cantidad total de metros excavados durante el día y la cantidad cavada por cada excavador.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No funcional

--------------


6. Simulación día Torneo: Se muestran los ítems encontrados y su tipo por cada excavador.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No funcional

--------------


7. Simulación día Torneo: Si ocurre un evento, se muestra el cambio de Arena y su efecto en los excavadores.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No funcional

--------------


8. Simulación día Torneo: Se muestran los excavadores que han agotado su energía y comienzan a descansar.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No funcional

--------------


9. Mostrar estado torneo: Se muestra en pantalla toda la información mínima pedida en el enunciado sobre el torneo y los excavadores.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No funcional

--------------


10. Menú Ítems: Se muestran todos los ítems encontrados, permitiendo seleccionar uno.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No funcional

--------------


11. Menú Ítems: Al seleccionar un ítem y utilizarlo, desaparece de la mochila.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 1              | 0               |

No funcional

--------------


12. Guardar partida: Está implementada la opción de guardar partida. Se informa al usuario si el guardado fue exitoso.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No funcional

--------------


13. Robustez: Todos los menus solicitados poseen la opción de volver al menu anterior y salir del  programa.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 2               |

No se pudo testear con los menús que no están implementados

--------------


14. Robustez: Todos los menús son a prueba de cualquier tipo de input.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 6              | 3               |

No se pudo testear con los menús que no están implementados

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 31             | 9               |


#### **Archivos (14 pts)**

1. Archivos CSV: Los archivos csv utilizados son trabajados correctamente.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 4               |

Bien

--------------


2. Archivos TXT: Se trabaja correctamente con el archivo DCCavaCava.txt. Se lee y escribe correctamente el archivo para cargar y guardar la partida.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 0               |

No se carga y no se guarda la partida en el archivo mencionado

--------------


3. parametros.py: Utiliza e importa correctamente los parámetros del archivo parametros.py.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

Bien

--------------


4. parametros.py: El archivo parametros.py contiene todos los parámetros y constantes que se utilizan a lo largo del programa, además de los especificados en el enunciado.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 2               |

Faltó incluir los path

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 14             | 8               |

#### Bonus (3 **decimas**)

1. Guardar Partida: Cumple con todos los requisitos de este bonus.

| Décimas Máximas | Décimas Obtenidas |
| --------------- | ----------------- |
| 3               | 0                |

No implementado

--------------


> **Resumen décimas**

| Décimas Máximas | Décimas Obtenidas |
| --------------- | ----------------- |
| 3              | 0                |


#### **Descuentos generales (34 décimas)**

#####  Descuentos generales (máximo 10 décimas)

1. Se descuenta hasta 5 décimas si el README no indica archivos los archivos necesarios para ejecutar la tarea ni información relevante para la corrección.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 5                | 2                 |

Intenta dejar el readme como aparece en el template y ahí ir modificando respecto a las cosas que hiciste, las que no y las que fallan un poco. Ayuda bastante la representación gráfica de las cosas, y también te puede ayudar a ti a ver más fácilmente que cosas tienes

--------------


2. Se descuentan hasta 4 décimas por no respetar PEP8

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 4                | 3                 |

Recuerda tener cuidado con los espacios al momento de declarar las cosas. También recuerda que los imports, todos se hacen al inicio del archivo y no entre medio.

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
| 34               | 5                 | 5                  |
