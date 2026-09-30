
#  Validación de entrada y búsqueda en una lista

def ejercicio1():
    print("\n--- EJERCICIO 1 ---")
    lista = [1, 3, 5, 7, 9]

    numero = -1
    while numero < 0 or numero > 9:
        entrada = input("Ingrese un número entero del 0 al 9: ")
        if entrada.isdigit():
            numero = int(entrada)
        else:
            numero = -1
        if numero < 0 or numero > 9:
            print("Entrada inválida. Debe ser un entero entre 0 y 9.")

    if numero in lista:
        print("El número", numero, "SÍ está en la lista", lista)
    else:
        print("El número", numero, "NO está en la lista", lista)


# =====================================================
# EJERCICIO 2: Gestión de conjuntos de usuarios y administradores
# =====================================================
def ejercicio2():
    print("\n--- EJERCICIO 2 ---")
    usuarios = {"Marcela", "David", "Elvira", "Juan", "Marcos"}
    administradores = {"Juan", "Marcela"}

    administradores.discard("Juan")
    administradores.add("Marcos")

    print("Listado de usuarios:")
    for usuario in sorted(usuarios):
        if usuario in administradores:
            print("-", usuario, ": es administrador")
        else:
            print("-", usuario, ": NO es administrador")



#  Registro de información en un diccionario

def ejercicio3():
    print("\n--- EJERCICIO 3 ---")
    usuario_info = {}

    seguir = "s"
    while seguir.lower() == "s":
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")

        usuario_info[nombre] = {
            "nombre": nombre,
            "edad": edad,
            "dirección": direccion,
            "teléfono": telefono,
        }
        seguir = input("¿Desea ingresar otro usuario? (s/n): ")

    print("\nInformación ingresada:")
    for nombre in usuario_info:
        print("Usuario:", nombre)
        for clave, valor in usuario_info[nombre].items():
            print("  ", clave, ":", valor)



#  inventario de instrumentos musicales

sucursales = {
    "Centro": [
        {"id": "P001", "precio": 15000, "tipo": "Percusión"},
        {"id": "V001", "precio": 30000, "tipo": "Viento"},
        {"id": "C001", "precio": 45000, "tipo": "Cuerda"},
        {"id": "C002", "precio": 52000, "tipo": "Cuerda"},
    ],
    "Norte": [
        {"id": "P002", "precio": 22000, "tipo": "Percusión"},
        {"id": "V002", "precio": 28000, "tipo": "Viento"},
        {"id": "V003", "precio": 35000, "tipo": "Viento"},
    ],
}


def listarInstrumentos():
    """Muestra todos los instrumentos con sucursal, ID, precio y tipo."""
    for sucursal in sucursales:
        for inst in sucursales[sucursal]:
            print("Sucursal:", sucursal, "| ID:", inst["id"],
                "| Precio: $", inst["precio"], "| Tipo:", inst["tipo"])


def instrumentosPorTipo(tipo):
    """Devuelve una lista con los instrumentos del tipo indicado."""
    resultado = []
    for sucursal in sucursales:
        for inst in sucursales[sucursal]:
            if inst["tipo"].lower() == tipo.lower():
                resultado.append(inst)
    return resultado


def borrarInstrumento(id_instrum):
    """Elimina el instrumento con ese ID de la sucursal donde se encuentre."""
    for sucursal in sucursales:
        for inst in sucursales[sucursal]:
            if inst["id"] == id_instrum:
                sucursales[sucursal].remove(inst)
                print("Instrumento", id_instrum, "eliminado de la sucursal", sucursal)
                return True
    print("No se encontró ningún instrumento con ID", id_instrum)
    return False


def porcInstrumentosPorTipo(sucursal):
    """Muestra y retorna el porcentaje de instrumentos de cada tipo."""
    if sucursal not in sucursales:
        print("La sucursal", sucursal, "no existe")
        return None

    instrumentos = sucursales[sucursal]
    total = len(instrumentos)
    porcentajes = {"Percusión": 0, "Viento": 0, "Cuerda": 0}

    if total == 0:
        print("La sucursal", sucursal, "no tiene instrumentos")
        return porcentajes

    for tipo in porcentajes:
        cantidad = 0
        for inst in instrumentos:
            if inst["tipo"] == tipo:
                cantidad += 1
        porcentajes[tipo] = cantidad * 100 / total

    print("Porcentajes en la sucursal", sucursal + ":")
    for tipo, porc in porcentajes.items():
        print("-", tipo, ":", round(porc, 2), "%")
    return porcentajes


def ejercicio4():
    print("\n--- EJERCICIO 4 ---")
    print("=== Listado de instrumentos ===")
    listarInstrumentos()

    print("\n=== Instrumentos de tipo Cuerda ===")
    for inst in instrumentosPorTipo("Cuerda"):
        print(inst)

    print("\n=== Porcentajes por tipo (Centro) ===")
    porcInstrumentosPorTipo("Centro")

    print("\n=== Borrar instrumento V002 ===")
    borrarInstrumento("V002")

    print("\n=== Listado actualizado ===")
    listarInstrumentos()

    print("\n=== Porcentajes por tipo (Norte) ===")
    porcInstrumentosPorTipo("Norte")



# ESTE SERIA EL PROGRAMA PRINCIPAL

opcion = ""
while opcion != "0":
    print("\n===== TP IV - Python =====")
    print("1. Ejercicio 1 - Validación y búsqueda en lista")
    print("2. Ejercicio 2 - Conjuntos de usuarios y administradores")
    print("3. Ejercicio 3 - Diccionario de usuarios")
    print("4. Ejercicio 4 - Inventario de instrumentos")
    print("0. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        ejercicio1()
    elif opcion == "2":
        ejercicio2()
    elif opcion == "3":
        ejercicio3()
    elif opcion == "4":
        ejercicio4()
    elif opcion != "0":
        print("Opción inválida.")
print("Fin del programa.")
