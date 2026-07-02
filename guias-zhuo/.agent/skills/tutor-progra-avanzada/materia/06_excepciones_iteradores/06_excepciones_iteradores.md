# Semana 6: Excepciones, Iterables, Iteradores y Listas Ligadas

Este documento detalla la teoría, ejemplos y buenas prácticas para la materia de la semana 6 en **Programación Avanzada**.

---

## 1. Excepciones en Python

Las excepciones son eventos de error que ocurren durante la ejecución de un programa (tiempo de ejecución), interrumpiendo el flujo normal de instrucciones. Son distintas de los errores sintácticos (como `SyntaxError` o `IndentationError`), los cuales impiden que el código llegue a ejecutarse.

### Tipos Comunes de Excepciones
- `NameError`: Intento de acceder a una variable local o global no definida.
- `ZeroDivisionError`: División por cero.
- `IndexError`: Acceso a un índice fuera de rango en una secuencia (lista, tupla).
- `KeyError`: Acceso a una llave inexistente en un diccionario.
- `AttributeError`: Intento de acceder a un atributo o método inexistente en un objeto.
- `TypeError`: Operación aplicada a un objeto de tipo inapropiado.
- `ValueError`: Operación recibe un argumento con el tipo correcto pero valor inapropiado (e.g. `int("hola")`).

### Levantando Excepciones (`raise`)
Podemos lanzar una excepción de forma voluntaria en el código utilizando la instrucción `raise`:
```python
def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("El divisor no puede ser cero.")
    return a / b
```

### Manejo de Excepciones (`try`, `except`, `else`, `finally`)
Para controlar excepciones y evitar que el programa aborte bruscamente, usamos el bloque `try-except`:

```python
try:
    # Código que puede lanzar excepciones
    resultado = dividir(10, 0)
except ZeroDivisionError as err:
    # Código que maneja específicamente esta excepción
    print(f"Error detectado: {err}")
except (TypeError, ValueError) as err:
    # Manejo de múltiples tipos de excepción en un solo bloque
    print(f"Error de tipo o valor: {err}")
else:
    # Se ejecuta SOLO si NO se lanzó ninguna excepción en el bloque try
    print(f"Operación exitosa. Resultado: {resultado}")
finally:
    # Se ejecuta SIEMPRE, haya o no una excepción, e incluso si hay un return previo.
    # Ideal para liberar recursos (cerrar archivos, conexiones a BD, etc.)
    print("Limpieza finalizada.")
```

### Excepciones Personalizadas
Es posible definir excepciones propias creando subclases de `Exception` (o de algún error más específico):
```python
class EdadInvalidaError(Exception):
    """Excepción levantada al ingresar una edad fuera del rango permitido."""
    def __init__(self, edad: int):
        mensaje = f"La edad {edad} no está en el rango permitido (0-120)."
        super().__init__(mensaje)

# Uso:
edad_usuario = 150
if edad_usuario > 120:
    raise EdadInvalidaError(edad_usuario)
```

---

## 2. Iterables e Iteradores

En Python, la iteración (como los bucles `for`) se sustenta en un protocolo formal compuesto por dos conceptos complementarios.

### Iterable
Un objeto es **iterable** si puede retornar sus elementos uno a uno.
- Debe implementar el método especial `__iter__()`, el cual debe retornar un objeto **iterador**.
- Ejemplos integrados: `list`, `tuple`, `dict`, `set`, `str`.

### Iterador
Un objeto es un **iterador** si realiza el seguimiento del estado de la iteración.
- Debe implementar el método especial `__next__()`, el cual retorna el siguiente elemento en cada llamada. Cuando no quedan más elementos, debe levantar la excepción `StopIteration`.
- Debe implementar el método especial `__iter__()` que se retorna a sí mismo (`return self`).

### El Protocolo por Detrás de un `for`
Cuando escribimos `for x in iterable:`, Python realiza lo siguiente por detrás:
```python
# Equivalente conceptual
iterable = [1, 2, 3]
iterador = iter(iterable)  # Llama a iterable.__iter__()
while True:
    try:
        x = next(iterador)  # Llama a iterador.__next__()
        # ... cuerpo del for ...
    except StopIteration:
        break  # Termina la iteración de manera limpia
```

### Ejemplo de Iterador Personalizado
```python
class RangoPares:
    def __init__(self, maximo: int):
        self.maximo = maximo
        self.actual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual >= self.maximo:
            raise StopIteration
        valor = self.actual
        self.actual += 2
        return valor

# Uso:
for par in RangoPares(6):
    print(par)  # Imprime: 0, 2, 4
```

---

## 3. Listas Ligadas (Linked Lists)

Una lista ligada es una estructura de datos secuencial compuesta por **Nodos** enlazados entre sí. A diferencia de las listas de Python (que son arreglos dinámicos en memoria contigua), los nodos de una lista ligada pueden estar dispersos en memoria y cada uno almacena una referencia al siguiente nodo.

### Clases Base (`Nodo` y `ListaLigada`)
```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # Apunta al siguiente objeto Nodo

class ListaLigada:
    def __init__(self):
        self.cabeza = None  # Apunta al primer Nodo de la lista

    def agregar_inicio(self, valor):
        """Inserta un nodo al inicio de la lista ($O(1)$)."""
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def agregar_final(self, valor):
        """Inserta un nodo al final de la lista ($O(N)$ sin puntero cola)."""
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo
```

### Cómo Hacer Iterable una Lista Ligada
Para poder recorrer la `ListaLigada` con un bucle `for` de forma directa, podemos definir un iterador personalizado para la lista:

```python
class IteradorListaLigada:
    def __init__(self, cabeza_nodo: Nodo):
        self.actual = cabeza_nodo

    def __iter__(self):
        return self

    def __next__(self):
        if not self.actual:
            raise StopIteration
        valor = self.actual.valor
        self.actual = self.actual.siguiente
        return valor

# Modificando la clase ListaLigada original para añadir soporte:
class ListaLigadaIterable(ListaLigada):
    def __iter__(self):
        return IteradorListaLigada(self.cabeza)

# Uso:
lista = ListaLigadaIterable()
lista.agregar_inicio(3)
lista.agregar_inicio(2)
lista.agregar_inicio(1)

for val in lista:
    print(val)  # Imprime 1, 2, 3 secuencialmente
```

---

## 4. Ejemplos Prácticos Complementarios

Se ha desarrollado un ejemplo práctico para demostrar cómo integrar el control estructurado de excepciones, el protocolo de iteración y las estructuras enlazadas en un único software coherente:

### [analizador_logs.py](ejemplos/analizador_logs.py)
Este script implementa un analizador inteligente para archivos de logs simulados. Utiliza:
- **Excepciones Personalizadas (`FormatoLogInvalidoError` y `NivelLogInvalidoError`)**: Para detectar anomalías de sintaxis en el archivo de texto y descartar logs incorrectos de forma controlada.
- **Flujo `try-except-else-finally`**: Permite al parser interceptar errores específicos en cada línea sin abortar el procesamiento completo de otras líneas correctas del archivo.
- **Protocolo de Iteración (`LectorLogs`)**: Define un iterador personalizado que separa campos línea por línea bajo demanda, simulando un procesamiento eficiente en memoria (perezoso) sobre un flujo grande.
- **Lista Ligada Personalizada (`ListaLigadaErrores`)**: Almacena en memoria de forma secuencial y eficiente aquellos logs detectados con niveles de criticidad altos (`ERROR` y `CRITICAL`), permitiendo recorrerlos secuencialmente usando su propio iterador interno.

Puedes ejecutar e inspeccionar el código de este ejemplo en [materia/06_excepciones_iteradores/ejemplos/analizador_logs.py](ejemplos/analizador_logs.py) para analizar el manejo secuencial de excepciones e iteración.
