# MÓDULO: GESTIÓN DE BICICLETAS
# Sistema de alquiler de bicicletas

ARCHIVO_BICICLETAS = "bicicletas.txt"


def registrar_bicicleta():
    """
    Registra una bicicleta nueva.
    """

    id_bici = input("Ingrese ID de la bicicleta: ")
    modelo = input("Ingrese modelo: ")

    estado = "Disponible"

    with open(ARCHIVO_BICICLETAS, "a") as archivo:
        archivo.write(id_bici + ";" + modelo + ";" + estado + "\n")

    print("\nBicicleta registrada correctamente.\n")


def mostrar_bicicletas():
    """
    Muestra todas las bicicletas registradas.
    """

    with open(ARCHIVO_BICICLETAS, "r") as archivo:

        print("\n===== LISTA DE BICICLETAS =====\n")

        for linea in archivo:

            datos = linea.strip().split(";")

            print("ID:", datos[0])
            print("Modelo:", datos[1])
            print("Estado:", datos[2])
            print("-----------------------------")


def buscar_bicicleta():
    """
    Busca una bicicleta por ID.
    """

    buscar = input("Ingrese ID a buscar: ")

    encontrada = False

    with open(ARCHIVO_BICICLETAS, "r") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if datos[0] == buscar:

                print("\nBicicleta encontrada")
                print("-------------------")
                print("ID:", datos[0])
                print("Modelo:", datos[1])
                print("Estado:", datos[2])

                encontrada = True
                break

    if not encontrada:
        print("No existe una bicicleta con ese ID.")


def mostrar_disponibles():
    """
    Muestra únicamente las bicicletas disponibles.
    """

    with open(ARCHIVO_BICICLETAS, "r") as archivo:

        print("\n===== BICICLETAS DISPONIBLES =====\n")

        for linea in archivo:

            datos = linea.strip().split(";")

            if datos[2] == "Disponible":

                print("ID:", datos[0])
                print("Modelo:", datos[1])
                print("----------------------")


def cambiar_estado():
    """
    Cambia el estado de una bicicleta.
    """

    buscar = input("Ingrese ID de la bicicleta: ")

    nuevo_estado = input(
        "Nuevo estado (Disponible / Alquilada / Mantenimiento): "
    )

    lineas = []

    with open(ARCHIVO_BICICLETAS, "r") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if datos[0] == buscar:

                datos[2] = nuevo_estado

            linea = datos[0] + ";" + datos[1] + ";" + datos[2] + "\n"

            lineas.append(linea)

    with open(ARCHIVO_BICICLETAS, "w") as archivo:

        for linea in lineas:

            archivo.write(linea)

    print("Estado actualizado correctamente.")