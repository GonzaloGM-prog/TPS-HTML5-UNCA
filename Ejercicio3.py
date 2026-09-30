# Ejercicio 3: Registro de información en un diccionario

# Diccionario principal: clave = nombre, valor = diccionario con los datos
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

# Muestro la info
print("\nInformación ingresada:")
for nombre in usuario_info:
    print("Usuario:", nombre)
    for clave, valor in usuario_info[nombre].items():
        print("  ", clave, ":", valor)
