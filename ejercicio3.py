#Creamos una variable de 3 elementos
respuestas = [0, 0, 0]
#En cada posocion vamos a guardar un tipo de respuesta
respuestas[0] = int(input("Introduzca la cantidad de respuestas correctas: "))
respuestas[1] = int(input("Introduzca la cantidad de respuestas incorrectas: "))
respuestas[2] = int(input("Introduzca la cantidad de respuestas en blanco: "))
print("La cantidad de correctas es: ", respuestas[0], " La cantidad de incorrectas es", respuestas[1], " Las respuestas en blanco son: ", respuestas[2])
#operaciones para calcular  el puntaje total
correctas = respuestas[0]*3
total = correctas - respuestas[1]
print("El puntaje total es de: ", total)






