#pedimos el numero que deseamos en el que se haga la multiplicacion
x = int(input("ingrese el numero del cual desea saber su tabla de multiplicar: "))
#el bucle se hará hasta multiplicarse por el digito 10
for i in range(11):
    print(x," x ", i, " = ", x*i) #imprimimos en orden de la pocisiones y hacemos la operacion