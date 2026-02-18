# Crear una función que reciba dos listas y devuelva una nueva lista con los elementos comunes entre ambas listas, sin duplicados.
def interseccion_listas(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    resultado = sorted(list(conjunto1 & conjunto2))
    return resultado

# Entrada desde consola
entrada1 = input("Ingresa los elementos de la primera lista (separados por coma): ")
entrada2 = input("Ingresa los elementos de la segunda lista (separados por coma): ")

# Convertir strings a listas de números
lista1 = [int(x.strip()) for x in entrada1.split(",")]
lista2 = [int(x.strip()) for x in entrada2.split(",")]

print("Elementos comunes:", interseccion_listas(lista1, lista2))