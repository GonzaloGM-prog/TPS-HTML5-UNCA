#Ejercicio 1: Validación de entrada y búsqueda en una lista

# Lista predefinida de números
lista = [1, 3, 5, 7, 9]

# Pido el numero
numero = -1
while numero < 0 or numero > 9:
    entrada = input("Ingrese un número entero del 0 al 9: ")
    if entrada.isdigit():
        numero = int(entrada)
    else:
        numero = -1
    if numero < 0 or numero > 9:
        print("Entrada inválida. Debe ser un entero entre 0 y 9.")

# vemos si el numero esta o no
if numero in lista:
    print("El número", numero, "SÍ está en la lista", lista)
else:
    print("El número", numero, "NO está en la lista", lista)