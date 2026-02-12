#Calcular cuantos de 10 numeros son pares
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
op = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_pares = 0

#Bucle for para llenar la lista de tamaño 10
for x in range(10):
    num[x] = int(input("Ingrese 10 numeros: "))

#Bucle for para evaluar cada
for x in range(10):
    op = num[x]%2
    if op == 0:
        print("El numero,", num[x], "es par")
        total_pares+=1
    else:
        print("El numero,", num[x], "es impar")
print("El numero total de pares es: ", total_pares)






