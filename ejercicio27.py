#Creamos la funcion pra alcular el area y colocamos como prametro la variable r
def areaCirculo(r):
    return 3.1416*r*r #el return nos devolverá la operacion, se usa en funciones

r = float(input(" Ingrese el area del circulo: ")) #Ingresamos el area en la variable r
print("-"*40)
print(f"El area del circulo con radio {r} es: ", areaCirculo(r)) #llamamos a la funcion e imprimimos el resultado, en este caso ingresamos como parametro el r