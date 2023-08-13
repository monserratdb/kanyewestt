# Tarea 0: DCCeldas

Definí mi Menú de Acción antes que el Menú de Inicio, pues quería asegurarme de que apenas se ingresara un string que estuviera dentro de la carpeta Archivos, se pudiera entrar al Menú de Acciones sin problema.

La función ```solucionar_tablero``` presenta fallas porque no pude trabajarla con recursividad y no logré que las condiciones se siguieran correctamente para que no pusiera más "T" de las que debía (aún así, la función ```verificar_tortugas``` funciona de manera correcta, al igual que la función ```verificar_alcance_bomba``)
Probé ```guardar_tablero``` y funciona correctamente creando un archivo en formato .txt, que además sigue el formato de los archivos dados (Ej: "2,2,-,2,-"), pero no supe cómo agregar el archivo creado a la carpeta 
Archivos


## Consideraciones generales

### Cosas implementadas y no implementadas 

* <Verificar regla 1</sub>>: Hecha completa
* <Verificar regla 2</sub>>: Hecha completa
* <Verificar regla 3</sub>>: Hecha completa
* <Verificar regla 4</sub>>: Hecha completa
* <Funcion solucionar_tablero</sub>>: Presenta fallas
* <Funcion guardar_tablero</sub>>: Hecha completa

## Ejecución
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe contar con las siguientes funciones y archivos adicionales:
1. ```tablero.py``` en la misma carpeta en que se ejecuta ```main.py```
2. ```functions.py``` en la misma carpeta en que se ejecuta ```main.py```
3. ```Archivos``` (que debe contener archivos con extensión .txt) en la misma carpeta en que se ejecuta ```main.py```


## Librerías y librerías propias
La lista de librerías externas que utilicé fue la siguiente:
- os

La lista de librerías propias que utilicé fue la siguiente:
- functions
- tablero

## Supuestos y consideraciones adicionales
Los supuestos que realicé durante la tarea son los siguientes:

1. <Que la regla 3 sólo es inválida cuando ocurre que en una celda se tiene algo como "2T" o "-T" y es válido porque en las issues se mencionó que nunca nos darán archivos que tengan dos elementos entre las comas. Como 2,2T,-,2,-. > 
2. <Que para saber si un archivo tiene o no solución, sólo se me darán archivos que tienen bombas y espacios vacíos ("numero" y "-") ya que de esa forma la única regla que verifica si tiene solución o no el tablero, es la regla 2.> 


## Referencias de código externo


Para realizar mi tarea saqué código de:
1. https://github.com/loricode/menupython/blob/master/menupython.py: este lo utilicé más que nada para darme una idea de cómo funcionaba un Menú en python, pues nunca había hecho uno. No copié código literal.

2. \https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks: 
 este separa los elementos de la lista en el valor que yo le indico y está implementado en el archivo
<functions.py> en las línea 9.


PD: perdón si este no era el orden, pero por error borré lo que viene a continuación del orden original que nos dieron
## Verificación por item
Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si *NO* completaste lo pedido
- ✅ si completaste *correctamente* lo pedido
- 🟠 si el item está *incompleto* o tiene algunos errores
#### Menú de Inicio (5 pts) (7%)
##### ✅ Seleccionar Archivo
##### ✅ Validar Archivos
#### Menú de Acciones (11 pts) (15%) 
##### ✅ Opciones
##### ✅ Mostrar tablero 
##### ✅ Validar bombas y tortugas
##### ✅ Revisar solución
##### 🟠 Solucionar tablero
##### ✅ Salir
#### Funciones (34 pts) (45%)
##### ✅ Cargar tablero
##### ✅ Guardar tablero
##### ✅ Valor bombas
##### ✅ Alcance bomba
##### ✅ Verificar tortugas
##### 🟠 Solucionar tablero
#### General: (19 pts) (25%)
##### ✅ Manejo de Archivos
##### ✅ Menús
##### ✅ tablero.py
##### ✅ Módulos
##### 🟠 PEP-8
#### Bonus: 6 décimas
##### ❌ Funciones atómicas
##### ❌ Regla 5
