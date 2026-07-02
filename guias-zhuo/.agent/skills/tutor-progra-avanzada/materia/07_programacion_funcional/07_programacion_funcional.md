# Semana 7: Programación Funcional, Generadores e itertools

Este documento detalla la teoría, ejemplos prácticos y conceptos clave de la programación funcional y generadores para la semana 7 de **Programación Avanzada**.

---

## 1. Paradigma de Programación Funcional

La programación funcional es un paradigma donde la computación se trata como la evaluación de funciones matemáticas, evitando los cambios de estado y los datos mutables.

### Conceptos Centrales
- **Funciones Puras**: Funciones que, dado un mismo argumento, siempre retornan el mismo resultado y **no tienen efectos colaterales** (no modifican variables globales, archivos, argumentos mutables, etc.).
- **Inmutabilidad**: Los datos no se modifican; en su lugar, se crean nuevos datos derivados de los originales. Esto facilita enormemente la legibilidad y la concurrencia segura.
- **Funciones de Primera Clase**: Las funciones son tratadas como cualquier otro objeto. Pueden ser guardadas en variables, pasadas como argumentos y retornadas por otras funciones.

---

## 2. Expresiones Lambda
Son funciones anónimas definidas en una sola línea. No contienen sentencias complejas (como `return` explícito o bucles) y solo evalúan una expresión que se retorna automáticamente.

```python
# Sintaxis: lambda argumentos: expresion
sumar = lambda x, y: x + y
print(sumar(5, 3))  # 8
```

---

## 3. Funciones de Orden Superior en Iterables

Son funciones que reciben como argumento otra función para operar sobre una colección.

### `map(funcion, iterable)`
Aplica una función a cada elemento de un iterable. Retorna un generador (objeto lazy/perezoso).
```python
numeros = [1, 2, 3, 4]
duplicados = list(map(lambda x: x * 2, numeros))  # [2, 4, 6, 8]
```

### `filter(funcion, iterable)`
Filtra los elementos del iterable conservando solo aquellos para los cuales la función (predicado) retorna `True`. Retorna un objeto lazy.
```python
pares = list(filter(lambda x: x % 2 == 0, numeros))  # [2, 4]
```

### `reduce(funcion, iterable[, inicializador])`
Aplica de forma acumulativa una función de dos argumentos a los elementos de izquierda a derecha. Debe importarse desde el módulo `functools`.
```python
from functools import reduce
suma_total = reduce(lambda acumulado, actual: acumulado + actual, numeros)  # 10
```

### `zip(*iterables)`
Agrupa los elementos correspondientes de múltiples iterables en tuplas. Termina cuando el iterable más corto se agota. Retorna un objeto lazy.
```python
nombres = ["Ana", "Bob"]
edades = [25, 30, 35]
combinado = list(zip(nombres, edades))  # [("Ana", 25), ("Bob", 30)]
```
- **Inversa de `zip`**: Usar el operador de desempaquetado `*` con `zip`:
  ```python
  nombres_rec, edades_rec = zip(*combinado)
  # nombres_rec = ("Ana", "Bob"), edades_rec = (25, 30)
  ```

### `enumerate(iterable[, start])`
Retorna un iterador de tuplas `(indice, elemento)` facilitando el acceso al índice durante un recorrido.
```python
for indice, valor in enumerate(["A", "B"], start=1):
    print(f"{indice}: {valor}")  # 1: A, 2: B
```

---

## 4. Funciones Generadoras y Generadores

Un **generador** es un tipo especial de iterador que produce valores de forma perezosa (on-demand), evitando almacenar la colección completa en memoria.

### Funciones Generadoras y `yield`
Se definen como funciones normales, pero utilizan la palabra clave `yield` en lugar de `return`.
- Al encontrar `yield`, la función produce el valor y **suspende temporalmente su ejecución**, guardando todo su estado de variables locales.
- Al pedir el siguiente elemento (vía `next` o un `for`), la función se reanuda justo en la línea posterior al `yield`.

```python
def contador_tres():
    yield 1
    yield 2
    yield 3

gen = contador_tres()
print(next(gen))  # 1
print(next(gen))  # 2
```

### Expresiones Generadoras
Sintaxis compacta similar a las listas por comprensión, pero utilizando paréntesis `()` en lugar de corchetes `[]`. No crea la lista en memoria.
```python
# Expresión generadora (O(1) memoria)
cuadrados_gen = (x**2 for x in range(1000000)) 
```

### Comunicación con Generadores (`send`)
El método `send(valor)` permite enviar datos de regreso al generador. El generador recibe el valor como resultado de la expresión `yield`.
- **Importante**: Para iniciar un generador (hacer un "primer paso" o *prime*), se debe llamar primero a `next(generador)` o `generador.send(None)`.

```python
def acumulador():
    total = 0
    while True:
        # yield suspende y retorna el 'total'. Al reanudarse con send(valor),
        # el 'valor' se asigna a la variable 'recibido'.
        recibido = yield total
        if recibido is not None:
            total += recibido

gen = acumulador()
print(next(gen))       # 0 (inicializa el generador hasta el primer yield)
print(gen.send(10))    # 10 (envía 10, total se hace 10, retorna 10)
print(gen.send(5))     # 15 (envía 5, total se hace 15, retorna 15)
```

---

## 5. El Módulo `itertools`

Proporciona funciones altamente optimizadas para crear y manipular iteradores complejos.

- `count(start=0, step=1)`: Crea un iterador infinito que cuenta desde `start` con pasos de tamaño `step`.
- `cycle(iterable)`: Guarda una copia del iterable y repite sus elementos infinitamente en ciclo.
- `repeat(object[, times])`: Repite el objeto infinitamente o una cantidad `times` de veces.
- `chain(*iterables)`: Concatena múltiples iterables de forma secuencial en un único iterador.
  ```python
  import itertools
  list(itertools.chain([1, 2], [3, 4]))  # [1, 2, 3, 4]
  ```
- `groupby(iterable, keyfunc=None)`: Agrupa los elementos consecutivos del iterable que tengan la misma llave calculada por `keyfunc`.
  - **¡Regla Crítica!**: El iterable **debe estar ordenado** bajo la misma función llave antes de llamar a `groupby`. De lo contrario, agrupará de forma fragmentada.
  ```python
  datos = ["perro", "gato", "loro", "raton"]
  datos.sort(key=len)  # Paso obligatorio
  for largo, grupo in itertools.groupby(datos, len):
      print(f"Largo {largo}: {list(grupo)}")
  ```
- `permutations(iterable, r)`: Retorna permutaciones de longitud `r`.
- `combinations(iterable, r)`: Retorna combinaciones de longitud `r` sin repetición de elementos.

---

## 6. Eficiencia: Generadores vs Estructuras en Memoria

En programación avanzada, optimizar el uso de memoria es crucial:
1. **Carga Perezosa de Archivos**: Leer un archivo de texto línea a línea usando un archivo iterable (`for linea in archivo:`) mantiene solo una línea en memoria, a diferencia de `archivo.readlines()` que carga todo el contenido.
2. **Generadores como pipelines**: Conectar generadores (e.g. filtrar datos y luego mapear) permite procesar millones de registros sin que el consumo de memoria aumente.

---

## 7. Ejemplos Prácticos Complementarios

Se ha desarrollado un ejemplo práctico completo para ilustrar cómo integrar el diseño funcional, la comunicación bidireccional con generadores y las herramientas avanzadas de iteración:

### [procesamiento_datos.py](ejemplos/procesamiento_datos.py)
Este script simula un procesador de analíticas y comportamiento de usuarios. Utiliza:
- **Funciones Puras e Inmutabilidad**: Mantiene funciones sin efectos secundarios para filtrar y extraer datos sobre eventos simulados.
- **Funciones de Orden Superior (`map`, `filter`, `reduce`)**: Combina transformaciones y acumulaciones de datos usando `lambda`.
- **Generadores Cooperativos (`yield` y `send()`)**: Crea un acumulador dinámico que calcula el promedio móvil sobre un flujo de valores, inyectando datos desde el exterior y recuperando resultados en tiempo real.
- **Módulo `itertools`**:
  - `chain` para fusionar eficientemente flujos de registros sin duplicar memoria.
  - `groupby` para agrupar datos de analíticas por el tipo de evento (ordenando previamente).
  - `combinations` para identificar pares de eventos realizados por el mismo usuario con el fin de modelar patrones de navegación.

Puedes ver y probar el script en [materia/07_programacion_funcional/ejemplos/procesamiento_datos.py](ejemplos/procesamiento_datos.py) para analizar el procesamiento funcional y generadores.
