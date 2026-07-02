"""
Ejemplo Práctico Complementario - Semana 4: OOP Avanzado
Tema: Simulación de Sistema de Combate RPG (Juego de Rol)

Este script integra los siguientes conceptos avanzados:
1. `abc.ABC` y `@abstractmethod`: Clase base abstracta para entidades de combate.
2. Multiherencia Cooperativa: Resolución del problema del diamante con Guerrero, Mago y Paladín.
3. Métodos Dunder (Sobrecarga de Operadores): `__repr__`, `__add__` y `__gt__`.
4. Decoradores: Decorador personalizado para registrar las acciones de combate.
"""

from abc import ABC, abstractmethod


# 1. Decorador para registrar acciones de combate
def log_accion(funcion):
    """
    Decorador que envuelve un método de combate para imprimir los detalles
    del evento de forma formateada antes de ejecutar la acción.
    """
    def wrapper(self, *args, **kwargs):
        nombre_accion = funcion.__name__.replace("_", " ").title()
        print(f"[COMBATE] {self.nombre} inicia la acción: '{nombre_accion}'")
        resultado = funcion(self, *args, **kwargs)
        return resultado
    return wrapper


# 2. Clase Abstracta Base (ABC)
class EntidadCombate(ABC):
    """
    Representa cualquier entidad que pueda entrar en combate.
    Define la estructura obligatoria que deben implementar sus subclases.
    """
    def __init__(self, nombre: str, vida: int, **kwargs):
        # super().__init__() en multiherencia cooperativa pasa los argumentos
        # sobrantes al siguiente constructor en el MRO.
        super().__init__(**kwargs)
        self.nombre = nombre
        self.vida = vida

    @abstractmethod
    def atacar(self) -> int:
        """Calcula y retorna el daño infligido."""
        pass

    @abstractmethod
    def recibir_daño(self, cantidad: int):
        """Aplica la reducción de salud correspondiente."""
        pass


# 3. Clases base de la herencia del diamante
class Personaje(EntidadCombate):
    """
    Clase base para personajes jugables.
    Añade un nivel al personaje.
    """
    def __init__(self, nivel: int, **kwargs):
        super().__init__(**kwargs)
        self.nivel = nivel

    def atacar(self) -> int:
        # Ataque básico proporcional al nivel
        return self.nivel * 5

    def recibir_daño(self, cantidad: int):
        self.vida = max(0, self.vida - cantidad)
        print(f"-> {self.nombre} recibió {cantidad} de daño. Vida restante: {self.vida}")

    # Sobrecarga del operador Mayor Que (>) para comparar niveles
    def __gt__(self, otro):
        if not isinstance(otro, Personaje):
            return NotImplemented
        return self.nivel > otro.nivel

    # Sobrecarga del operador Suma (+) para fusionar fuerzas
    def __add__(self, otro):
        if not isinstance(otro, Personaje):
            return NotImplemented
        nuevo_nombre = f"Fusión de {self.nombre} y {otro.nombre}"
        nueva_vida = self.vida + otro.vida
        nuevo_nivel = self.nivel + otro.nivel
        # Retorna una nueva instancia de Personaje (Fusión básica)
        return Personaje(nombre=nuevo_nombre, vida=nueva_vida, nivel=nuevo_nivel)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(Nombre: {self.nombre}, Nivel: {self.nivel}, Vida: {self.vida})"


class Guerrero(Personaje):
    """
    Especialización de Guerrero. Añade el atributo fuerza física.
    """
    def __init__(self, fuerza: int, **kwargs):
        # Envía los kwargs al constructor de Personaje
        super().__init__(**kwargs)
        self.fuerza = fuerza

    @log_accion
    def atacar(self) -> int:
        # El daño del guerrero depende del ataque base y su fuerza
        daño_base = super().atacar()
        daño_guerrero = daño_base + (self.fuerza * 2)
        print(f"  [Guerrero] ¡Golpe de Espada! Daño físico calculado: {daño_guerrero}")
        return daño_guerrero


class Mago(Personaje):
    """
    Especialización de Mago. Añade el atributo poder mágico (mana).
    """
    def __init__(self, mana: int, **kwargs):
        super().__init__(**kwargs)
        self.mana = mana

    @log_accion
    def atacar(self) -> int:
        # El mago consume mana para lanzar un hechizo fuerte, si no, hace ataque base
        if self.mana >= 10:
            self.mana -= 10
            daño_hechizo = super().atacar() + 30
            print(f"  [Mago] ¡Bola de Fuego! Consume 10 mana (Queda: {self.mana}). Daño mágico: {daño_hechizo}")
            return daño_hechizo
        else:
            print("  [Mago] Sin mana suficiente. Realiza ataque físico débil.")
            return super().atacar()


# 4. Clase Paladín: La punta inferior del Diamante (Multiherencia)
# El MRO será: Paladin -> Guerrero -> Mago -> Personaje -> EntidadCombate -> ABC -> object
class Paladin(Guerrero, Mago):
    """
    Clase Paladín que combina habilidades de Guerrero y Mago.
    """
    def __init__(self, nombre: str, vida: int, nivel: int, fuerza: int, mana: int):
        # Llamamos cooperativamente a super().__init__
        # Todos los constructores anteriores deben recibir sus argumentos como keyword arguments (**kwargs)
        # o desempaquetarse explícitamente en orden de MRO.
        super().__init__(
            nombre=nombre,
            vida=vida,
            nivel=nivel,
            fuerza=fuerza,
            mana=mana
        )

    @log_accion
    def atacar(self) -> int:
        # Un paladín ataca combinando la espada física y el hechizo
        print("  [Paladín] Canalizando aura sagrada...")
        # Llama a atacar de Guerrero (vía MRO) y atacar de Mago (vía MRO)
        # Para forzar la llamada cooperativa al MRO:
        daño_fisico = Guerrero.atacar(self)
        daño_sagrado = Mago.atacar(self)
        return daño_fisico + daño_sagrado


# 5. Código de prueba para simulación
if __name__ == "__main__":
    print("--- 1. Creación de Personajes y Cooperación del MRO ---")
    # Instanciamos clases específicas
    guerrero_arturo = Guerrero(nombre="Arturo", vida=150, nivel=5, fuerza=15)
    mago_merlin = Mago(nombre="Merlín", vida=100, nivel=6, mana=30)
    paladin_lancelot = Paladin(nombre="Lancelot", vida=200, nivel=7, fuerza=12, mana=20)

    # Imprimir representaciones __repr__
    print(guerrero_arturo)
    print(mago_merlin)
    print(paladin_lancelot)

    # Mostrar la jerarquía del MRO del Paladín
    print("\nMethod Resolution Order (MRO) para la clase Paladin:")
    for cls in Paladin.__mro__:
        print(f" - {cls.__name__}")

    print("\n--- 2. Fase de Combate (Uso de Decorador y Métodos) ---")
    # Arturo ataca a Merlín
    daño_da = guerrero_arturo.atacar()
    mago_merlin.recibir_daño(daño_da)
    print()

    # Merlín contraataca
    daño_mag = mago_merlin.atacar()
    guerrero_arturo.recibir_daño(daño_mag)
    print()

    # Lancelot el Paladín ataca a un objetivo genérico
    daño_paladin = paladin_lancelot.atacar()
    print(f"Daño final calculado para el Paladín: {daño_paladin}\n")

    print("--- 3. Demostración de Sobrecarga de Operadores ---")
    # Comparar niveles (__gt__)
    print(f"¿Merlín ({mago_merlin.nivel}) es de mayor nivel que Arturo ({guerrero_arturo.nivel})?: {mago_merlin > guerrero_arturo}")
    print(f"¿Arturo es de mayor nivel que Lancelot?: {guerrero_arturo > paladin_lancelot}")

    # Fusión de personajes (__add__)
    print("\nFusionando Arturo y Merlín:")
    fusion = guerrero_arturo + mago_merlin
    print(fusion)
