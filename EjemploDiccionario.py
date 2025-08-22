directorio = {}

def mostrar_directorio():
    print("\nDirectorio")
    for indice, persona in directorio.items():
        print(f"{indice}. {persona["nombre"]}, {persona["apellido"]}, {persona["numero"]}, {persona["direccion"]}")


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
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        numero = input("Telefono: ").strip()
        direccion = input("Dirección: ").strip()
        print("¿La informacion ingresada es correcta?")
        print(f"{nombre}, {apellido}, {numero}, {direccion}")
        if validar():

            directorio[len(directorio) + 1] = {"nombre": nombre, "apellido": apellido, "numero": numero, "direccion": direccion}
            break

def eliminar_contacto():
    if len(directorio) > 0:
        while True:
            print("\nSelecciona el contacto que deseas eliminar\n")
            mostrar_directorio()
            try:
                buscador = int(input("[]: "))

                if buscador in directorio:
                    persona_eliminada = directorio.pop(buscador)
                    print(f"Persona eliminada, {persona_eliminada["nombre"]}, {persona_eliminada["apellido"]}\n")
                    break
                else: 
                    print("Indice no encontrado")
            except ValueError:
                print("Valor ingresado no es valido")
    else:
        print("Directorio vacio")

while True:
    print("\nDirectorio\n")

    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Consultar directorio")
    print("4. Salir")
    match input("[]: "):
        case "1":
            agregar_contacto()
        case "2":
            eliminar_contacto()
        case "3":
            mostrar_directorio()
        case "4":
            break
        case _:
            print("Operacion no valida")
print("Programa Termiando")