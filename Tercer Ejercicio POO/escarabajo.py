from animal import Animal

class Escarabajo(Animal):
    def __init__(self, nombre: str, edad_meses: int, color: str, tiene_cuerno: bool):
        super().__init__(
            nombre=nombre,
            edad=edad_meses,
            habitat="Bosque / Tierra",
            dieta="Herbívoro/Descomponedor",
            tamano="Muy Pequeño",
            color=color
        )
        self.tiene_cuerno = tiene_cuerno

    
    def comunicacion(self) -> str:
        return f"[Escarabajo {self.nombre}] Frota sus patas/alas para generar estridulación (sonido casi imperceptible)."

    
    def moverse(self) -> str:
        cuerno_txt = "con su cuerno frontal" if self.tiene_cuerno else ""
        return f"[Escarabajo {self.nombre}] Trepa sobre la corteza de los árboles {cuerno_txt}."