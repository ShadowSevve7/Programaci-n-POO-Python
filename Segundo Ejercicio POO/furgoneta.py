from vehiculo import Vehiculo

class Furgoneta(Vehiculo):
    def __init__(self, modelo: str, color: str, motor: str, combustible: str, capacidad_carga_kg: int):
        super().__init__(modelo, color, motor, puertas=5, pasajeros=7, combustible=combustible)
        self.capacidad_carga_kg = capacidad_carga_kg

    
    def arranque(self) -> str:
        mensaje_base = super().arranque()
        return f"[Furgoneta Comercial] {mensaje_base} Verificando peso de carga ({self.capacidad_carga_kg} kg max)."