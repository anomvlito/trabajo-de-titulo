"""
Ejemplo Práctico Complementario - Semana 7: Programación Funcional e itertools
Tema: Procesamiento de Métricas y Analíticas de Usuario

Este script demuestra los siguientes conceptos funcionales:
1. Funciones Puras e Inmutabilidad.
2. Funciones de Orden Superior: map, filter, reduce.
3. Generador Interactivo (Corrutina): Utiliza yield y el método send() para
   calcular estadísticas acumuladas en tiempo real.
4. Herramientas de Iteración (itertools):
   - itertools.chain: Para fusionar múltiples fuentes de logs.
   - itertools.groupby: Para agrupar logs por tipo.
   - itertools.combinations: Para analizar pares de páginas visitadas por un usuario.
"""

from functools import reduce
import itertools

# --- 1. Definición de Datos de Prueba (Inmutables por convención) ---

LOGS_MAÑANA = [
    {"usuario": "alice", "evento": "click_boton", "timestamp": "09:15", "valor": 10},
    {"usuario": "bob", "evento": "vista_pagina", "timestamp": "09:30", "valor": 1},
    {"usuario": "alice", "evento": "vista_pagina", "timestamp": "09:45", "valor": 1}
]

LOGS_TARDE = [
    {"usuario": "alice", "evento": "compra", "timestamp": "14:20", "valor": 150},
    {"usuario": "charlie", "evento": "vista_pagina", "timestamp": "15:00", "valor": 1},
    {"usuario": "bob", "evento": "click_boton", "timestamp": "16:15", "valor": 12}
]


# --- 2. Programación Funcional Clásica (map, filter, reduce) ---

def es_vista_pagina(log: dict) -> bool:
    """Función pura: Verifica si el evento es una vista de página."""
    return log["evento"] == "vista_pagina"


def obtener_usuario(log: dict) -> str:
    """Función pura: Extrae el nombre de usuario de un log."""
    return log["usuario"]


# --- 3. Generador Avanzado con send() ---

def acumulador_promedio():
    """
    Generador que actúa como un acumulador de promedio móvil.
    Recibe valores usando send(), calcula el promedio y lo devuelve en el yield.
    """
    total = 0.0
    conteo = 0
    promedio = 0.0
    
    # El primer yield es para inicializar la corrutina
    valor_recibido = yield promedio
    
    while True:
        if valor_recibido is not None:
            total += valor_recibido
            conteo += 1
            promedio = total / conteo
        # Retorna el promedio actual y espera el siguiente valor vía send()
        valor_recibido = yield promedio


# --- 4. Ejecución del Procesamiento de Datos ---

if __name__ == "__main__":
    print("--- 1. Fusión de Flujos usando itertools.chain ---")
    # chain une múltiples iterables de forma eficiente sin crear listas temporales grandes en memoria
    flujo_completo = list(itertools.chain(LOGS_MAÑANA, LOGS_TARDE))
    for log in flujo_completo:
        print(f"  {log}")

    print("\n--- 2. Filtrado y Transformación Funcional (map/filter) ---")
    # Filtrar solo vistas de página y obtener los usuarios asociados de forma funcional
    paginas_vistas = filter(es_vista_pagina, flujo_completo)
    usuarios_interesados = map(obtener_usuario, paginas_vistas)
    print(f"  Usuarios que vieron páginas: {list(usuarios_interesados)}")

    print("\n--- 3. Reducción de Datos (functools.reduce) ---")
    # Calcular el valor total acumulado de todos los eventos
    # Usamos una función lambda para sumar el acumulador con el valor de cada diccionario
    valor_total = reduce(lambda acumulado, log: acumulado + log["valor"], flujo_completo, 0.0)
    print(f"  Suma total de valor de eventos procesados: {valor_total}")

    print("\n--- 4. Agrupamiento con itertools.groupby ---")
    # groupby requiere que los datos de entrada estén ordenados por la clave de agrupación
    clave_ordenamiento = lambda log: log["evento"]
    flujo_ordenado = sorted(flujo_completo, key=clave_ordenamiento)
    
    agrupado = itertools.groupby(flujo_ordenado, key=clave_ordenamiento)
    for clave, grupo in agrupado:
        # grupo es un iterador de un solo uso
        lista_grupo = list(grupo)
        print(f"  Evento: {clave:<15} | Cantidad: {len(lista_grupo)} | Elementos: {[x['usuario'] for x in lista_grupo]}")

    print("\n--- 5. Análisis de Combinaciones de Comportamiento (itertools.combinations) ---")
    # Obtener todas las combinaciones posibles de 2 eventos de Alice
    eventos_alice = list(filter(lambda log: log["usuario"] == "alice", flujo_completo))
    nombres_eventos_alice = [log["evento"] for log in eventos_alice]
    
    # combinations genera tuplas únicas sin repetir elementos en distinta posición
    pares_eventos = list(itertools.combinations(nombres_eventos_alice, 2))
    print(f"  Eventos de Alice en el día: {nombres_eventos_alice}")
    print(f"  Pares posibles de eventos de Alice (sin importar orden):")
    for par in pares_eventos:
        print(f"    - {par[0]} con {par[1]}")

    print("\n--- 6. Generador Cooperativo con Control de Entrada (yield / send) ---")
    # Inicializar el acumulador
    promediador = acumulador_promedio()
    # Primera llamada a next() o send(None) para avanzar el generador hasta el primer yield
    next(promediador)
    
    # Enviar valores dinámicos
    valores_simulados = [10.0, 20.0, 30.0, 5.0]
    print("  Enviando valores secuenciales al generador:")
    for val in valores_simulados:
        # send() inyecta el valor en el yield del generador y retorna el nuevo promedio calculado
        promedio_actual = promediador.send(val)
        print(f"    Valor enviado: {val:>4} | Promedio Móvil Retornado: {promedio_actual:.2f}")
