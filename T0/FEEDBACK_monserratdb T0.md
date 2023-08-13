# FEEDBACK T0

**Repositorio de _monserratdb_**

## Resumen

| Puntaje Máximo | Puntaje Obtenido | Décimas descuento | Nota final |
| -------------- | ----------------  | ----------------- | ---------- |
| 69            |  38,5              | 0,0                | **4.35**     |

## Comentario general 

Me gusto mucho tu codigo, eres ordenada y se puede leer correctamente sin problemas tu codigo. Intenta trabajar mejor tus archivos y comprender los path relativos, para así el corrector pueda probar la robustez de tu codigo. Tienes mucho talento! sigue asi



### Puntaje por sección

#### Menú de inicio: 5 pts

1. **Seleccionar Archivo**. El menú permite escribir el nombre del archivo y posteriormente ingresa al Menú de Acciones.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

bien!

--------------


2. **Validar Archivo**. Verifica correctamente la existencia del archivo cuyo nombre es el input ingresado. En caso de que no exista, se advierte al usuario y se cierra el programa.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 3               |

bien!

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 5              | 5               |

#### Menú de Acciones: 11 pts

1. **Opciones**. El menú contiene todas las opciones mínimas pedidas en el enunciado.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

bien!

--------------


2. **Mostrar tablero**. Al seleccionar esta opción, se visualiza correctamente el tablero cargado desde los archivos.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 6              | 2               |

bien!

--------------


3. **Validar bombas y tortugas**. Al seleccionar esta opción, se valida que el tablero cumpla las Reglas 2 y 4 y muestra en consola la respuesta.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 1               |

No puedes validar bomba en tablero = [ '12','-','-','-','-','-', '14'],['-','-', "14','-','-','-','-'],['-','-','-','-','-','-','-'],['-','-','14','-','-','5','-'],['-','-','-','-','-','-','-'],['14','-','-','3','-','-','-'],['12','-','-','-', '14','-', '3' ] en este caso, la primera entrada tiene un borde incorrecto.

--------------


4. **Revisar solución**. Al seleccionar esta opción, se revisa si la solución cumple con todas las reglas obligatorias e imprime el resultado.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

bien!

--------------


5. **Solucionar tablero**. Al seleccionar esta opción, se soluciona el tablero cargado y se guarda correctamente la solución en el archivo correspondiente. En caso contrario, se notifica al usuario.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

No soluciona para tablero = [['-','3'],['-','-']], ni para tableros invalidos o tableros vacios.

--------------


6. **Salir**. Al seleccionar esta opción, se sale correctamente del programa.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 1              | 1               |

bien!

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 11             | 8               |

#### Funciones: 34 pts

1. **Cargar tablero**. La función recibe los parámetros solicitados y retorna correctamente una lista de listas con la información del tablero.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 1,5               |

Problema en la carga de archivos "No such file or directory: 'Archivos\\archivo_test.txt'" Problemas con los path relativos.

--------------


2. **Guardar tablero**. La función recibe los parámetros solicitados y guarda correctamente el archivo correspondiente.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 1,5               |

Problema en la carga de archivos "No such file or directory: 'Archivos\\archivo_test.txt'" Problemas con los path relativos.

--------------


3. **Valor bombas**. La función recibe los parámetros solicitados y verifica que el valor de la bomba sea válido. Retorna el int correspondiente. 

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 3              | 1,5               |

3

--------------


4. **Alcance bomba**. La función recibe los parámetros solicitados y calcula el número de celdas que afecta dicha bomba. Retorna el int correspondiente.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 6              | 6               |

bien!

--------------


3. **Verificar tortugas**. La función recibe los parámetros solicitados y calcula la cantidad de tortugas que tengan uno o más vecinos tortugas. Retorna el int correspondiente.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 4              | 4               |

bien!

--------------


3. **Solucionar tablero**. La función recibe los parámetros solicitados, crea una solución del tablero verificando que todas las reglas obligatorias se cumplan y retorna una lista de listas con la solución del tablero. 

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 15              | 0               |

No basta con solucionar un caso, por ejemplo. para el tablero = [
            ['T','3','T','-'],
            ['-','-','-','-'],
            ['-','-','-','-'],
            ['-','-','-','-'],
        ] no se puede hallar solucion de bombas entre tortugas.

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 34              | 14,5               |

#### General: 19 pts

1. **Manejo de Archivos**. Se trabaja correctamente con los archivos. Se lee el tablero de forma correcta a partir del archivo de texto correspondiente.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

bien!

--------------


2. **Manejo de Archivos**. Se trabaja correctamente con los archivos. Se escribe el tablero de forma correcta en el archivo de texto correspondiente.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

bien!

--------------


3. **Menús**. Los menús son a prueba de todo tipo de errores.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 0               |

Tu programa se cae facilemente al colocar la opcion enter

--------------


4. **tablero.py**. Se importa y utiliza correctamente la función para imprimir el tablero.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 2              | 2               |

bien!

--------------


5. **Módulos**. El programa se encuentra modularizado si es necesario.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 5              | 5               |

bien!

--------------


6. **PEP8**. El programa respeta correctamente PEP8.

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 6              | 0               |

Mucho error Pep8, ojo con el uso de las ","

--------------


> **Resumen puntaje**

| Puntaje Máximo | Puntaje Obtenido |
| -------------- | ---------------- |
| 19             | 11               |

#### Bonus: 6 décimas máximo

1. **Funciones atómicas**. Cumple con todos los requisitos de este bonus.

| Décimas Máximas | Décimas Obtenidas |
| --------------- | ----------------- |
| 2               | 0                |

Funciones extensas, quiza podrias ser más breve en tus condicionales para hacer mas cosas en menos codigo.

--------------


2. **Regla 5**. Cumple con todos los requisitos de este bonus.

| Décimas Máximas | Décimas Obtenidas |
| --------------- | ----------------- |
| 4               | 0                |

no implementado

--------------


> **Resumen bonus**

| Décimas Máximas | Décimas Obtenidas |
| --------------- | ----------------- |
| 6               | 0                |

#### Descuentos generales (20 décimas)

##### Descuentos generales (máximo 10 décimas)

1. Se descuenta 1 décima si el README no indica los archivos necesarios para ejecutar la tarea.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 1                | 0                 |

Excelente Readme

--------------


2. Se descuenta hasta 4 décimas si el README no incluye aspectos implementados y no implementados, o bien cualquier información relevante para la corrección.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 4                | 0                 |

Todo detallado y bien referenciado

--------------


3. Se descuentan 5 décimas si no se sigue el formato de entrega.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 5                | 0                 |

Repositorio limpio y buen uso de gitignore, felicitaciones!

--------------


4. Se descuentan 1-5 décimas por cambio de líneas.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 5                | 0                 |

bien!

--------------


##### Descuentos por utilizar alguna librería o Built-in no autorizado (5 décimas)

1. Se descuentan 1- 5 décimas por utilizar alguna librería o Built-in no autorizado. Tal como dice en cada enunciado de tarea, no se permite ninguna librería a no ser que nosotros especifiquemos lo contrario.

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 5                | 0                 |

Bien!

--------------


> **Resumen Descuento**

| Descuento máximo | Descuento Obtenido |
| ---------------- | ------------------ |
| 15               | 0                 |
