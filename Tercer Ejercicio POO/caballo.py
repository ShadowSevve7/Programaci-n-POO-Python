from animal import Animal

class Caballo(Animal):
    def __init__(self, nombre: str, edad: int, color: str, tamano: str, velocidad_max_kmh: int):
        super().__init__(
            nombre=nombre, 
            edad=edad, 
            habitat="Pradera / Campo", 
            dieta="Herbívoro", 
            tamano=tamano, 
            color=color
        )
        self.velocidad_max_kmh = velocidad_max_kmh

    
    def comunicacion(self) -> str:
        return f"[Caballo {self.nombre}] ¡Relincha fuertemente! (¡Iiii-hh-hh-hh!)"

    
    def moverse(self) -> str:
        mensaje_base = super().moverse()
        return f"[Caballo] {mensaje_base} Está galopando a {self.velocidad_max_kmh} km/h."