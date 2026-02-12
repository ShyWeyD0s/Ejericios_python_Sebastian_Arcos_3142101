numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
    lista_digitos = []
    original = numero

    #Extraer los dígitos y guardarlos en la lista
    #ya los deja invertidos
    temp = numero
    while temp > 0:
        digito = temp % 10
        lista_digitos.append(digito)
        temp = temp // 10


    #string vacío y vamos sumando cada dígito convertido a texto
    resultado_texto = ""
    for d in lista_digitos:
        resultado_texto = resultado_texto + str(d)

    #resultados
    print(f"\nNúmero original: {original}")
    print(f"Lista de dígitos: {lista_digitos}")
    print(f"Número invertido: {resultado_texto}")