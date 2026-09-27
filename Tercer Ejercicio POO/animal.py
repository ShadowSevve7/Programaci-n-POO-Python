class Animal:
    def __init__(self, nombre: str, edad: int, habitat: str, dieta: str, tamano: str, color: str):
        
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color
        
        
        self.__energia = 100
        self.__dormido = False

    
    def obtener_energia(self) -> int:
        return self.__energia

    def esta_dormido(self) -> bool:
        return self.__dormido

    
    def moverse(self) -> str:
        if self.__dormido:
            return f"{self.nombre} está dormido y no puede moverse."
        self.__energia -= 10
        return f"{self.nombre} se está moviendo en su hábitat ({self.habitat})."

    def comunicacion(self) -> str:
        return f"{self.nombre} emite un sonido o señal para comunicarse."

    def alimentarse(self, alimento: str) -> str:
        self.__energia = min(100, self.__energia + 20)
        return f"{self.nombre} se alimenta de {alimento} (Dieta: {self.dieta})."

    def descanso(self) -> str:
        self.__dormido = True
        self.__energia = 100
        return f"{self.nombre} entra en periodo de descanso/sueño."