
from animal import Animal
from caballo import Caballo
from pato import Pato
from cocodrilo import Cocodrilo
from escarabajo import Escarabajo

def ejecutar_ejercicio():
    print("=== EJERCICIO DE ANIMALES COMPLETO (POO) ===")

    
    mi_caballo = Caballo(nombre="Rayo", edad=5, color="Marrón", tamano="Grande", velocidad_max_kmh=60)
    mi_pato = Pato(nombre="Lucas", edad=2, color="Verde y Blanco", vuela=True)
    mi_cocodrilo = Cocodrilo(nombre="Dante", edad=12, color="Verde Oscuro", tamano_metros=3.5)
    mi_escarabajo = Escarabajo(nombre="Hércules", edad_meses=6, color="Negro Brillante", tiene_cuerno=True)

    
    rugido_coco = mi_cocodrilo.comunicacion()
    nado_coco = mi_cocodrilo.moverse()
    comida_coco = mi_cocodrilo.alimentarse("Carne / Carne fresca")

    
    sonido_escarabajo = mi_escarabajo.comunicacion()
    marcha_escarabajo = mi_escarabajo.moverse()
    comida_escarabajo = mi_escarabajo.alimentarse("Hojas secas")

    
    print("\n--- CABALLO Y PATO ---")
    print(mi_caballo.comunicacion())
    print(mi_pato.comunicacion())

    print("\n--- COCODRILO ---")
    print(rugido_coco)
    print(nado_coco)
    print(comida_coco)
    print(f"Energía actual: {mi_cocodrilo.obtener_energia()}%")

    print("\n--- ESCARABAJO ---")
    print(sonido_escarabajo)
    print(marcha_escarabajo)
    print(comida_escarabajo)
    print(f"Energía actual: {mi_escarabajo.obtener_energia()}%")

if __name__ == "__main__":
    ejecutar_ejercicio()