from animal import Animal

class Cocodrilo(Animal):
    def __init__(self, nombre: str, edad: int, color: str, tamano_metros: float):
        super().__init__(
            nombre=nombre,
            edad=edad,
            habitat="Ríos / Pantanos",
            dieta="Carnívoro",
            tamano=f"{tamano_metros}m",
            color=color
        )
        self.tamano_metros = tamano_metros

    
    def comunicacion(self) -> str:
        return f"[Cocodrilo {self.nombre}] Emite un rugido/soplido subacuático amenazante."

    
    def moverse(self) -> str:
        return f"[Cocodrilo {self.nombre}] Se desliza sigilosamente por el agua del pantano."