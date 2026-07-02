# Semana 10: Serialización JSON y Servicios Web (APIs)

Este documento detalla los conceptos de serialización orientada a texto (JSON), conceptos básicos de redes de computadores, y el desarrollo de servicios web (cliente y servidor HTTP) para la semana 10 de **Programación Avanzada**.

---

## 1. Serialización JSON en Python

La serialización es el proceso de convertir un objeto en memoria a un formato de almacenamiento o transmisión (en este caso, una cadena de texto en formato JSON).

### Operaciones Básicas
- **Serializar**: `json.dumps(objeto)` (retorna string) o `json.dump(objeto, archivo)` (escribe en archivo).
- **Deserializar**: `json.loads(string_json)` (retorna objeto Python) o `json.load(archivo)` (lee desde archivo).

### Serialización de Objetos Personalizados
Por defecto, el módulo `json` solo admite tipos nativos (`dict`, `list`, `str`, `int`, `float`, `bool`, `None`). Si intentamos serializar una instancia de una clase propia, arrojará `TypeError`.

#### Personalización con `JSONEncoder`
Para solucionarlo, definimos una clase que hereda de `json.JSONEncoder` y sobreescribimos el método `default(self, o)`:

```python
import json

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

class PersonaEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Persona):
            # Retorna una representación en diccionario compatible con JSON
            return {"nombre": o.nombre, "edad": o.edad, "__class__": "Persona"}
        # Delegar el comportamiento al encoder base para otros tipos
        return super().default(o)

# Uso:
p = Persona("Diego", 22)
string_json = json.dumps(p, cls=PersonaEncoder)
# '{"nombre": "Diego", "edad": 22, "__class__": "Persona"}'
```

#### Deserialización Personalizada con `object_hook`
Para recuperar el objeto original al deserializar, pasamos una función decodificadora al parámetro `object_hook`:

```python
def persona_decoder(dct):
    if "__class__" in dct and dct["__class__"] == "Persona":
        return Persona(dct["nombre"], dct["edad"])
    return dct

# Uso:
objeto_recuperado = json.loads(string_json, object_hook=persona_decoder)
print(type(objeto_recuperado))  # <class '__main__.Persona'>
```

---

## 2. Conceptos de Redes y Arquitectura Cliente-Servidor

- **Dirección IP**: Identificador único numérico asignado a cada dispositivo en una red.
- **Puerto**: Identificador numérico lógico (0 a 65535) asociado a un proceso o aplicación específica en un computador.
- **Arquitectura Cliente-Servidor**: 
  - El **Servidor** escucha peticiones en un puerto específico de forma pasiva.
  - El **Cliente** inicia la comunicación de forma activa conectándose al puerto del servidor.

---

## 3. Web Services e HTTP

Un **Servicio Web** es una aplicación diseñada para comunicarse mediante la web (usando típicamente el protocolo **HTTP**).

### Peticiones HTTP
Toda petición contiene:
1. **URL**: La ruta o dirección del recurso.
2. **Método (Verbo)**: 
   - `GET`: Solicitar datos al servidor.
   - `POST`: Enviar datos nuevos para crear o procesar un recurso.
3. **Headers**: Metadatos (autenticación, tipo de contenido).
4. **Body (Cuerpo)**: Carga útil de datos (típico en peticiones POST).

### Códigos de Respuesta Comunes
- `200 OK` / `201 Created`: Éxito.
- `400 Bad Request`: Petición mal estructurada.
- `401 Unauthorized` / `403 Forbidden`: Problemas de permisos/credenciales.
- `404 Not Found`: Recurso inexistente.
- `429 Too Many Requests`: Límite de peticiones excedido (Rate limiting).
- `500 Internal Server Error`: Falla interna en el código del servidor.

---

## 4. Consumo de APIs en Python (Cliente HTTP)

Se utiliza la librería externa `requests`.

```python
import requests

# 1. Petición GET con parámetros
url = "https://api.ejemplo.com/usuarios"
parametros = {"rol": "admin", "activo": "true"}
headers = {"Authorization": "Bearer token123"}

response = requests.get(url, params=parametros, headers=headers)

if response.status_code == 200:
    datos = response.json()  # Parsea directamente la respuesta JSON
    print(datos)

# 2. Petición POST enviando JSON en el cuerpo
payload = {"nombre": "Sofía", "edad": 25}
response_post = requests.post(url, json=payload)
print(response_post.status_code)  # e.g., 201
```

---

## 5. Creación de Servicios Web (Servidor HTTP con Flask)

`Flask` es un microframework minimalista en Python para levantar servidores web y APIs.

### Ejemplo Completo de API en Flask
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada
usuarios = {
    1: {"nombre": "Alicia", "rol": "usuario"},
    2: {"nombre": "Carlos", "rol": "admin"}
}

# 1. Endpoint GET clásico
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    # Retorna JSON con estado HTTP 200 por defecto
    return jsonify(usuarios)

# 2. Endpoint GET con parámetros dinámicos en URL
@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):
    if usuario_id not in usuarios:
        # Retorna mensaje de error y código 404
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuarios[usuario_id])

# 3. Endpoint POST recibiendo JSON en el cuerpo
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    # Obtener el JSON enviado en el body
    datos = request.get_json()
    if not datos or "nombre" not in datos:
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    nuevo_id = max(usuarios.keys()) + 1
    usuarios[nuevo_id] = {"nombre": datos["nombre"], "rol": datos.get("rol", "usuario")}
    
    return jsonify({"id": nuevo_id, "usuario": usuarios[nuevo_id]}), 201

if __name__ == '__main__':
    # Levanta el servidor local en el puerto 5000
    app.run(port=5000, debug=True)
```
