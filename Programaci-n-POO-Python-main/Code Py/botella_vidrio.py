from botella import Botella

# Herencia: BotellaVidrio hereda de Botella
class BotellaVidrio(Botella):
    def __init__(self, capacidad_ml: int, forma: str, tapa: str, grabado: str):
        # Llamada al constructor de la clase padre
        super().__init__(material="Vidrio", capacidad_ml=capacidad_ml, forma=forma, tapa=tapa)
        self.grabado = grabado

    # Polimorfismo: Sobrescribimos el método contener_liquidos para añadir comportamiento de vidrio
    def contener_liquidos(self, cantidad_ml: int) -> str:
        mensaje_base = super().contener_liquidos(cantidad_ml)
        return f"[Botella de Vidrio Grabada '{self.grabado}'] {mensaje_base} Se mantiene fresco y protegido."