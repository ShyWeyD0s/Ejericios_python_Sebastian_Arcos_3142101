
def mediaNumeros(num): #Creamos la funcion para calcular la media
    return sum(num)/len(num)


num = [0]*5 #Creamos la lista de longitud 5

#Bucle para llenar los numeros en la lista
for i in range(len(num)):
    num[i] = int(input(f"Ingrese el número para la posición {i + 1}: "))

print(f"la media de los numeros {num} es: ", mediaNumeros(num))