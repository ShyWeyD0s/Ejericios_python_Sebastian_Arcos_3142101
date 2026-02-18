def min_max(numeros):
    if not numeros:
        return None, None
    
    return min(numeros), max(numeros)


# Entrada de usuario
entrada = input("Ingresa números separados por espacios: ")
lista = list(map(int, entrada.split()))

minimo, maximo = min_max(lista)
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")