# Semana 4: Programación Orientada a Objetos (OOP) Avanzada

Este documento detalla los conceptos avanzados de OOP en Python para la semana 4 de **Programación Avanzada**.

---

## 1. Herencia y Sobreescritura (`overriding`)

La herencia permite crear una nueva clase (subclase o clase hija) que hereda atributos y métodos de otra clase (superclase o clase madre), promoviendo la reutilización de código.

- **Sobreescritura de Métodos (Overriding)**: Ocurre cuando una subclase define un método con el mismo nombre que uno en su superclase, modificando o extendiendo su comportamiento.
- **Uso de `super()`**: Permite invocar un método de la superclase de forma dinámica sin nombrar la clase explícitamente. Es crucial para el correcto encadenamiento de inicializadores `__init__`.

```python
class Vehiculo:
    def __init__(self, marca: str):
        self.marca = marca

    def encender(self) -> str:
        return "Vehículo encendido."

class Auto(Vehiculo):
    def __init__(self, marca: str, combustible: str):
        super().__init__(marca)  # Llama al inicializador del padre
        self.combustible = combustible

    def encender(self) -> str:
        # Sobreescritura del método encender
        mensaje_base = super().encender()
        return f"{mensaje_base} El motor de {self.combustible} ruge."
```

---

## 2. Polimorfismo y Sobrecarga

El polimorfismo es la habilidad de tratar objetos de diferentes clases de manera uniforme a través de una interfaz común.

### Duck Typing (Tipado de Pato)
En Python, el polimorfismo no se basa en tipos formales o interfaces explícitas, sino en la disponibilidad de métodos y comportamiento. La regla es: *"Si camina como pato y grazna como pato, entonces es un pato"*.
Si un método espera un objeto que implementa un método `hablar()`, cualquier objeto que posea ese método funcionará, sin importar su clase o ancestros.

### Sobrecarga de Operadores (Operator Overloading)
Python permite redefinir el comportamiento de operadores integrados (como `+`, `*`, `==`, etc.) implementando métodos especiales (métodos "dunder", double underscore):

- `__str__(self)`: Retorna la representación informal en string de un objeto (usado por `print()`).
- `__repr__(self)`: Retorna la representación formal en string del objeto (usada en consola y depuración, idealmente debería permitir recrear el objeto).
- `__add__(self, other)`: Define el operador `+`.
- `__eq__(self, other)`: Define el operador de igualdad `==`.
- `__lt__(self, other)`: Define el operador menor que `<` (crucial para ordenamiento automático).

```python
class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Punto({self.x}, {self.y})"

    def __add__(self, other: "Punto") -> "Punto":
        return Punto(self.x + other.x, self.y + other.y)

p1 = Punto(1, 2)
p2 = Punto(3, 4)
print(p1 + p2)  # Salida: Punto(4.0, 6.0) debido a __add__ y __repr__
```

---

## 3. Multiherencia, Problema del Diamante y MRO

La multiherencia ocurre cuando una subclase hereda de más de una superclase. Esto puede generar conflictos conceptuales y de orden de ejecución de métodos.

### El Problema del Diamante
Ocurre cuando una clase `D` hereda de `B` y `C`, y ambas heredan de `A`. Si `A` define un método que `B` y `C` sobreescriben, ¿cuál versión hereda `D`?

```
    A (base)
   / \
  B   C
   \ /
    D (hereda de B y C)
```

### Method Resolution Order (MRO)
Python resuelve este conflicto de manera consistente mediante el algoritmo **C3 Linearization**, el cual calcula una lista lineal y ordenada de clases ancestros llamada **MRO**.
- Se puede inspeccionar el MRO de una clase llamando a `Clase.mro()` o accediendo al atributo `Clase.__mro__`.

### Multiherencia Cooperativa (`*args` y `**kwargs`)
Para asegurar que todos los inicializadores en la cadena del MRO se ejecuten correctamente sin omitir a ninguno, se debe programar de forma cooperativa. **Regla de oro**:
- Cada `__init__` debe usar `super().__init__(*args, **kwargs)` para pasar los argumentos no utilizados al siguiente elemento en el MRO.
- Todos los constructores deben aceptar argumentos genéricos `*args` y `**kwargs` para evitar errores de firma inesperados al recorrer la cadena.

```python
class Investigador:
    def __init__(self, area: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.area = area

class Docente:
    def __init__(self, departamento: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.departamento = departamento

class Academico(Docente, Investigador):
    def __init__(self, nombre: str, departamento: str, area: str, *args, **kwargs):
        # Llama a Docente, que llama a Investigador, que llama a object
        super().__init__(departamento=departamento, area=area, *args, **kwargs)
        self.nombre = nombre
```

---

## 4. Clases Abstractas (`Abstract Base Classes - ABC`)

Una clase abstracta es una clase diseñada para ser una plantilla. **No puede ser instanciada directamente** y define métodos abstractos que sus subclases *deben* implementar.

En Python, se utiliza el módulo `abc`:
- La clase debe heredar de `ABC`.
- Los métodos que deben ser sobreescritos obligatoriamente se marcan con el decorador `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def atacar(self) -> int:
        pass

class Guerrero(Personaje):
    def atacar(self) -> int:
        return 15  # Implementación obligatoria
```

---

## 5. Decoradores y Properties

### Funciones como Objetos de Primera Clase
En Python, las funciones pueden ser pasadas como argumentos, retornadas por otras funciones y definidas dentro de otros ámbitos locales (funciones anidadas).

### Decoradores Personalizados
Un decorador es una función que recibe otra función como argumento, añade cierto comportamiento (envoltura) y retorna la nueva función modificada.

```python
def mi_decorador(func):
    def envoltura(*args, **kwargs):
        print("Antes de llamar a la función")
        resultado = func(*args, **kwargs)
        print("Después de llamar a la función")
        return resultado
    return envoltura

@mi_decorador
def saludar(nombre):
    print(f"Hola {nombre}")
```

### Decoradores Incorporados Importantes
- **`@property`**: Transforma un método de lectura en un atributo virtual o de sólo lectura. Permite aplicar lógica (e.g., validación) al acceder a una variable.
- **`@<atributo>.setter`**: Define la lógica asociada a la modificación del atributo virtual.
- **`@staticmethod`**: Define un método que no recibe la instancia (`self`) ni la clase (`cls`). Se comporta como una función normal pero agrupada dentro de la clase.
- **`@classmethod`**: Define un método que recibe la clase (`cls`) como primer argumento en lugar de la instancia. Útil para constructores alternativos.

```python
class Email:
    def __init__(self, direccion: str):
        self._direccion = direccion

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, nueva_direccion: str):
        if "@" in nueva_direccion:
            self._direccion = nueva_direccion
        else:
            raise ValueError("Email inválido")
```

---

## 6. Diagrama de Clases (UML)

Permite visualizar la estructura de clases del software, sus atributos, métodos y relaciones.

### Representación de una Clase
Se dibuja como una caja dividida en tres partes:
1. **Nombre de la clase**
2. **Atributos** (con visibilidad: `+` público, `-` privado, `#` protegido)
3. **Métodos**

### Relaciones entre Clases
- **Herencia (Especialización)**: Se dibuja una línea con una flecha de punta triangular vacía (`◁`) que apunta desde la clase hija hacia la clase base.
- **Contención (Agregación y Composición)**: Representa que una clase contiene una instancia de otra clase en sus atributos. Se dibuja con un rombo en el extremo de la clase contenedora:
  - **Agregación**: Rombo vacío (`♢`). Indica que la parte puede existir independientemente del todo (e.g., un `Curso` y sus `Estudiantes`).
  - **Composición**: Rombo relleno de negro (`♦`). Indica una dependencia vital de ciclo de vida; si el contenedor se destruye, las partes también (e.g., un `Auto` y su `Motor`).

---

## 7. Ejemplos Prácticos Complementarios

Se ha desarrollado un ejemplo práctico avanzado para demostrar cómo se relacionan estas características orientadas a objetos en un diseño de software real:

### [sistema_combate.py](ejemplos/sistema_combate.py)
Este script simula un motor de combate de juego de rol (RPG). Utiliza:
- **`EntidadCombate` (Clase Abstracta)**: Como plantilla obligatoria para cualquier objeto atacable o atacante.
- **Multiherencia Cooperativa (El Diamante)**: Las clases `Guerrero` y `Mago` heredan de `Personaje`, y la clase `Paladin` hereda de ambos, implementando un constructor que encadena correctamente mediante `super().__init__()` y los parámetros desempaquetados.
- **`__repr__`**: Para imprimir el estado detallado de cada personaje en consola de forma estructurada.
- **Sobrecarga de operadores (`__add__` y `__gt__`)**: Para fusionar personajes sumando sus niveles/vida y compararlos directamente usando operadores relacionales estándar (`>`).
- **Decorador `@log_accion`**: Para interceptar y registrar automáticamente en consola cada ataque o acción realizada por las entidades.

Puedes explorar el código y ejecutarlo directamente desde [materia/04_oop_avanzado/ejemplos/sistema_combate.py](ejemplos/sistema_combate.py) para analizar el orden del MRO y el comportamiento cooperativo.
