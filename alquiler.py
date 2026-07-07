#Gestion de Alquileres

from datetime import datetime
from clientes import buscar_cliente
from bicicletas import buscar_bicicleta
from bicicletas import cambiar_estado

ARCHIVO_ALQUILERES = "alquileres.txt"
TARIFA_HORA = 3000  # Tarifa por hora de alquiler

def registrar_alquiler():
    dni = input("Ingrese DNI del cliente: ")
    cliente = buscar_cliente(dni)
    if cliente is None:
        print("Cliente no encontrado. Debe registrarse primero.")
        return
    
    codigo = input("Ingrese código de la bicicleta: ")
    bicicleta = buscar_bicicleta(codigo)
    if bicicleta is None:
        print("Bicicleta no encontrada.")
        return
    
    if bicicleta["estado"] != "Disponible":
        print("La bicicleta no está disponible para alquiler.")
        return
    fecha_inicio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(ARCHIVO_ALQUILERES, "a") as archivo:
        archivo.write(dni + "," + codigo + "," + fecha_inicio + "," + ";" + "Activo\n")
    cambiar_estado(codigo, "Alquilada")
    print("Alquiler registrado exitosamente.")

def buscar_alquiler_activo(codigo):
    """
    Busca un alquiler activo por código de bicicleta.
    """
    try:
        with open(ARCHIVO_ALQUILERES, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if datos[1] == codigo and datos[4] == "Activo":
                    alquiler = {
                        "dni": datos[0],
                        "codigo": datos[1],
                        "fecha_inicio": datos[2],
                        "fecha_fin": datos[3],
                        "estado": datos[4]
                    }
                    return alquiler
    except FileNotFoundError:
        print("No hay registros de alquileres.")
    return None

def registrar_devolucion():
    """
    Registra la devolución de una bicicleta.
    """
    codigo = input("Ingrese código de la bicicleta: ")
    alquiler = buscar_alquiler_activo(codigo)

    if alquiler is None:
        print("\nNo existe un alquiler activo para esa bicicleta.\n")
        return

    fecha_fin = datetime.now()

    fecha_inicio = datetime.strptime(
        alquiler["fecha_inicio"],"%d/%m/%Y %H:%M")

    tiempo = fecha_fin - fecha_inicio
    horas = tiempo.total_seconds() / 3600

    if horas < 1:
        horas = 1
    importe = horas * TARIFA_HORA
    cambiar_estado(codigo, "Disponible")
    actualizar_alquiler(codigo, fecha_fin.strftime("%d/%m/%Y %H:%M"))

    print("\n===== DEVOLUCIÓN =====")
    print("Tiempo de uso:", round(horas, 2), "horas")
    print("Importe: $", round(importe, 2))
    print("\nDevolución registrada correctamente.\n")

def actualizar_alquiler(codigo, fecha_fin):
    lineas = []
    with open(ARCHIVO_ALQUILERES, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")

            if datos[1] == codigo and datos[4] == "Activo":
                datos[3] = fecha_fin
                datos[4] = "Finalizado"

            lineas.append(";".join(datos) + "\n")

    with open(ARCHIVO_ALQUILERES, "w") as archivo:

        archivo.writelines(lineas)

def mostrar_alquileres():
    """
    Muestra todos los alquileres registrados.
    """
    try:
        with open(ARCHIVO_ALQUILERES, "r") as archivo:
            print("======= ALQUILERES =======")
            for linea in archivo:
                datos = linea.strip().split(";")
                print("DNI       :", datos[0])
                print("Bicicleta :", datos[1])
                print("Inicio    :", datos[2])
                print("Fin       :", datos[3])
                print("Estado    :", datos[4])
                print("------------------------------")

    except FileNotFoundError:
        print("No existen alquileres registrados.")

#Menu
def menu_alquiler():
    while True:
        print("========== GESTIÓN DE ALQUILERES ==========")
        print("1. Registrar alquiler")
        print("2. Registrar devolución")
        print("3. Mostrar alquileres")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_alquiler()
        elif opcion == "2":
            registrar_devolucion()
        elif opcion == "3":
            mostrar_alquileres()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")