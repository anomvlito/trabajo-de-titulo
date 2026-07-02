# Semana 11: Serialización Pickle, Bytes y Sockets (TCP/UDP)

Este documento detalla los conceptos de serialización orientada a bytes (Pickle), manipulación de bytes, y la implementación de sockets concurrentes (cliente/servidor) para la semana 11 de **Programación Avanzada**.

---

## 1. Serialización Pickle

A diferencia de JSON, `pickle` es un protocolo de serialización binario exclusivo de Python.

### Características y Comparativa
- **Formato**: Binario (`bytes`), no legible por humanos.
- **Soporte**: Admite casi cualquier objeto de Python (incluso referencias circulares, funciones y clases personalizadas) sin necesidad de configurar encoders complejos.
- **Seguridad**: **¡Advertencia Crítica!** Deserializar datos provenientes de fuentes no confiables con `pickle` es peligroso, ya que permite la ejecución de código arbitrario durante la reconstrucción del objeto.

### Personalización mediante `__getstate__` y `__setstate__`
Permite controlar qué atributos se guardan y cómo se restauran. Es ideal para omitir atributos que no se pueden serializar directamente (como conexiones a bases de datos o sockets abiertos):

```python
import pickle

class ClienteConexion:
    def __init__(self, ip: str, puerto: int):
        self.ip = ip
        self.puerto = puerto
        # El socket no es serializable
        self.conexion_socket = None 

    def __getstate__(self):
        # Retorna el estado que queremos serializar (excluyendo el socket)
        estado = self.__dict__.copy()
        if "conexion_socket" in estado:
            del estado["conexion_socket"]
        return estado

    def __setstate__(self, state):
        # Restaura el estado del objeto y recrea los atributos omitidos
        self.__dict__.update(state)
        self.conexion_socket = None  # Se inicializa vacío para reconexión
```

---

## 2. Manejo de Bytes en Python

El manejo de datos a bajo nivel requiere interactuar con secuencias de bytes utilizando los objetos `bytes` (inmutables) y `bytearray` (mutables).

### Conversiones Fundamentales
- **Strings a Bytes (y viceversa)**:
  - De texto a bytes: `bytes_obj = "Hola".encode("utf-8")`
  - De bytes a texto: `texto = bytes_obj.decode("utf-8")`
- **Enteros a Bytes (y viceversa)**:
  - De entero a bytes: `num.to_bytes(length_in_bytes, byteorder)`
  - De bytes a entero: `int.from_bytes(bytes_obj, byteorder)`
  - **`byteorder`**: Determina el orden de importancia de los bytes:
    - `'big'`: El byte más significativo va primero (Big-Endian).
    - `'little'`: El byte menos significativo va primero (Little-Endian).

```python
# Ejemplo de conversión de entero a 4 bytes Big-Endian
numero = 1024
num_bytes = numero.to_bytes(4, byteorder='big')  # b'\x00\x00\x04\x00'
numero_recuperado = int.from_bytes(num_bytes, byteorder='big')  # 1024
```

---

## 3. Sockets en Python

Un **socket** es un extremo de un canal de comunicación bidireccional entre dos procesos en una red.

### Sockets TCP (`SOCK_STREAM`)
Orientado a la conexión y confiable. Asegura que los datos lleguen completos, ordenados y sin errores.

#### Código Servidor TCP Básico
```python
import socket

host = "127.0.0.1"
puerto = 8000

# 1. Crear el socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Asociar a IP y puerto
server_socket.bind((host, puerto))

# 3. Escuchar conexiones entrantes
server_socket.listen()
print(f"Servidor escuchando en {host}:{puerto}...")

# 4. Aceptar conexión (Bloqueante)
client_socket, address = server_socket.accept()
print(f"Conexión establecida con {address}")

# 5. Recibir y enviar datos (siempre en bytes)
datos = client_socket.recv(1024)
mensaje = datos.decode("utf-8")
print(f"Recibido: {mensaje}")

client_socket.sendall("Mensaje recibido".encode("utf-8"))

# 6. Cerrar sockets
client_socket.close()
server_socket.close()
```

#### Código Cliente TCP Básico
```python
import socket

# 1. Crear el socket TCP y conectar al servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8000))

# 2. Enviar y recibir
client_socket.sendall("Hola servidor".encode("utf-8"))
respuesta = client_socket.recv(1024).decode("utf-8")
print(f"Servidor respondió: {respuesta}")

# 3. Cerrar
client_socket.close()
```

---

## 4. Protocolo de Envío de Datos (Resolviendo Fragmentación en TCP)

Dado que TCP es un protocolo basado en flujos de datos continuos (*stream-based*), no garantiza que un `send(mensaje)` corresponda exactamente a un `recv()`. Varios mensajes pueden juntarse o llegar en partes (fragmentación).

### Protocolo de Prefijo de Tamaño
Para delimitar los mensajes, la convención del curso es anteponer al mensaje una cabecera fija de **4 bytes** que contiene la longitud exacta (en bytes) del mensaje que viene a continuación.

```python
# --- EMISOR ---
def enviar_mensaje(socket_destino, mensaje_str: str):
    mensaje_bytes = mensaje_str.encode("utf-8")
    largo = len(mensaje_bytes)
    
    # Codificar el largo del mensaje en 4 bytes Big-Endian
    largo_bytes = largo.to_bytes(4, byteorder='big')
    
    # Enviar cabecera + cuerpo
    socket_destino.sendall(largo_bytes + mensaje_bytes)

# --- RECEPTOR ---
def recibir_mensaje(socket_origen) -> str:
    # 1. Leer los primeros 4 bytes para obtener el largo
    largo_bytes = socket_origen.recv(4)
    if not largo_bytes:
        return ""
    largo = int.from_bytes(largo_bytes, byteorder='big')
    
    # 2. Leer exactamente 'largo' bytes (iterando si llega fragmentado)
    bytes_recibidos = bytearray()
    while len(bytes_recibidos) < largo:
        falta = largo - len(bytes_recibidos)
        chunk = socket_origen.recv(min(falta, 4096))
        if not chunk:
            break
        bytes_recibidos.extend(chunk)
        
    return bytes_recibidos.decode("utf-8")
```

---

## 5. Servidores Concurrentes (Multi-cliente con Threading)

Un servidor real debe poder interactuar con múltiples clientes al mismo tiempo de forma concurrente, evitando quedar bloqueado en el `recv` o `accept` de un solo cliente.

```python
import socket
import threading

class ServidorConcurrente:
    def __init__(self, host: str, puerto: int):
        self.host = host
        self.puerto = puerto
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def iniciar(self):
        self.socket_servidor.bind((self.host, self.puerto))
        self.socket_servidor.listen()
        print(f"Servidor concurrente iniciado en {self.host}:{self.puerto}")
        
        while True:
            # Aceptar una nueva conexión
            conn, addr = self.socket_servidor.accept()
            print(f"Nuevo cliente conectado desde: {addr}")
            
            # Lanzar un hilo independiente para manejar al cliente
            hilo = threading.Thread(
                target=self.manejar_cliente, 
                args=(conn, addr), 
                daemon=True
            )
            hilo.start()

    def manejar_cliente(self, conn, addr):
        try:
            while True:
                # Usar protocolo de lectura
                datos = conn.recv(1024)
                if not datos:
                    break
                print(f"Cliente {addr} dice: {datos.decode('utf-8')}")
                conn.sendall(b"OK")
        except ConnectionResetError:
            print(f"Cliente {addr} desconectado abruptamente.")
        finally:
            conn.close()
            print(f"Conexión con {addr} cerrada.")

if __name__ == '__main__':
    server = ServidorConcurrente("127.0.0.1", 8000)
    server.iniciar()
```
