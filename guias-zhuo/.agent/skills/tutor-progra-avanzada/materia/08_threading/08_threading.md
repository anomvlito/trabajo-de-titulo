# Semana 8: Concurrencia y Threading (Hilos)

Este documento detalla la teoría, ejemplos prácticos y mecanismos de sincronización para la semana 8 de **Programación Avanzada**.

---

## 1. Concurrencia vs Paralelismo

- **Concurrencia**: Habilidad de procesar múltiples tareas haciendo progreso en intervalos de tiempo superpuestos (e.g., mediante alternancia rápida o *context switching*).
- **Paralelismo**: Ejecución simultánea de múltiples tareas en el mismo instante físico de tiempo (requiere múltiples procesadores o núcleos físicos).

### El GIL (Global Interpreter Lock) de Python
En la implementación de CPython (la estándar), existe el **GIL**, un cerrojo que permite que **solo un hilo ejecute bytecode de Python a la vez**.
- **Consecuencia**: Los threads en Python no logran paralelismo real para tareas **CPU-bound** (cómputo intensivo de procesador).
- **Uso ideal**: Los threads son extremadamente eficientes para tareas **I/O-bound** (entrada/salida, como peticiones de red, lectura/escritura de disco o espera de interacción de usuario), ya que el hilo libera el GIL mientras espera que la operación I/O termine.

---

## 2. Creación y Manejo de Threads

En Python se utiliza el módulo `threading`. Existen dos formas de crear un hilo:

### Método A: Pasando un objetivo (`target`)
```python
import threading
import time

def tarea(nombre: str, espera: int):
    print(f"Hilo {nombre} iniciando...")
    time.sleep(espera)
    print(f"Hilo {nombre} finalizado.")

# Creación de hilos
hilo1 = threading.Thread(target=tarea, args=("A", 2))
hilo2 = threading.Thread(target=tarea, args=("B", 1))

hilo1.start()  # Lanza el hilo. ¡NUNCA llamar a .run() directamente!
hilo2.start()

hilo1.join()   # Bloquea el hilo principal hasta que hilo1 termine.
hilo2.join()
print("Todos los hilos han terminado.")
```

### Método B: Heredando de `threading.Thread`
Útil cuando el hilo requiere mantener estado interno complejo. Se debe sobreescribir el método `run()`.
```python
class MiHilo(threading.Thread):
    def __init__(self, limite: int, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Obligatorio llamar al init padre
        self.limite = limite

    def run(self):
        for i in range(self.limite):
            print(f"Contando: {i}")
            time.sleep(0.5)
```

### Hilos Daemon (Daemon Threads)
Un hilo *daemon* es un hilo de soporte que corre en el fondo. El hilo principal de Python terminará su ejecución aun cuando queden hilos daemon activos (estos se abortarán de inmediato).
- Se definen pasando `daemon=True` al constructor de `Thread` o haciendo `hilo.daemon = True` antes de llamar a `start()`.

---

## 3. Condiciones de Carrera (Race Conditions) y Locks

Una **condición de carrera** ocurre cuando múltiples hilos leen y modifican una variable compartida de forma concurrente, y el resultado final depende del orden de planificación del sistema operativo.

### Sincronización con `threading.Lock`
Para proteger secciones críticas de código (código que manipula memoria compartida), se utiliza un **Lock** (exclusión mutua):

```python
import threading

valor_compartido = 0
lock_variable = threading.Lock()  # El lock debe ser compartido por todos los hilos

def incrementar():
    global valor_compartido
    for _ in range(100000):
        # Regla Crítica: Usar context manager 'with' para asegurar 
        # que el lock se libere aun si ocurre un error dentro.
        with lock_variable:
            # Sección Crítica
            aux = valor_compartido
            valor_compartido = aux + 1
```

---

## 4. Coordinación con `threading.Event`

Un `Event` es uno de los mecanismos más sencillos de comunicación entre hilos: un hilo le avisa a otro que ocurrió un suceso mediante una bandera booleana interna (inicialmente `False`).

### Métodos Principales
- `wait(timeout=None)`: Bloquea el hilo actual hasta que la bandera interna sea `True`.
- `set()`: Cambia la bandera a `True` y despierta a todos los hilos bloqueados en `wait()`.
- `clear()`: Restablece la bandera a `False`.
- `is_set()`: Retorna `True` si la bandera es verdadera.

```python
import threading
import time

evento = threading.Event()

def esperar_senal():
    print("Esperando señal del evento...")
    evento.wait()  # Se bloquea aquí
    print("¡Señal recibida! Hilo continúa.")

def activar_senal():
    time.sleep(2)
    print("Activando señal...")
    evento.set()   # Despierta a los hilos esperando

t1 = threading.Thread(target=esperar_senal)
t2 = threading.Thread(target=activar_senal)
t1.start()
t2.start()
```

---

## 5. Deadlocks (Bloqueos Mutuos)

Un **deadlock** ocurre cuando dos o más hilos quedan bloqueados indefinidamente porque cada uno está esperando por un recurso (un Lock) que tiene retenido el otro hilo.

```
Hilo 1 adquiere Lock A ───> Espera Lock B (retenido por Hilo 2)
Hilo 2 adquiere Lock B ───> Espera Lock A (retenido por Hilo 1)
```

### Prevención de Deadlocks
1. **Adquirir cerrojos en el mismo orden**: Si todos los hilos que necesitan los Locks A y B los adquieren siempre en el orden A y luego B, el deadlock es imposible.
2. **Evitar anidamiento de Locks**: Evitar retener un Lock mientras se intenta adquirir otro.
3. **Usar timeouts**: Utilizar `lock.acquire(timeout=segundos)` para liberar y reintentar si no se obtiene a tiempo.

---

## 6. Patrón Productor-Consumidor

Es un patrón de diseño concurrente común. Uno o más hilos (productores) generan datos y los ponen en un almacenamiento común, y otros hilos (consumidores) los procesan y extraen de allí.

### Uso de `queue.Queue`
Para este patrón se recomienda utilizar la clase **`queue.Queue`** del módulo `queue`, ya que implementa toda la sincronización de hilos necesaria por debajo (bloqueos y condiciones de espera de forma segura y eficiente).

- `put(item)`: Agrega un elemento a la cola. Si la cola está llena, bloquea el hilo hasta que haya espacio.
- `get()`: Remueve y retorna un elemento de la cola. Si la cola está vacía, bloquea el hilo hasta que haya un elemento disponible.
- `task_done()`: Indica que un elemento previamente obtenido mediante `get()` ya fue procesado por completo.
- `join()`: Bloquea el hilo principal hasta que todos los elementos de la cola hayan sido procesados (es decir, que haya un `task_done()` por cada `get()`).

```python
import threading
import queue
import time
import random

cola_trabajos = queue.Queue(maxsize=5)

def productor():
    for i in range(10):
        item = f"Trabajo {i}"
        cola_trabajos.put(item)  # Bloquea si la cola está llena ($maxsize=5$)
        print(f"Producido: {item}")
        time.sleep(random.random())

def consumidor():
    while True:
        item = cola_trabajos.get()  # Bloquea si la cola está vacía
        print(f"Consumido: {item}")
        time.sleep(random.random() * 2)
        cola_trabajos.task_done()   # Avisa que el trabajo terminó

# Iniciar hilos
t_prod = threading.Thread(target=productor)
t_cons = threading.Thread(target=consumidor, daemon=True) # Daemon para que aborte al salir
t_prod.start()
t_cons.start()

t_prod.join()
cola_trabajos.join() # Espera a que todos los elementos sean procesados
print("Todos los trabajos procesados.")
```

---

## 7. Ejemplos Prácticos Complementarios

Se ha desarrollado un ejemplo práctico avanzado de concurrencia y multihilo para demostrar la coordinación e interacción segura entre hilos en un software de simulación real:

### [simulador_descargas.py](ejemplos/simulador_descargas.py)
Este script simula un gestor de descargas concurrentes en red. Utiliza:
- **`threading.Thread`**: Crea hilos de soporte demoníacos (`TrabajadorDescarga`) para descargar partes de archivos en paralelo simulando tareas I/O-bound.
- **`queue.Queue`**: Modela el patrón Productor-Consumidor de forma segura para encolar y despachar los archivos entre los hilos de descarga activos.
- **`threading.Lock`**: Sincroniza la actualización de una variable global compartida (`total_bytes_descargados`), impidiendo condiciones de carrera entre los múltiples trabajadores.
- **`threading.Event`**: Implementa el control dinámico de pausa y reanudación grupal mediante `evento_control_pausa` (bloqueando a los hilos de descarga de forma segura al limpiar la señal de ejecución).
- **Control de Salida Limpia**: Utiliza un evento adicional para propagar la señal de parada y concluir el ciclo de ejecución de los trabajadores sin dejar hilos colgados.

Puedes revisar y ejecutar este script en [materia/08_threading/ejemplos/simulador_descargas.py](ejemplos/simulador_descargas.py) para analizar el comportamiento coordinado de hilos.
