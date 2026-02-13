vector = [] #Inicializamos el vector vacio

for i in range(15): #El bucle le dara la longitud a la lista/vector(15) en el bucle for

    vector.append(int(input("Agrege datos numericos al vector: ")))

par = []# inicializamos la lista donde se van a guardar los numeros pares
impar = []# inicializamos la lista donde se van a guardar los numeros impares

for x in vector: #Por cada elemento en el vector (15)

    if x%2 == 0: #Bucle que evalua si el residuo es igual a 0 para saber si es par

        par.append(x) #Si cumple la condicion lo agregamos en la lista de pares

    else : # si no se cumple, es impar

        impar.append(x)


print("Los numeros pares son: ", par,
    "\nlos numeros impares son: ", impar)

if len(par) > len(impar):

    print(" la lista de Pares es mayor")

elif len(impar) > len(par):

    print(" la lista de Impares es mayor ")

else:

    print("Pares e impares son iguales")


print("La longitud de los pares es: ", len(par), " La longitud de los impares es: ", len(impar))


