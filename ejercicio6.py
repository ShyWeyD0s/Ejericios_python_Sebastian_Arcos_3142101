#Perimetro triangulo equilatero
#Importamos math para poder hacer las raices
import math
#Creamos variables e ingresamps datos
h = float(input("Ingrese la altura del triangulo: "))
#hacemos operacion para obtener el lado, ya que para su perimetro necesitamos de un lado
l = (2*h)/math.sqrt(3)
#Hacemos operacion para el perimetro
p = 3*l
#Imprimimos en consola el valor
print("El valor del perimeto del triangulo con altura",h, "es: ",p, "Y su lados son: ",l)
