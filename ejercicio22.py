try :#Try para evitar datos erroneos

    #Inicializamos las variables
    l = int(input("Ingrese el lado de el cuadrado en cm: "))
    a = l*l
    p = 12+12+12+12

#Si detecta un exc le mostramos el tipo de error
except ValueError:

    print("Error: El dato ingresado no es un número entero.")

#con una f string imprimimos el area y su perimetro
print(f"El area del cuadrado es de: {a}cm2 \nSu perimetro es de: {p}cm")