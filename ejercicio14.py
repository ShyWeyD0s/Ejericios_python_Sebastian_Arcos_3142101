#Inicializamos la lista para guardar los resultados finales en Celsius
temperaturas = [0.0] * 5 #Si multiplicamos la lista por 5 podremos crear 5 posiciones


#Creamos la funcion pra convertir de f a c
def calcular_celsius(f):
    return (f - 32) * 5 / 9


for x in range(5):
    opc = int(input("Su temperatura está en Fahrenheit?\n1) Sí  2) No: "))
    if opc == 1:
        f = float(input("Ingrese la temperatura en °F: "))
        c = calcular_celsius(f)
        print(f"{f}°F equivalen a {c:.2f}°C")
    else:
        c = float(input("Ingrese la temperatura en °C: "))
        print(f"Registrado como {c}°C")
    #Guardamos
    temperaturas[x] = c
#mostramos la lista completa
print("Temperaturas registradas (°C):")
print(temperaturas)

sumaTotal = 0

#por cada temperatura realizamos la suma y el promedio con la ayuda de un bucle for
for t in temperaturas:
    sumaTotal += t
cantidad_dias = len(temperaturas)
promedio = sumaTotal / cantidad_dias

#resultado del promedio
print("La temperatura media es, ", promedio)

#Con un bucle for en cada temperatura evaluamos si la temperatura es mayor al promedio
for t in temperaturas:
    if t > promedio:
        print("La temperatura de, ", t, "°c Fue la mas alta en el promedio")
    else:
        print("La temperatura de, ", t, "°c No sobrepasa el promedio de todas las temperaturas: ", promedio)




