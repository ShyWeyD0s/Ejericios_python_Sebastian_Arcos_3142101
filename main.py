#Crear variable para guardar la entrada en una variable
entrada1 = input("Igrese el dato 1")
entrada2 = input("Igrese el dato 2")
#Tenemos que siempre convertir la entrada al tipo de dato deseado
entero1 = int(entrada1)
entero2 = int(entrada2)
print("los datos son", entero1, entero2)
#Listas
lista = [1, 2, 3, 4, 5]
#para agregar
lista.append(10)
#para eliminar por indice
lista.remove(2)
#para ordenar una lista
lista.sort()
print(lista)
print(lista[0], "Posicion 0 de la lista (p")
#extraer un rango
rango = lista[1:5]
print("El rango es: ", lista)
#Para saber el tamañi
len(lista)
#Matrices
userA = ["Juan","123-234"]
userB = ["Pedro","345-746"]
Agenda = []
Agenda.append(userA)
Agenda.append(userB)
#Imprimir posiciones
print(Agenda)
        #Col 0   -   #Col 1
#fila 0= [["Juan","123-234"],
#dila 1= ["Pedro","345-746"]]
print(Agenda[0][0]) # Juan
print(Agenda[1][1]) # 345-746
#Bucle for
num = [1,3,5,2,4,7,8,6,9]
for x in num: #Por cada elemento en num:
    print(num) #Recordar indentacion
#Bucle while
i = 1
while i < 10:
    print(i)
    i = i + 1
#Declarar funciones
def mi_funcion(param1, param2):
    print(param1)
    print(param2)
mi_funcion("hola", 2)

