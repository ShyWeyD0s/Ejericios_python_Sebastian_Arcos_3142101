notas = []
opc = ""
#Bucle while para ejecutarse mientras la opcion no sea while
while opc != "fin":
    nota = int(input("Agregue una nota: "))
    notas.append(nota)
    opc = input("Si desea dejar de añadir notas escriba fin: ")
#Nos imprime la cantidad de notas
print("La cantidad de notas es:", len(notas))
#Bucle para sumar cada nota
suma = 0
for x in notas:
    suma += x #Cada nota se asigna y suma en la variable suma
#la media va a ser igual a la suma dividido entre el tamaño de la lista o cantidad de numeros
media = suma / len(notas)
print("El promedio de las notas es:", media)










