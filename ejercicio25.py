numeros = []  #Creamos la lista vacía
#Pedimos el primer número y lo guardamos en una variable temporal
nuevoNumero = int(input("Ingrese un numero para añadir, "
                        "\n si quiere dejar de añadir ingrese un negativo para salir: "))

#bucle se ejecuta mientras el último número ingresado sea positivo
while nuevoNumero >= 0:
    numeros.append(nuevoNumero)  #si el numero es mayor o igual a 0 agregamos el nuevo_numero a la lista
    print(f"Lista actual: {numeros}")

    # Pedimos el siguiente número para evaluar en la siguiente vuelta
    nuevoNumero = int(input("Ingrese otro numero: "))


print(f"Bucle finalizado. Ingresaste un número negativo.")
print(f"Los números positivos guardados fueron: {numeros}")