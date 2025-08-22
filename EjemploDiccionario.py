directorio = {}

def validar():
    match input("[S/N]: ").upper():
        case "S":
            return True
        case "N":
            return False
        case _:
            print("Opcion no valida")

def agregar_contacto():
    while True:
        print("Informacion del contacto")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        numero = input("Telefono: ")
        direccion = input("Dirección: ")
        print("¿La informacion ingresada es correcta?")
        if validar():
            directorio[len(directorio) + 1] = {"nombre": nombre, "apellido": apellido, "numero": numero, "direccion": direccion}
            break

def mostrar_directorio():
    for indice, persona in directorio.items():
        print(f"{indice}. {persona["nombre"]}, {persona["apellido"]}, {persona["numero"]}, {persona["direccion"]}")


while True:
    print("Directorio\n")

    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Consultar directorio")
    print("4. Salir")
    match input("[]: "):
        case "1":
            agregar_contacto()
        case "2":
            pass
        case "3":
            mostrar_directorio()
        case "4":
            break
        case _:
            print("Operacion no valida")