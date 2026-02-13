try :

    l = int(input("Ingrese el lado de el cuadrado: "))
    a = l*l
    p = 12+12+12+12

except ValueError:

    print("Error: El dato ingresado no es un número entero.")


print(f"El area del cuadrado es de: {a}cm2 \nSu perimetro es de: {p}cm")