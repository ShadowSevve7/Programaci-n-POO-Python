from botella import Botella
from botella_vidrio import BotellaVidrio

#******* Codigo Principal ********

obj_botella = Botella
obj_botella_vidrio = BotellaVidrio

def ejecutar_demostracion():
    print("Paso a Paso de los 7 procesos para el POO en python")

from botella import Botella
from botella_vidrio import BotellaVidrio

def ejecutar_demostracion():
    print("--- APLICANDO LOS 7 PASOS DE POO EN PYTHON ---")


    # Paso 5: Crear Objeto = E.D (Instanciación de objetos con datos de entrada)
    botella_plastico = Botella(material="Plástico PET", capacidad_ml=500, forma="Cilíndrica", tapa="Rosca")
    botella_vino = BotellaVidrio(capacidad_ml=750, forma="Bordelesa", tapa="Corcho", grabado="Reserva Especial")

    # Paso 6: Llamar Métodos = E.D (Ejecutar acciones sobre los objetos)
    res_plastico = botella_plastico.contener_liquidos(400)
    res_vidrio = botella_vino.contener_liquidos(750) # Polimorfismo en acción

    print("\n--- RESULTADOS (Análisis de Datos) ---")
    print(f"Botella 1 (Plástico): {res_plastico}")
    print(f"Capacidad total: {botella_plastico.obtener_capacidad()} ml | Contenido actual: {botella_plastico.obtener_contenido()} ml")
    
    print("-" * 50)
    print(f"Botella 2 (Vidrio - Herencia/Polimorfismo): {res_vidrio}")
    print(f"Capacidad total: {botella_vino.obtener_capacidad()} ml | Grabado: {botella_vino.grabado}")

if __name__ == "__main__":
    ejecutar_demostracion()