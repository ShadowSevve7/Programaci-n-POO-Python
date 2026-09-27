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
        if cantidad_ml <= self.__contenido_actual_ml:
            return f"Se han vertido actualmente {cantidad_ml} de liquido de la botella. :D"
        else:
            return f"Se ha llenado actualmente la botella con la capacidad maxima de {self.__capaciadad_ml} ml. :P"

    def vaciar(self) -> str:
        self.__contenido_actual_ml = 0
        return "La botella se ha vaciado al fallo xD"