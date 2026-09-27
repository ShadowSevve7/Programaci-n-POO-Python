from animal import Animal

class Pato(Animal):
    def __init__(self, nombre: str, edad: int, color: str, vuela: bool):
        super().__init__(
            nombre=nombre, 
            edad=edad, 
            habitat="Lago / Humedal", 
            dieta="Omnívoro", 
            tamano="Pequeño", 
            color=color
        )
        self.vuela = vuela

    
    def comunicacion(self) -> str:
        return f"[Pato {self.nombre}] ¡Hace Cuak Cuak!"

    
    def moverse(self) -> str:
        estilo = "volando por el cielo" if self.vuela else "nadando en el agua"
        return f"[Pato {self.nombre}] Se desplaza {estilo}."