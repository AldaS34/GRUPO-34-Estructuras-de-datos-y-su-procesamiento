
def plano_cartesiano(conjunto_1, conjunto_2):
    relacion = set()
    for dato_1 in conjunto_1:
        for dato_2 in conjunto_2:
            relacion.add((dato_1,dato_2))
    return relacion 
    
def dominio(conjuntos):
    dom = set()
    for conjunto in conjuntos:
        dom.add(conjunto[0])
    return dom 

def codominio(conjuntos):
    cod = set()
    for conjunto in conjuntos:
        cod.add(conjunto[1])
    return cod 

def union(conjunto_1, conjunto_2):
    return conjunto_1 | conjunto_2

def interseccion(conjunto_1, conjunto_2):
    return conjunto_1 & conjunto_2

def complemento(conjunto_1, conjunto_2):
    return plano_cartesiano(conjunto_1,conjunto_2) - conjunto_1

def diferencia(conjunto_1, conjunto_2):
    return conjunto_1 - conjunto_2

def diferencia_simetrica(conjunto_1, conjunto_2):
    return conjunto_1 ^ conjunto_2

def validar():
    match input("[S/N]: ").upper().strip():
        case "N":
            return True
        case "S":
            return False
        case _:
            print("Opcion no valida")

def obtener_conjunto():
    conjunto = set()
    while True:
        try:
            print("Ingresa un elemento a la vez y presiona enter")
            elemento = int(input("[]: "))
            conjunto.add(elemento)
            print("¿Agregar otro elemento?")
            if validar():
                print(conjunto)
                return conjunto
        except ValueError:
            print("Valor ingresado invalido")

conjunto_1 = set()
conjunto_2 = set()

print("Agrega elementos del primer conjunto")
conjunto_1 = obtener_conjunto()
print("Agregar elementos del segundo conjunto")
conjunto_2 = obtener_conjunto()
relacion = plano_cartesiano(conjunto_1, conjunto_2)
print(relacion)

while True:
    print("Menu")
    print("1. Crear plano cartesiano")
    print("2. Obtener Dominio")
    print("3. Obtener Codominio")
    print("4. Obtener Union")
    print("5. Obtener Interseccion")
    print("6. Obtener Complemento")
    print("7. Obtener Diferencia")
    print("8. Obtener Diferencia simetrica")
    print("9. Salir")

    match input("[]:"):
        case "1":
            print(plano_cartesiano(conjunto_1, conjunto_2))
        case "2":
            print(dominio(relacion))
        case "3":
            print(codominio(relacion))
        case "4":
            print(union(conjunto_1, conjunto_2))
        case "5":
            print(interseccion(conjunto_1, conjunto_2))
        case "6":
            print(complemento(conjunto_1, conjunto_2))
        case "7":
            print(diferencia(conjunto_1, conjunto_2))
        case "8":
            print(diferencia_simetrica(conjunto_1, conjunto_2))
        case "9":
            break
        case _:
            print("Opcion no valida")