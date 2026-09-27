class Botella:
    def __init__(self, material: str, capacidad_ml: int, forma: str, tapa: str):
        self.material = material
        self.forma = forma
        self.tapa = tapa
        
        
        self.__capacidad_ml = capacidad_ml
        self.__contenido_actual_ml = 0

    
    def obtener_capacidad(self) -> int:
        return self.__capacidad_ml

    def obtener_contenido(self) -> int:
        return self.__contenido_actual_ml

    
    def contener_liquidos(self, cantidad_ml: int) -> str:
        if cantidad_ml <= self.__capacidad_ml:
            self.__contenido_actual_ml = cantidad_ml
            return f"Se vertieron {cantidad_ml} ml de líquido en la botella."
        else:
            return f"Error: La cantidad supera la capacidad máxima de {self.__capacidad_ml} ml."

    def vaciar(self) -> str:
        self.__contenido_actual_ml = 0
        return "La botella ha sido vaciada."