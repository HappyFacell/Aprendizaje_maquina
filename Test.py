# Crear la funcion "pares" que devuelva un array o vector de números pares entre dos valores que serán parámetros de la función (inicio, fin)

def pares(inicio, fin):
    resultado = []
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            resultado.append(numero)

    return resultado


print(pares(1, 30))
print(pares(2, 40))
