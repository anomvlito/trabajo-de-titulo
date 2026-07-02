"""
Ejemplo Práctico Complementario - Semana 3: Estructuras de Datos
Tema: Simulación de Gestión de Inventario y Procesamiento de Órdenes (FIFO)

Este script integra las siguientes estructuras y conceptos:
1. `namedtuple`: Para la representación inmutable de productos.
2. `deque`: Como cola FIFO para procesar transacciones en orden de llegada.
3. `defaultdict`: Para agrupar ventas e inventarios por categoría de producto sin inicialización manual.
4. `set`: Para mantener un registro de clientes únicos que realizaron compras.
5. `*args` y `**kwargs`: Para una función utilitaria de logs formateados.
"""

from collections import namedtuple, deque, defaultdict

# 1. Definición de la estructura inmutable Producto usando namedtuple
# Representa un producto en catálogo con ID, nombre, precio y categoría.
Producto = namedtuple("Producto", ["sku", "nombre", "precio", "categoria"])

# 2. Catálogo de productos disponibles
CATALOGO = {
    "SKU-100": Producto("SKU-100", "Laptop Gamer", 1200.0, "Electrónica"),
    "SKU-101": Producto("SKU-101", "Mouse Inalámbrico", 35.0, "Electrónica"),
    "SKU-200": Producto("SKU-200", "Silla Ergonómica", 180.0, "Oficina"),
    "SKU-201": Producto("SKU-201", "Escritorio Elevable", 350.0, "Oficina"),
    "SKU-300": Producto("SKU-300", "Termo de Acero", 25.0, "Hogar")
}


# 3. Función utilitaria de logging dinámico (*args y **kwargs)
def registrar_log(nivel: str, *args, **kwargs):
    """
    Imprime un log formateado usando argumentos variables.
    *args: Mensajes o detalles secuenciales a imprimir.
    **kwargs: Pares clave-valor opcionales para metadatos del log.
    """
    mensajes_unidos = " | ".join(str(msg) for msg in args)
    metadatos = " - ".join(f"{k.upper()}: {v}" for k, v in kwargs.items())
    
    prefijo = f"[{nivel.upper()}]"
    if metadatos:
        print(f"{prefijo:<10} {mensajes_unidos} ({metadatos})")
    else:
        print(f"{prefijo:<10} {mensajes_unidos}")


# 4. Clase orquestadora de la Tienda
class GestionTienda:
    def __init__(self):
        # Cola FIFO para procesar las órdenes pendientes
        self.cola_ordenes = deque()
        
        # Registro de stock por SKU (defaultdict(int) inicializa valores en 0 automáticamente)
        self.stock = defaultdict(int)
        
        # Registro de ingresos de dinero acumulados por categoría
        self.ventas_por_categoria = defaultdict(float)
        
        # Conjunto de IDs de clientes únicos que compraron con éxito
        self.clientes_unicos = set()

    def reabastecer(self, sku: str, cantidad: int):
        """Añade stock de un SKU específico."""
        if sku not in CATALOGO:
            registrar_log("warning", f"SKU {sku} no registrado en catálogo", accion="reabastecimiento")
            return
        
        self.stock[sku] += cantidad
        producto = CATALOGO[sku]
        registrar_log(
            "info", 
            f"Stock aumentado para {producto.nombre}", 
            sku=sku, 
            nuevo_stock=self.stock[sku]
        )

    def recibir_orden(self, cliente_id: str, sku: str, cantidad: int):
        """Registra una orden de compra en la cola de procesamiento FIFO."""
        if sku not in CATALOGO:
            registrar_log("error", f"Intento de compra de SKU inexistente: {sku}", cliente=cliente_id)
            return
        
        # Agregamos la orden al final de la cola (derecha)
        self.cola_ordenes.append((cliente_id, sku, cantidad))
        registrar_log("info", f"Orden encolada para cliente {cliente_id}", cola_largo=len(self.cola_ordenes))

    def procesar_siguiente_orden(self):
        """Procesa y extrae la orden más antigua de la cola (FIFO - desde la izquierda)."""
        if not self.cola_ordenes:
            registrar_log("info", "No hay órdenes pendientes en la cola.")
            return

        # Desencolar por el extremo izquierdo (FIFO)
        cliente_id, sku, cantidad = self.cola_ordenes.popleft()
        producto = CATALOGO[sku]
        
        # Verificar stock disponible
        stock_disponible = self.stock[sku]
        if stock_disponible >= cantidad:
            # Confirmar transacción
            self.stock[sku] -= cantidad
            total_venta = producto.precio * cantidad
            
            # Registrar acumulados
            self.ventas_por_categoria[producto.categoria] += total_venta
            self.clientes_unicos.add(cliente_id)
            
            registrar_log(
                "success",
                f"Venta PROCESADA con éxito",
                cliente=cliente_id,
                item=producto.nombre,
                cant=cantidad,
                total=f"${total_venta:.2f}"
            )
        else:
            # Rechazar por falta de stock
            registrar_log(
                "warning",
                f"Venta RECHAZADA: Stock insuficiente para {producto.nombre}",
                cliente=cliente_id,
                solicitado=cantidad,
                disponible=stock_disponible
            )

    def mostrar_resumen(self):
        """Imprime un informe del estado actual de la tienda."""
        print("\n" + "="*50)
        print("          RESUMEN DE GESTIÓN DE LA TIENDA")
        print("="*50)
        
        print("\n[Inventario Actual]")
        for sku, cant in self.stock.items():
            prod = CATALOGO[sku]
            print(f"- {prod.nombre} ({sku}): {cant} unidades disponibles.")

        print("\n[Venta Acumulada por Categoría]")
        for cat, total in self.ventas_por_categoria.items():
            print(f"- {cat}: ${total:.2f}")

        print("\n[Estadísticas de Clientes]")
        print(f"- Total de transacciones exitosas (clientes únicos): {len(self.clientes_unicos)}")
        print(f"- Lista de clientes compradores: {', '.join(sorted(self.clientes_unicos))}")
        print("="*50 + "\n")


# 5. Código de prueba para simulación
if __name__ == "__main__":
    tienda = GestionTienda()
    
    # Reabastecer la tienda
    print("--- 1. Fase de Reabastecimiento ---")
    tienda.reabastecer("SKU-100", 2)  # Laptop Gamer
    tienda.reabastecer("SKU-101", 10) # Mouse Inalámbrico
    tienda.reabastecer("SKU-300", 5)  # Termo de Acero
    
    # Llegada de clientes y generación de órdenes de compra
    print("\n--- 2. Llegada de Órdenes (Encolamiento) ---")
    tienda.recibir_orden("USR_ALICIA", "SKU-100", 1)  # Solicita 1 laptop
    tienda.recibir_orden("USR_BOB", "SKU-100", 2)     # Solicita 2 laptops (excederá stock)
    tienda.recibir_orden("USR_ALICIA", "SKU-101", 2)  # Solicita 2 mouses
    tienda.recibir_orden("USR_CARLOS", "SKU-300", 1)  # Solicita 1 termo
    
    # Procesamiento secuencial (FIFO)
    print("\n--- 3. Procesando Cola de Órdenes (FIFO) ---")
    tienda.procesar_siguiente_orden()  # Procesa Alicia (1 laptop) -> Éxito
    tienda.procesar_siguiente_orden()  # Procesa Bob (2 laptops) -> Falla (solo queda 1)
    tienda.procesar_siguiente_orden()  # Procesa Alicia (2 mouses) -> Éxito
    tienda.procesar_siguiente_orden()  # Procesa Carlos (1 termo) -> Éxito
    tienda.procesar_siguiente_orden()  # Intento de procesar con cola vacía
    
    # Mostrar resultados
    tienda.mostrar_resumen()
