import random #Importamos la libreria de random para poder implementar un numeor aleatorio a la variable

x = random.randint(1, 15)#llamamos a la funcion y establecemos un limite a la variable
n = int(input("Adivine el numero del 1 al 15: "))
intentos = 0

while  n != x :

    if n > x:

        print("El numero a adivinar es menor, intente otra vez")
        n = int(input("Adivine el numero: "))
        intentos += 1


    elif n < x:

        print("El numero a adivinar es mayor, intente otra vez")
        n = int(input("Adivine el numero: "))
        intentos += 1

#Extra, para saber que tan bien le fue al usuario, condicional if
print(f"El numero es {x}, correcto!!! ")
if intentos <= 2:
    print(f"Su numero de intentos fue: {intentos}, :o ¿Eres adivino?")

else :
    print(f"Su numero de intentos fue: {intentos}, D: que horror!!")


