def validar_dni(dni):
    # Función para validar el formato del DNI
    while True:
        if len(dni) == 8 and dni.isdigit():
            return True
        else:
            print("DNI inválido. Debe tener 8 dígitos.")
            print("completar con ceros a la izquierda si es necesario.")
            dni = input("Ingrese su DNI: ")

def validar_nombre(nombre):
    # Función para validar el nombre del cliente
    while True:
        if nombre.isalpha():
            return True
        else:
            print("Nombre inválido. Debe contener solo letras.")
            nombre = input("Ingrese su nombre: ")

def validar_email(email):
    # Función para validar el formato del email
    while True:
        if "@" in email and "." in email:
            return True
        else:
            print("Email inválido. Debe contener '@' y '.'")
            email = input("Ingrese su email: ")

def validar_telefono(telefono):
    # Función para validar el formato del número de teléfono
    while True:
        if telefono.isdigit() and len(telefono) >= 7:
            return True
        else:
            print("Número de teléfono inválido. Debe contener solo dígitos y tener al menos 7 dígitos.")
            telefono = input("Ingrese su número de teléfono: ")

def registrar_cliente(clientes):
    # Función para registrar un nuevo cliente
    dni = input("Ingrese su DNI: ")
    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    telefono = input("Ingrese su número de teléfono: ")
    
    clientes = {"dni": dni, "nombre": nombre, "email": email, "telefono": telefono}

    clientes.append (clientes)

    print("Cliente registrado exitosamente.")


def buscar_cliente(clientes, dni):
    # Función para buscar un cliente por DNI
    for cliente in clientes:
        if cliente["dni"] == dni:
            print(f"Cliente encontrado: {cliente}")
            return cliente
    print("Cliente no encontrado.")
    return None

def mostrar_clientes(clientes):
    # Función para mostrar todos los clientes registrados
    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return
    else:
        for cliente in clientes:
            print("-----------------------------")
            print(f"DNI: {cliente['dni']}, Nombre: {cliente['nombre']}, Email: {cliente['email']}, Teléfono: {cliente['telefono']}")
            print("-----------------------------")

def eliminar_cliente(clientes, dni):
    # Función para eliminar un cliente por DNI
    for cliente in clientes:
        if cliente["dni"] == dni:
            clientes.remove(cliente)
            print("Cliente eliminado exitosamente.")
            return
    print("Cliente no encontrado.")

def existe_cliente(clientes, dni):
    # Función para verificar si un cliente existe por DNI
    for cliente in clientes:
        if cliente["dni"] == dni:
            return True
            print("Cliente registrado.")
    return False
    print("Cliente no registrado.")