# Semana 3: Estructuras de Datos y Argumentos Variables

Este documento contiene la teoría detallada, ejemplos prácticos y reglas de diseño para la materia de estructuras de datos y manejo de argumentos de la semana 3 en **Programación Avanzada**.

---

## 1. Tuplas (`tuple`)
Las tuplas son contenedores secuenciales, ordenados e **inmutables**. Una vez creada, no es posible agregar, modificar ni eliminar sus elementos.

### Características Clave
- **Definición**: Se definen separando elementos por comas, opcionalmente rodeados por paréntesis. Para crear una tupla de un solo elemento, es obligatorio usar una coma: `mi_tupla = (42,)`.
- **Acceso**: Soporta indexación y *slicing* ($O(1)$).
- **Casos de uso**:
  - Representación de registros estáticos (e.g., coordenadas `(x, y)`, colores `(R, G, B)`).
  - Retorno de múltiples valores en una función: `return x, y`.
  - Como llaves en un diccionario (ya que son inmutables y *hasheables*, siempre que sus elementos internos también lo sean).

---

## 2. Stacks (Pilas)
Una pila es una estructura de datos lineal que sigue el principio **LIFO** (*Last In, First Out*): el último elemento en entrar es el primero en salir.

### Operaciones Fundamentales
- **Push**: Agregar un elemento al tope. En Python se implementa usando `list.append()`. Eficiencia: $O(1)$ amortizado.
- **Pop**: Eliminar y retornar el elemento del tope. En Python se usa `list.pop()`. Eficiencia: $O(1)$ amortizado.
- **Peek**: Observar el elemento en el tope sin removerlo. En Python: `mi_lista[-1]`. Eficiencia: $O(1)$.
- **Is Empty**: Verificar si la pila está vacía. En Python: `len(mi_lista) == 0`. Eficiencia: $O(1)$.

```python
# Ejemplo de Stack usando list
stack = []
stack.append(10)  # Push 10
stack.append(20)  # Push 20
top = stack[-1]   # Peek -> 20
item = stack.pop() # Pop -> 20
is_empty = len(stack) == 0  # False
```

---

## 3. Colas (Queues)
Una cola es una estructura de datos lineal que sigue el principio **FIFO** (*First In, First Out*): el primer elemento en entrar es el primero en salir.

### Implementación Eficiente en Python
**¡Cuidado!** Usar una lista de Python (`list`) como cola es un anti-patrón de rendimiento. Al hacer `list.pop(0)`, todos los elementos restantes deben desplazarse una posición a la izquierda, lo que toma tiempo lineal $O(N)$.

Para implementar una cola de manera eficiente ($O(1)$), se debe utilizar la clase `deque` del módulo `collections`:

- **Enqueue**: Agregar un elemento al final de la cola. Usar `deque.append(item)`. Eficiencia: $O(1)$.
- **Dequeue**: Remover y retornar el primer elemento de la cola. Usar `deque.popleft()`. Eficiencia: $O(1)$.
- **Peek**: Observar el primer elemento. Usar `deque[0]`. Eficiencia: $O(1)$.

```python
from collections import deque

queue = deque()
queue.append("A")      # Enqueue "A"
queue.append("B")      # Enqueue "B"
front = queue[0]       # Peek -> "A"
first = queue.popleft() # Dequeue -> "A" ($O(1)$)
```

---

## 4. Diccionarios (`dict`)
Un diccionario es una estructura de datos asociativa no secuencial y **mutable** que mapea **llaves únicas** a **valores**.

### Características y Rendimiento
- **Búsqueda, Inserción y Eliminación**: Operaciones extremadamente eficientes con tiempo promedio $O(1)$, ya que utiliza una *tabla de hash* por detrás.
- **Llaves permitidas**: Solo objetos **inmutables y hasheables** (e.g., `int`, `str`, `float`, `tuple` de hasheables). No se pueden usar listas, sets ni otros diccionarios como llaves.
- **Valores permitidos**: Cualquier tipo de objeto (mutables o inmutables).
- **Mantenimiento del orden**: Desde Python 3.7, los diccionarios mantienen el orden de inserción de sus llaves.

### Métodos Útiles
- `get(key, default)`: Retorna el valor de la llave. Si no existe, retorna `default` (evita levantar `KeyError`).
- `items()`: Retorna una vista de tuplas `(llave, valor)`.
- `keys()` / `values()`: Retorna vistas con las llaves o valores.
- `setdefault(key, default)`: Si la llave existe, retorna su valor; si no, la crea con el valor `default` y lo retorna.

### Diccionarios por Comprensión
Permiten crear diccionarios de forma concisa:
```python
cuadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 5. Defaultdict (`collections.defaultdict`)
Es una subclase de `dict` que evita el problema de inicializar llaves inexistentes al proporcionar un valor por defecto automáticamente mediante una función constructora (o fábrica).

### Caso de Uso Común: Agrupación
Sin `defaultdict`:
```python
grupos = {}
for persona, grupo in datos:
    if grupo not in grupos:
        grupos[grupo] = []
    grupos[grupo].append(persona)
```

Con `defaultdict`:
```python
from collections import defaultdict

grupos = defaultdict(list)  # list es la función fábrica que retorna []
for persona, grupo in datos:
    grupos[grupo].append(persona)  # Si la llave no existe, inicializa [] y hace append
```

---

## 6. Sets (Conjuntos)
Un set es una colección **mutable**, **no ordenada** y que **no permite elementos duplicados**.

### Propiedades y Eficiencia
- **Membership tests (`in`)**: Buscar si un elemento pertenece al set toma tiempo promedio $O(1)$, ideal para filtrados rápidos y eliminación de duplicados.
- **Restricción**: Los elementos de un set deben ser **hasheables** (inmutables).

### Operaciones de Conjunto
Sean dos sets `A` y `B`:
- **Unión (`A | B` o `A.union(B)`)**: Elementos en `A`, en `B` o en ambos.
- **Intersección (`A & B` o `A.intersection(B)`)**: Elementos presentes en ambos conjuntos.
- **Diferencia (`A - B` o `A.difference(B)`)**: Elementos en `A` que no están en `B`.
- **Diferencia Simétrica (`A ^ B` o `A.symmetric_difference(B)`)**: Elementos que están en `A` o en `B`, pero no en ambos.

---

## 7. Argumentos Variables (`*args` y `**kwargs`)

Permiten definir funciones que acepten un número dinámico o variable de argumentos.

### Conceptos Clave
- **Argumentos vs Parámetros**: Los *parámetros* se declaran en la definición de la función. Los *argumentos* son los valores reales provistos al llamarla.
- **`*args` (Arguments)**: Captura argumentos posicionales adicionales y los empaqueta en una **tupla**.
- **`**kwargs` (Keyword Arguments)**: Captura argumentos de palabra clave (con nombre) adicionales y los empaqueta en un **diccionario**.

### Orden Correcto en Definiciones de Funciones
Python exige un orden estricto en la firma de una función:
1. Argumentos posicionales obligatorios.
2. Argumentos opcionales (con valores por defecto).
3. Parámetro `*args`.
4. Argumentos nombrados obligatorios (después de `*args`).
5. Parámetro `**kwargs`.

```python
def funcion_completa(a, b=10, *args, c, d=20, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"c: {c}, d: {d}")
    print(f"kwargs: {kwargs}")

# Llamada:
funcion_completa(1, 2, 3, 4, c=30, e=50, f=60)
# a: 1, b: 2
# args: (3, 4)
# c: 30, d: 20
# kwargs: {'e': 50, 'f': 60}
```

### Desempaquetado (Unpacking)
También es posible usar `*` y `**` al *llamar* a una función para expandir listas/tuplas o diccionarios en argumentos:
```python
def sumar(x, y, z):
    return x + y + z

valores_lista = [1, 2, 3]
valores_dict = {"x": 10, "y": 20, "z": 30}

print(sumar(*valores_lista))  # Equivalente a sumar(1, 2, 3)
print(sumar(**valores_dict))  # Equivalente a sumar(x=10, y=20, z=30)
```

---

## 8. Ejemplos Prácticos Complementarios

Se ha desarrollado un ejemplo práctico que demuestra cómo integrar todas estas estructuras en un sistema cohesivo:

### [control_tienda.py](ejemplos/control_tienda.py)
Este script simula un gestor de inventario y procesamiento de órdenes de una tienda. Utiliza:
- **`namedtuple`** para definir productos de catálogo inmutables.
- **`deque`** como cola FIFO para encolar y procesar las compras en el orden exacto de llegada de los clientes.
- **`defaultdict(int)`** y **`defaultdict(float)`** para llevar el stock de inventario e ingresos por categoría, eliminando la necesidad de verificar la existencia de llaves.
- **`set`** para registrar los IDs únicos de los clientes que han realizado compras con éxito.
- **`*args` y `**kwargs`** para construir un logger dinámico reutilizable y formatear los mensajes del sistema con metadatos opcionales.

Puedes revisar y ejecutar el script directamente desde [materia/03_estructuras_datos/ejemplos/control_tienda.py](ejemplos/control_tienda.py) para ver cómo operan estas estructuras integradas en tiempo de ejecución.
