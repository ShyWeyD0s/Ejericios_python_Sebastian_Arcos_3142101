
#inicializamos la variable que guarda el numero y el rango limite
x = int(input("Ingrese un numero el 1 al 10: "))
i = 10

#si x no es true se pedirá nuevamente el numero
while x != True:

    #condicionales para evaluar si el numero excede el limite
    if x > 10 :

        print(f"El numero{x} es mayor al rango permitido")
        x = int(input("Ingrese un numero el 1 al 10: "))

    elif x <= 0 :

        print(f"El numero{x} es menor al rango permitido")
        x = int(input("Ingrese un numero el 1 al 10: "))

    #Si el numero no excede el numero, la variable x tomara el valor boolean de True, lo que cuplira la condicion y nos sacara del bucle
    else :
        
        x = True

#Le comunicamos al usuario que el dato ingresado si fue valido
print("Gracias, el numero ingresado si fue valido")