from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, modelo: str, color: str, motor: str, combustible: str, ejes: int):
        super().__init__(modelo, color, motor, puertas=2, pasajeros=3, combustible=combustible)
        self.ejes = ejes

    
    def aceleracion_y_frenado(self, cambio_kmh: int) -> str:
        mensaje = super().aceleracion_y_frenado(cambio_kmh)
        if cambio_kmh < 0:
            return f"[Camión {self.ejes} ejes] {mensaje} (Freno de aire activado)."
        return f"[Camión {self.ejes} ejes] {mensaje}"