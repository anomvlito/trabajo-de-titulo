"""
Ejemplo Práctico Complementario - Semana 6: Excepciones e Iteradores
Tema: Analizador Inteligente de Archivos de Logs

Este script integra los siguientes conceptos:
1. Excepciones Personalizadas: Captura y tipificación de errores de formato y dominio.
2. try-except-else-finally: Control detallado del flujo al parsear cadenas problemáticas.
3. Iterador Personalizado: Clase que recorre las líneas de un log de forma perezosa.
4. Lista Ligada e Iterador Asociado: Almacena en memoria de forma encadenada los
   mensajes críticos detectados durante la iteración.
"""

# --- 1. Definición de Excepciones Personalizadas ---

class FormatoLogInvalidoError(Exception):
    """Levantada cuando una línea de log no sigue el patrón esperado (campos faltantes)."""
    def __init__(self, linea: str, n_linea: int):
        self.linea = linea
        self.n_linea = n_linea
        super().__init__(f"Línea {n_linea} no contiene el formato esperado: '{linea.strip()}'")


class NivelLogInvalidoError(Exception):
    """Levantada cuando el nivel del log no corresponde a INFO, WARNING, ERROR o CRITICAL."""
    def __init__(self, nivel: str, n_linea: int):
        self.nivel = nivel
        self.n_linea = n_linea
        super().__init__(f"Nivel de log '{nivel}' desconocido en línea {n_linea}.")


# --- 2. Nodo y Lista Ligada para almacenar errores severos ---

class NodoLog:
    def __init__(self, timestamp: str, nivel: str, mensaje: str):
        self.timestamp = timestamp
        self.nivel = nivel
        self.mensaje = mensaje
        self.siguiente = None


class IteradorErrores:
    """Iterador que recorre secuencialmente los nodos de la ListaLigadaErrores."""
    def __init__(self, cabeza: NodoLog):
        self.actual = cabeza

    def __iter__(self):
        return self

    def __next__(self) -> NodoLog:
        if not self.actual:
            raise StopIteration
        nodo = self.actual
        self.actual = self.actual.siguiente
        return nodo


class ListaLigadaErrores:
    """Estructura encadenada para almacenar registros críticos del log."""
    def __init__(self):
        self.cabeza = None

    def agregar(self, timestamp: str, nivel: str, mensaje: str):
        nuevo_nodo = NodoLog(timestamp, nivel, mensaje)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        
        # Insertar al final
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def __iter__(self):
        return IteradorErrores(self.cabeza)


# --- 3. Iterable e Iterador de Logs (LectorLogs) ---

class LectorLogs:
    """
    Iterable que toma un string multilínea y retorna un iterador para 
    procesar las líneas una por una, convirtiéndolas en diccionarios estructurados.
    """
    NIVELES_VALIDOS = {"INFO", "WARNING", "ERROR", "CRITICAL"}

    def __init__(self, datos_logs: str):
        self.lineas = datos_logs.strip().split("\n")
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        """Parsea y retorna la siguiente línea válida, o levanta excepciones si hay errores."""
        if self.indice >= len(self.lineas):
            raise StopIteration
        
        linea = self.lineas[self.indice]
        n_linea = self.indice + 1
        self.indice += 1
        
        # Un formato correcto debe ser: TIMESTAMP|NIVEL|MENSAJE
        partes = linea.split("|")
        if len(partes) != 3:
            raise FormatoLogInvalidoError(linea, n_linea)
            
        timestamp, nivel, mensaje = partes
        nivel = nivel.strip().upper()
        
        if nivel not in self.NIVELES_VALIDOS:
            raise NivelLogInvalidoError(nivel, n_linea)
            
        return timestamp.strip(), nivel, mensaje.strip()


# --- 4. Flujo de Simulación y Pruebas ---

# Datos simulados con algunas líneas corruptas a propósito para probar excepciones
LOGS_MOCK = """
2026-05-27 12:00:01|INFO|Sistema iniciado correctamente
2026-05-27 12:01:15|WARNING|Uso de disco cercano al 85%
Línea corrupta que va a fallar aquí sin formato correcto
2026-05-27 12:02:40|DEBUG|Intento de login con nivel no estándar
2026-05-27 12:03:00|ERROR|Error de conexión con base de datos
2026-05-27 12:04:12|CRITICAL|Fallo de energía en servidor de respaldo
"""

if __name__ == "__main__":
    lector = LectorLogs(LOGS_MOCK)
    lista_critica = ListaLigadaErrores()
    
    lineas_procesadas = 0
    lineas_invalidas = 0
    
    print("--- Iniciando Análisis de Logs (Iteración Perezosa) ---")
    
    # Recorrer el iterable usando el protocolo estándar
    while True:
        try:
            # Obtener el siguiente elemento procesado
            timestamp, nivel, mensaje = next(lector)
            
        except StopIteration:
            # Fin del flujo limpio
            break
            
        except FormatoLogInvalidoError as err:
            lineas_invalidas += 1
            print(f"[RECHAZADO] Error de Formato en línea {err.n_linea}: {err}")
            
        except NivelLogInvalidoError as err:
            lineas_invalidas += 1
            print(f"[RECHAZADO] Nivel Invalido en línea {err.n_linea}: {err}")
            
        else:
            # Se ejecuta si no se levantó ninguna excepción
            lineas_procesadas += 1
            print(f"[OK - {nivel}] {timestamp}: {mensaje}")
            
            # Si el nivel es ERROR o CRITICAL, lo guardamos en la estructura encadenada
            if nivel in {"ERROR", "CRITICAL"}:
                lista_critica.agregar(timestamp, nivel, mensaje)
                
        finally:
            # Se ejecuta al final de cada ciclo del análisis
            # Excelente para llevar métricas o depurar
            pass

    print("\n--- Resultados del Análisis ---")
    print(f"- Líneas analizadas con éxito: {lineas_procesadas}")
    print(f"- Líneas corruptas ignoradas: {lineas_invalidas}")

    print("\n--- Registros Críticos Almacenados en la Lista Ligada ---")
    # Recorrer la lista ligada usando su iterador dedicado
    for error_nodo in lista_critica:
        print(f"[{error_nodo.nivel}] en {error_nodo.timestamp} -> {error_nodo.mensaje}")
