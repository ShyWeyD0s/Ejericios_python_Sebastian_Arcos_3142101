#Creamos una lista con un indice extra para poder ser evaluados
num = [0, 0, 0, 0]
#con un bucle for llenamos los datos de la lista, en este caso 3
for x in range(3):
    num[x] = int(input("Ingrese 3 numeros enteros"))
    if num[x] <0:
        print("Error, el numero tiene que se entero positivo")
        break #break por si ingresa un numero negativo
#imprimimos cada numero en la lista
for x in range(3):
    #aqui evaluamos el numero en la posicion actual y el numero en la siguiente posicion (+1)
    if num[x] > num[x+1]:
        print("El numero",num[x]," es mayor a ",num[x+1])
    else:
        print("El numero", num[x], " es menor a ", num[x + 1])