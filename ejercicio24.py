# primera entrada
texto = input("Ingrese un texto en minusculas: ")

# bucle se ejecuta mientras .islower() sea Falso
# Usamos not para invertir el valor booleano
while not texto.islower():
    print("Error: El texto contiene mayúsculas o no tiene solo letras minúsculas.")
    texto = input("Por favor, escríbalo de nuevo solo en minúsculas: ")

#Imprimimos al salir del bucle para comunicar que el texto cumple con las caracteristicas
print("Gracias, el texto ingresado está en minúsculas.")