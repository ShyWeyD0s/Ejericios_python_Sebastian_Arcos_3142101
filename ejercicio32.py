#Creamos la funcion para evaluar si una lista es mas larga que otra, y los parametros ingresados seran las listas
def masLarga(list1, list2):
    if len(list1) > len(list2):
        return f"La lista1: {list1} es más grande que la lista2: {list2}"
    elif len(list1) < len(list2):
        return f"La lista2: {list2} es más grande que la lista1: {list1}"
    else:
        return "Las listas tienen la misma cantidad de datos"
#inicializamos las listas
list1 = []
list2 = []

#bucle para llenar lista 1
while True:
    dato = input("Ingrese dato para lista 1 o 'salir' para terminar: ")
    if dato.lower() == "salir":
        break
    list1.append(dato)
#bucle para llenar lista 2
while True:
    dato = input("Ingrese dato para lista 2 o 'salir' para terminar: ")
    if dato.lower() == "salir":
        break
    list2.append(dato)

#imprimimos y llamamos a la funcion
print("\n" + masLarga(list1, list2))









