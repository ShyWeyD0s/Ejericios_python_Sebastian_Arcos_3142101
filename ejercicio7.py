#Creamos una lista vacia de tamaño 3
num = [0, 0, 0]
#creamos una variable para el resultado de la operación
sum = 0
#Creamos un bucle for para llenar los datos
for x in range(3):
    num[x] = int(input("Ingrese 3 numeros enteros: "))
#condicional para si el numero es negativo
if num[0] < 0:
    sum = num[0]*num[1]*num[2]
    print("Como el primer numero es negativo. El resultado del producto de los numeros es: ", sum)
#condicional si el primer numero no cumple la primera condicion
else:
    sum = num[0]+num[1]+num[2]
    print("Como el primer numero es positivo. El resultado de la suma de los numeros es: ", sum)



