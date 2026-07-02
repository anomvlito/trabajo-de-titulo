"""
Ejemplo Práctico Complementario - Semana 8: Concurrencia y Multihilo
Tema: Simulador de Gestor de Descargas Concurrentes

Este script demuestra los siguientes conceptos de concurrencia:
1. threading.Thread: Ejecución asíncrona de múltiples trabajadores.
2. queue.Queue: Comunicación segura entre hilos usando el patrón Productor-Consumidor.
3. threading.Lock: Sincronización de acceso a una variable compartida (total de bytes descargados).
4. threading.Event: Coordinación colectiva de hilos para implementar las acciones
   de Pausar / Reanudar descargas en tiempo de ejecución.
"""

import queue
import threading
import time
import random

# --- 1. Definición de Recursos Compartidos ---

# Cola segura para la comunicación Productor-Consumidor
cola_descargas = queue.Queue()

# Lock para proteger el acceso de escritura al contador de bytes descargados
lock_contador = threading.Lock()
total_bytes_descargados = 0

# Evento para pausar/reanudar todos los hilos trabajadores simultáneamente.
# Si el evento está seteado (True), los trabajadores continúan.
# Si el evento está limpio (False), los trabajadores se bloquean hasta que se setee de nuevo.
evento_control_pausa = threading.Event()
evento_control_pausa.set()  # Iniciar en True (permitir descarga inmediata)

# Evento para indicar a los hilos trabajadores que deben terminar su ejecución de forma limpia.
evento_terminar = threading.Event()


# --- 2. Hilo Trabajador (Consumer) ---

class TrabajadorDescarga(threading.Thread):
    def __init__(self, id_worker: int):
        super().__init__()
        self.id_worker = id_worker
        # Marcamos el hilo como daemon para que termine automáticamente al cerrarse el hilo principal
        self.daemon = True

    def run(self):
        print(f"[Worker-{self.id_worker}] Iniciado y esperando tareas...")
        
        while not evento_terminar.is_set():
            try:
                # Intentar obtener una tarea de la cola.
                # timeout=0.5 evita que se quede bloqueado permanentemente y revise periódicamente 'evento_terminar'.
                archivo_id, tamaño_esperado = cola_descargas.get(timeout=0.5)
            except queue.Empty:
                # No hay tareas de momento, volver a evaluar el bucle
                continue
            
            print(f"[Worker-{self.id_worker}] Comenzando a descargar {archivo_id} ({tamaño_esperado} MB)...")
            bytes_bajados_archivo = 0
            
            # Simulamos la descarga en partes (chunks)
            while bytes_bajados_archivo < tamaño_esperado:
                # 1. Verificar si se solicitó terminar el hilo inmediatamente
                if evento_terminar.is_set():
                    print(f"[Worker-{self.id_worker}] Descarga cancelada a la mitad para {archivo_id}.")
                    cola_descargas.task_done()
                    return
                
                # 2. Coordinación de Pausa: esperar si evento_control_pausa está en False.
                # Si está pausado, se bloquea aquí hasta que se llame a evento_control_pausa.set()
                if not evento_control_pausa.is_set():
                    print(f"[Worker-{self.id_worker}] Pausado. Esperando reanudación...")
                    evento_control_pausa.wait()
                    print(f"[Worker-{self.id_worker}] Reanudando descarga de {archivo_id}...")

                # Simular tiempo de descarga de un chunk
                time.sleep(0.2)
                chunk_descarga = min(random.randint(10, 30), tamaño_esperado - bytes_bajados_archivo)
                bytes_bajados_archivo += chunk_descarga
                
                # 3. Actualización de Contador Compartido de forma segura usando el Lock
                with lock_contador:
                    global total_bytes_descargados
                    total_bytes_descargados += chunk_descarga

            print(f"[Worker-{self.id_worker}] ¡Descarga EXITOSA! {archivo_id} finalizado.")
            # Notificar a la cola que la tarea fue procesada por completo
            cola_descargas.task_done()


# --- 3. Ejecución del Programa Principal (Producer y Controlador) ---

if __name__ == "__main__":
    print("--- 1. Inicializando Hilos Trabajadores ---")
    NUM_WORKERS = 3
    trabajadores = []
    for idx in range(1, NUM_WORKERS + 1):
        worker = TrabajadorDescarga(idx)
        trabajadores.append(worker)
        worker.start()

    print("\n--- 2. Encolando Tareas de Descarga (Productor) ---")
    archivos_por_descargar = [
        ("FotoVacaciones.png", 50),
        ("InstaladorIDE.tar.gz", 120),
        ("BaseDatosClientes.db", 200),
        ("MusicaFavorita.mp3", 40),
        ("DocumentoGuia.pdf", 30)
    ]
    
    for nombre, size in archivos_por_descargar:
        print(f"[Producer] Encolando: {nombre} ({size} MB)")
        cola_descargas.put((nombre, size))

    print(f"\n[Sistema] Cola cargada con {cola_descargas.qsize()} descargas pendientes.")
    time.sleep(1.0) # Permitir que los hilos comiencen a procesar

    # --- 3. Demostración de Control de Flujo con Event (Pausar y Reanudar) ---
    print("\n--- 3. Demostrando Control de Flujo (Pausa de Descargas) ---")
    print("[Controlador] ¡Pausando descargas de forma colectiva!")
    evento_control_pausa.clear()  # Limpia el evento (False). Los hilos pausarán en el siguiente ciclo.
    
    time.sleep(1.5)  # Esperar un momento en estado de pausa
    
    # Imprimir estadísticas protegidas con Lock
    with lock_contador:
        print(f"[Métricas] Total descargado hasta la pausa: {total_bytes_descargados} MB")

    print("\n[Controlador] ¡Reanudando descargas!")
    evento_control_pausa.set()  # Setea el evento (True). Los hilos se desbloquean y continúan.

    # --- 4. Esperar finalización de la Cola ---
    print("\n--- 4. Esperando a que finalicen todas las descargas pendientes ---")
    # cola_descargas.join() bloquea el hilo principal hasta que task_done() se haya llamado para cada tarea
    cola_descargas.join()
    
    # Detener hilos de forma limpia
    evento_terminar.set()
    
    print("\n--- 5. Resumen Final de Descargas ---")
    with lock_contador:
        print(f"- Total de datos descargados con éxito: {total_bytes_descargados} MB")
    print("- Estado de la cola de descargas: Vacía (Todas completadas).")
    print("[Sistema] Programa finalizado de manera limpia.")
