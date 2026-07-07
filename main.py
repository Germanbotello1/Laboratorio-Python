from clientes import menu_clientes
from bicicletas import menu_bicicletas
from alquiler import menu_alquiler

#Menu principal del sistema
def menu_principal():
    while True:
        print("========================================")
        print("   SISTEMA DE ALQUILER DE BICICLETAS   ")
        print("========================================")

        print("1. Gestión de clientes")
        print("2. Gestión de bicicletas")
        print("3. Gestión de alquileres")
        print("4. Estadísticas")
        print("5. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_bicicletas()
        elif opcion == "3":
            menu_alquiler()
        elif opcion == "4":
            print("Módulo de estadísticas en desarrollo.")
        elif opcion == "5":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opción inválida.")

menu_principal()