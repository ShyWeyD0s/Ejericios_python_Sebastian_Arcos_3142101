for i in range(7): #como el maximo numero que puede aparecer en una ficha de domino es 6, establecemos 7 como el limite
    for j in range(i, 7): # j va a ser el segundo digito de las fichas
        print(f"[{i}|{j}]")# usamos el f strnig para poder crear una visual de las fichas
        print("-----")#espacio para separar fichas
