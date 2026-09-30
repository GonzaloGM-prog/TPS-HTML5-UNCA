# Ejercicio 2: Gestión de conjuntos de usuarios y administradores
# 1. pongo el conjunto de usuarios
usuarios = {"Marcela", "David", "Elvira", "Juan", "Marcos"}
# 2. pongo el conjunto de administradores
administradores = {"Juan", "Marcela"}
# 3. Eliminar a Juan de los administradores
administradores.discard("Juan")

# 4. Añadir a Marcos como administrador 
administradores.add("Marcos")

# 5. Mostrar todos los usuarios indicando si son administradores
print("Listado de usuarios:")
for usuario in sorted(usuarios):
    if usuario in administradores:
        print("-", usuario, ": es administrador")
    else:
        print("-", usuario, ": NO es administrador")