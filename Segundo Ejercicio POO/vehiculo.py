class Vehiculo:
    def __init__(self, modelo: str, color: str, motor: str, puertas: int, pasajeros: int, combustible: str):
        
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.puertas = puertas
        self.pasajeros = pasajeros
        self.combustible = combustible
        
        
        self.__encendido = False
        self.__velocidad_kmh = 0

    
    def esta_encendido(self) -> bool:
        return self.__encendido

    def obtener_velocidad(self) -> int:
        return self.__velocidad_kmh

    
    def arranque(self) -> str:
        if not self.__encendido:
            self.__encendido = True
            return f"El vehículo {self.modelo} ha arrancado."
        return f"El vehículo {self.modelo} ya está encendido."

    def apagado(self) -> str:
        if self.__encendido:
            self.__encendido = False
            self.__velocidad_kmh = 0
            return f"El vehículo {self.modelo} se ha apagado."
        return f"El vehículo {self.modelo} ya estaba apagado."

    def aceleracion_y_frenado(self, cambio_kmh: int) -> str:
        if not self.__encendido:
            return "No se puede acelerar ni frenar con el vehículo apagado."
        
        self.__velocidad_kmh += cambio_kmh
        if self.__velocidad_kmh < 0:
            self.__velocidad_kmh = 0
            
        return f"Velocidad actual de {self.modelo}: {self.__velocidad_kmh} km/h."

    def luces(self, estado: str) -> str:
        return f"Luces de {self.modelo}: {estado}."

    def climatizacion(self, temp_celsius: int) -> str:
        return f"Climatización ajustada a {temp_celsius}°C en {self.modelo}."