#Creamos la funcion para saber si en la primera posicion hay minuscula o mayuscula
def mayOmin(cadena):
    #condicional dentro de la funcion para que evalue si tiene o no minusculas
    if cadena[0].islower():
        return (f"El texto, ¨{cadena}¨ tiene minusculas en la primera posicion")
    else:
        return (f"El texto, ¨{cadena}¨ NO tiene minusculas en la primera posicion")



cadena = input("Ingrese su texto: ")
print(mayOmin(cadena))