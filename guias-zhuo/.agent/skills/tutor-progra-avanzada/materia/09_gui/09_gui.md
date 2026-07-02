# Semana 9: Interfaces Gráficas de Usuario (GUI) con PyQt5

Este documento detalla la arquitectura, elementos gráficos y patrones de diseño recomendados para el desarrollo de interfaces gráficas usando PyQt5 en **Programación Avanzada**.

---

## 1. Fundamentos de PyQt5

PyQt5 es un binding de Python para el framework gráfico multiplataforma Qt. Funciona bajo un flujo de ejecución dirigido por eventos (Event-Loop).

### Estructura Mínima de una Aplicación
Toda aplicación gráfica en PyQt5 requiere instanciar un `QApplication` para controlar el loop de eventos y mantener viva la interfaz.

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 1. Crear la aplicación pasando los argumentos de sistema
app = QApplication(sys.argv)

# 2. Instanciar la ventana principal
ventana = QWidget()
ventana.setWindowTitle("Mi Primera Ventana")
ventana.resize(400, 300)

# 3. Mostrar la ventana
ventana.show()

# 4. Iniciar el event-loop de Qt y asegurar salida limpia del proceso
sys.exit(app.exec_())
```

---

## 2. Elementos Gráficos: Widgets y Layouts

### Widgets Comunes
Un *Widget* es cualquier elemento visual en la pantalla (botones, etiquetas, campos de texto, ventanas).
- `QLabel`: Mostrar texto o imágenes.
  - Para mostrar una imagen: `label.setPixmap(QPixmap("ruta/a/imagen.png"))`.
- `QPushButton`: Un botón clásico cliqueable.
- `QLineEdit`: Campo de entrada de texto de una sola línea.

### Layouts (Administradores de Diseño)
En lugar de posicionar elementos con coordenadas fijas (coordenadas absolutas que se rompen al redimensionar la ventana), se utilizan Layouts para distribuir los widgets de forma adaptativa y automática.

- `QVBoxLayout`: Apila widgets verticalmente.
- `QHBoxLayout`: Apila widgets horizontalmente.
- `QGridLayout`: Organiza widgets en una grilla de filas y columnas.

```python
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self):
        # Crear widgets
        self.etiqueta = QLabel("Hola, ingresa tus datos:", self)
        self.boton = QPushButton("Enviar", self)

        # Crear layout vertical y añadir widgets
        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta)
        layout.addWidget(self.boton)

        # Asignar el layout a la ventana
        self.setLayout(layout)
        self.setWindowTitle("Ejemplo Layouts")
```

---

## 3. Señales y Slots

Las **señales** y **slots** son el mecanismo central de comunicación de Qt para responder a eventos (clics, ingresos de texto, temporizadores).
- **Señal**: Evento que emite un objeto (e.g., clic de un botón, cambio de texto).
- **Slot**: Método o función que se ejecuta en respuesta a una señal.

```python
# Conectar la señal clicked del botón a un método personalizado (slot)
self.boton.clicked.connect(self.procesar_clic)

def procesar_clic(self):
    self.etiqueta.setText("¡Botón presionado!")
```

### Identificar al Emisor (`sender()`)
Si múltiples widgets se conectan al mismo slot, se puede identificar cuál de ellos emitió la señal usando `self.sender()`:
```python
def slot_compartido(self):
    boton_presionado = self.sender()
    print(f"Presionaron el botón: {boton_presionado.text()}")
```

### Señales Personalizadas (`pyqtSignal`)
Podemos crear eventos propios para transmitir datos entre objetos. **Importante**: Las señales personalizadas deben declararse siempre como **atributos de clase** de clases que hereden de `QObject` o de algún `QWidget`.

```python
from PyQt5.QtCore import pyqtSignal, QObject

class EmisorDeMensajes(QObject):
    # Definición de señal que transmite un string y un entero
    senal_notificacion = pyqtSignal(str, int)

    def enviar(self):
        # Emitir la señal con los argumentos requeridos
        self.senal_notificacion.emit("Usuario registrado", 200)
```

---

## 4. Eventos de Ventana y Entrada

PyQt permite capturar interacciones de bajo nivel sobreescribiendo métodos especiales de la ventana:

### Eventos de Mouse
- `mousePressEvent(self, event)`: Se ejecuta al presionar un botón del mouse.
- `mouseReleaseEvent(self, event)`: Se ejecuta al soltar un botón del mouse.
- `mouseMoveEvent(self, event)`: Se ejecuta al mover el mouse. **Nota**: Por defecto, solo captura movimientos si se mantiene presionado un botón. Para capturarlo en todo momento, se debe llamar a `self.setMouseTracking(True)` en la inicialización de la ventana.

```python
from PyQt5.QtCore import Qt

def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
        x = event.x()
        y = event.y()
        print(f"Clic izquierdo en coordenadas: ({x}, {y})")
```

### Eventos de Teclado
- `keyPressEvent(self, event)`: Se ejecuta al presionar una tecla.
```python
def keyPressEvent(self, event):
    if event.key() == Qt.Key_Escape:
        self.close()  # Cierra la ventana si se presiona Escape
```

---

## 5. Arquitectura y Desacoplamiento Front-end / Back-end

Una regla de oro en el diseño de software interactivo es separar la interfaz gráfica de usuario (Front-end) de la lógica interna de la aplicación (Back-end).

- **Front-end**: Construye los widgets, define layouts y captura interacciones directas del usuario. **No debe procesar datos pesados, ni lógica de juegos, ni reglas de negocio.**
- **Back-end**: Implementa la lógica algorítmica y procesamiento de datos. **No debe importar nada de PyQt5 ni manipular widgets de interfaz.**

### Comunicación Bidireccional
1. **De Front-end a Back-end**: El Front-end tiene una referencia al Back-end y llama a sus métodos directamente ante eventos de usuario (e.g. `self.backend.validar_jugada(x, y)`).
2. **De Back-end a Front-end**: El Back-end **no conoce** al Front-end. Para enviarle respuestas o cambios de estado, el Back-end debe definir y **emitir señales personalizadas (`pyqtSignal`)**. El Front-end conecta esas señales a métodos encargados de actualizar la visualización.

```
┌────────────────┐                    ┌────────────────┐
│   FRONT-END    │ ───Llamado Dir.──> │    BACK-END    │
│  (PyQt5 GUI)   │ <───pyqtSignal──── │ (Pure Python)  │
└────────────────┘                    └────────────────┘
```

---

## 6. Conexión y Control de Múltiples Ventanas

Para evitar cierres instantáneos e inconsistencias al saltar entre ventanas (por ejemplo, del menú principal a la pantalla del juego):
- Se debe evitar que una ventana instancie y muestre directamente a la otra de manera fuertemente acoplada.
- Se recomienda implementar una clase **Controladora** (Controller) que orqueste la visibilidad y conecte las señales de ambas ventanas.

```python
class VentanaLogin(QWidget):
    senal_login_exitoso = pyqtSignal(str)
    # ... al validar credenciales, hace: self.senal_login_exitoso.emit(usuario)

class VentanaJuego(QWidget):
    # ... define la ventana principal del juego

class Controlador:
    def __init__(self):
        self.login = VentanaLogin()
        self.juego = VentanaJuego()
        
        # Conectar señales
        self.login.senal_login_exitoso.connect(self.mostrar_juego)

    def iniciar(self):
        self.login.show()

    def mostrar_juego(self, usuario):
        self.login.close()
        self.juego.setWindowTitle(f"Juego - {usuario}")
        self.juego.show()
```
