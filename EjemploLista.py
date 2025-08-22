sabores = ["Chocolate","Vainilla","Fresa","Mango"]

def mostrar_sabores(sabores):
    i = 1
    for sabor in sabores:
        print(f"{i}. {sabor}")
        i += 1


while True:
    print("Pasteleria\n")

    print("Ingrese el numero de la opcion")
    print("1. Eliminar sabor")
    print("2. Ultimo sabor agregado")
    print("3. Salir")
    match input("[]: "):
        case "1":
            while True:
                while True:
                    print("Indique numero del sabor que desea elminiar:")
                    mostrar_sabores(sabores)
                    try:
                        indice = int(input("[]: ")) - 1
                        break
                    except ValueError:
                        print("Valor invalido")
                if indice <= len(sabores) - 1 and indice >= 0:
                    sabor_eliminado = sabores.pop(indice)
                    print(f"Sabor eliminado: {sabor_eliminado}")
                    break
        case "2":
            print(f"El ultimo sabor ingresado fue {sabores[-1]}\n")
            
        case _:
            break