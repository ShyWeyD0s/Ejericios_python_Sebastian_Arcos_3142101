

x = int(input("Ingrese un numero el 1 al 10: "))
i = 10


while x != True:
    if x > 10 :
        print(f"El numero{x} es mayor al rango permitido")
        x = int(input("Ingrese un numero el 1 al 10: "))
    elif x <= 0 :
        print(f"El numero{x} es menor al rango permitido")
        x = int(input("Ingrese un numero el 1 al 10: "))
    else :
        x = True


print("Gracias, el numero ingresado si fue valido")