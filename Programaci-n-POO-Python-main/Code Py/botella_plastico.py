from botella import Botella

class BotellaPlastica(Botella):
    def __init__(self, capacidad_ml: int, forma: str, tapa: str, es_reciclable: bool):
        # Constructor de la superclase
        super().__init__(material="Plástico PET", capacidad_ml=capacidad_ml, forma=forma, tapa=tapa)
        self.es_reciclable = es_reciclable

    # Polimorfismo: Sobrescribe contener_liquidos()
    def contener_liquidos(self, cantidad_ml: int) -> str:
        mensaje_base = super().contener_liquidos(cantidad_ml)
        reciclable_txt = "Es 100% Reciclable" if self.es_reciclable else "No es reciclable"
        return f"[Botella Plástica - {reciclable_txt}] {mensaje_base}"