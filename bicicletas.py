# MÓDULO: GESTIÓN DE BICICLETAS
# Sistema de alquiler de bicicletas

ARCHIVO_BICICLETAS = "bicicletas.txt"


def registrar_bicicleta():
    """
    Registra una bicicleta nueva.
    """

    codigo = input("Ingrese el codigo de la bicicleta: ")
    modelo = input("Ingrese modelo: ")

    if existe_bicicleta(codigo):
        print("Error: Ya existe una bicicleta con ese código.")
        return

    estado = "Disponible"

    try:
        with open(ARCHIVO_BICICLETAS, "a") as archivo:
            archivo.write(codigo + ";" + modelo + ";" + estado + "\n")
        print("\nBicicleta registrada correctamente.\n")
    
    except FileNotFoundError:
        print("Error al abrir el archivo.")

def existe_bicicleta(codigo):
    """
    Verifica si una bicicleta con el código dado ya existe.
    """
    bicicleta = buscar_bicicleta(codigo)
    if bicicleta is None:
        return False
    return True

def mostrar_bicicletas():
    """
    Muestra todas las bicicletas registradas.
    """
    try:
        with open(ARCHIVO_BICICLETAS, "r") as archivo:

            print("\n===== LISTA DE BICICLETAS =====\n")

            for linea in archivo:

                datos = linea.strip().split(";")

                print("Codigo:", datos[0])
                print("Modelo:", datos[1])
                print("Estado:", datos[2])
                print("-----------------------------")
    except FileNotFoundError:
        print("No hay bicicletas registradas.")

def buscar_bicicleta(codigo):
    """
    Busca una bicicleta por código.
    """
    codigo = input("Ingrese el código de la bicicleta: ")
    bicicleta = buscar_bicicleta(codigo)
    if bicicleta is None:
        print("Bicicleta no encontrada.")
        return
    print("Bicicleta encontrada:")
    print("Codigo:", bicicleta["codigo"])
    print("Modelo:", bicicleta["modelo"])
    print("Estado:", bicicleta["estado"])

def mostrar_disponibles():
    """
    Muestra únicamente las bicicletas disponibles.
    """
    try:
        with open(ARCHIVO_BICICLETAS, "r") as archivo:
        
            print("\n===== BICICLETAS DISPONIBLES =====\n")

        for linea in archivo:

            datos = linea.strip().split(";")

            if datos[2] == "Disponible":

                print("Codigo:", datos[0])
                print("Modelo:", datos[1])
                print("----------------------")
    except FileNotFoundError:
        print("No hay bicicletas registradas.")

def cambiar_estado():
    """
    Cambia el estado de una bicicleta.
    """

    lineas = []
    encontrada = False
    try:
        with open(ARCHIVO_BICICLETAS, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                if datos[0] == codigo:
                    datos[2] = nuevo_estado
                    encontrada = True
                lineas.append(";".join(datos) + "\n")
        with open(ARCHIVO_BICICLETAS, "w") as archivo:
            archivo.writelines(lineas)
    except FileNotFoundError:
        return False
    return encontrada

#Menu
def menu_bicicletas():
    while True:
        print("========== GESTIÓN DE BICICLETAS ==========")
        print("1. Registrar bicicleta")
        print("2. Consultar bicicleta")
        print("3. Mostrar todas las bicicletas")
        print("4. Mostrar bicicletas disponibles")
        print("5. Cambiar estado de una bicicleta")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_bicicleta()
        elif opcion == "2":
            consultar_bicicleta()
        elif opcion == "3":
            mostrar_bicicletas()
        elif opcion == "4":
            mostrar_disponibles()
        elif opcion == "5":
            codigo = input("Ingrese el código de la bicicleta: ")
            print("Estados posibles:")
            print("1. Disponible")
            print("2. Alquilada")
            print("3. Mantenimiento")

            opcion_estado = input("Seleccione el nuevo estado: ")

            if opcion_estado == "1":
                nuevo_estado = "Disponible"
            elif opcion_estado == "2":
                nuevo_estado = "Alquilada"
            elif opcion_estado == "3":
                nuevo_estado = "Mantenimiento"
            else:
                print("Estado inválido.")
                continue

            if cambiar_estado(codigo, nuevo_estado):
                print("Estado actualizado correctamente.")
            else:
                print("No existe una bicicleta con ese código.")
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")