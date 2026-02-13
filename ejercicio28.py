#Creamos la funcion para convertir °c a °f, recibimos como parametro °C
def calcularFarenheith(c):
    return (1.8 * c) + 32
#Pedimos la temperatura
c = int(input("Ingrese la temperatura en grados centigrados: "))
#Imprimimos directamente la funcion
print(f"la temperatura de {c}°c es {calcularFarenheith(c)}°f, en Farenheith")