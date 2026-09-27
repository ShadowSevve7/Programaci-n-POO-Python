from botella import Botella

class BotellaVidrio(Botella):
    def __init__(self, capacidad_ml: int, forma: str, tapa: str, grabado: str):
        # Constructor de la superclase
        super().__init__(material="Vidrio", capacidad_ml=capacidad_ml, forma=forma, tapa=tapa)
        self.grabado = grabado

    
    def contener_liquidos(self, cantidad_ml: int) -> str:
        mensaje_base = super().contener_liquidos(cantidad_ml)
        return f"[Botella de Vidrio Grabada '{self.grabado}'] {mensaje_base} Mantiene la bebida fresca."