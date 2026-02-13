vector = [1, 3, 4, 6, 7] #Inicializamos el vector de 5 posiciones
try: #Try por si se añade un valor incorrecto
    x = int(input("Ingrese un nuevo elemento para agregar al vector: "))
    #Buscamos la posición donde debe ir x
    i = 0
    while i < len(vector) and vector[i] < x:
        i += 1
    #Insertamos en esa posición específica
    vector.insert(i, x)
    print("Vector en orden ascendente:", vector)
except ValueError:
    print("Error: El dato ingresado no es un número entero.")