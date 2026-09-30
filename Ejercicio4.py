# Ejercicio 4: Gestión de inventario de instrumentos musicales

# Cada sucursal tiene un nombre y una lista de instrumentos.
# Cada instrumento es un diccionario con ID, precio y tipo.
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