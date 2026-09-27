from vehiculo import Vehiculo
from autodeportivo import AutoDeportivo
from furgoneta import Furgoneta
from camion import Camion

def ejecutar_ejercicio():
    print("==================================================")
    print("      EJERCICIO POO: VEHÍCULOS EN PYTHON       ")
    print("==================================================\n")



    
    bmw = AutoDeportivo(modelo="BMW Z4", color="Negro", motor="V6 3.0L", combustible="Gasolina", techo_descapotable=True)
    van = Furgoneta(modelo="Suzuki Carry", color="Blanco", motor="1.5L", combustible="Gasolina", capacidad_carga_kg=800)
    freightliner = Camion(modelo="Freightliner M2", color="Blanco", motor="Detroit Diesel 7.2L", combustible="Diésel", ejes=2)

    
    # Arranque de vehículo
    arranque_bmw = bmw.arranque()
    arranque_van = van.arranque()
    arranque_camion = freightliner.arranque()

    
    acel_bmw = bmw.aceleracion_y_frenado(30)       # Aumenta el doble por modo Sport
    acel_camion = freightliner.aceleracion_y_frenado(-10) # Freno de aire

    
    clima_bmw = bmw.climatizacion(21)
    luces_van = van.luces("Altas encendidas")

   
    print("--- ANÁLISIS DE DATOS Y SALIDA ---")
    
    print("\n1. AUTO DEPORTIVO:")
    print(f"   Arrancando: {arranque_bmw}")
    print(f"   Prueba Aceleración: {acel_bmw}")
    print(f"   Climatización: {clima_bmw}")
    print(f"   Encendido (Encapsulado): {bmw.esta_encendido()}")

    print("\n2. FURGONETA:")
    print(f"   Arrancando: {arranque_van}")
    print(f"   Luces: {luces_van}")
    print(f"   Capacidad Pasajeros: {van.pasajeros}")

    print("\n3. CAMIÓN:")
    print(f"   Arrancando: {arranque_camion}")
    print(f"   Prueba Frenado: {acel_camion}")
    print(f"   Tipo Combustible: {freightliner.combustible}")

if __name__ == "__main__":
    ejecutar_ejercicio()