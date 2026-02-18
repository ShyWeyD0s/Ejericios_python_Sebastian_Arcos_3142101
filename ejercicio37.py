def numeros_impares(lista):
    resultado = []
    for numero in lista:
        if numero % 2 != 0:
            resultado.append(numero)
    return resultado

# Input del usuario
numeros = input("Ingresa números separados por espacios: ")
lista = [int(x) for x in numeros.split()]

# Llamar la función y mostrar resultado
impares = numeros_impares(lista)
print("Números impares:", impares)