from clientes import registrar_cliente, mostrar_clientes

clientes = []

while True:
    print("---Menú Clientes---")
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_cliente(clientes)
    elif opcion == "2":
        mostrar_clientes(clientes)
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
