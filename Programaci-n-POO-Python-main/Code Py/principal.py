
from botella import Botella
from botella_plastica import BotellaPlastica
from botella_vidrio import BotellaVidrio

def ejecutar_demostracion():
    print("--- APLICANDO LOS 7 PASOS DE POO EN PYTHON ---")


    botella_generica = Botella(material="Aluminio", capacidad_ml=600, forma="Deportiva", tapa="Pitorro")
    botella_pet = BotellaPlastica(capacidad_ml=500, forma="Cilíndrica", tapa="Rosca", es_reciclable=True)
    botella_vino = BotellaVidrio(capacidad_ml=750, forma="Bordelesa", tapa="Corcho", grabado="Reserva Especial")

    res_generica = botella_generica.contener_liquidos(500)
    res_plastico = botella_pet.contener_liquidos(400)
    res_vidrio = botella_vino.contener_liquidos(750)

    print("\n--- RESULTADOS (Análisis de Datos) ---")
    
    print(f"1. Botella Genérica: {res_generica}")
    print(f"   Material: {botella_generica.material} | Capacidad: {botella_generica.obtener_capacidad()} ml\n")
    
    print(f"2. Botella Plástica: {res_plastico}")
    print(f"   Material: {botella_pet.material} | Contenido: {botella_pet.obtener_contenido()} ml\n")
    
    print(f"3. Botella Vidrio: {res_vidrio}")
    print(f"   Material: {botella_vino.material} | Grabado: {botella_vino.grabado}\n")

if __name__ == "__main__":
    ejecutar_demostracion()