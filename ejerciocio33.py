def cadena_mas_larga(lista_cadenas):
    """
    Devuelve la cadena más larga de una lista.
    Si hay varias del mismo largo, devuelve cualquiera de ellas.
    
    Args:
        lista_cadenas: Lista de strings
    
    Returns:
        String: La cadena más larga
    """
    return max(lista_cadenas, key=len)


# Ejemplo de uso
nombres = ['Pepe', 'Juan', 'María', 'Ana']
resultado = cadena_mas_larga(nombres)
print(resultado)  # Salida: María