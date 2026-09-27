from vehiculo import Vehiculo

class AutoDeportivo(Vehiculo):
    def __init__(self, modelo: str, color: str, motor: str, combustible: str, techo_descapotable: bool):
        
        super().__init__(modelo, color, motor, puertas=2, pasajeros=2, combustible=combustible)
        self.techo_descapotable = techo_descapotable

   
    def aceleracion_y_frenado(self, cambio_kmh: int) -> str:
        
        potencia = cambio_kmh * 2 if cambio_kmh > 0 else cambio_kmh
        mensaje = super().aceleracion_y_frenado(potencia)
        return f"[Deportivo {self.modelo}] {mensaje} ¡Modo Sport Activo!"

    def abatir_techo(self) -> str:
        if self.techo_descapotable:
            return f"El techo descapotable de {self.modelo} se ha abierto."
        return "Este vehículo no tiene techo descapotable."