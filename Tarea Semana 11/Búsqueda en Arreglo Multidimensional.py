def buscar_valor(m, valor):
    """
    Busca un valor en la matriz y devuelve su posición si lo encuentra.
    """
    for i in range(len(m)):  # Recorremos las filas
        for j in range(len(m[i])):  # Recorremos las columnas
            if m[i][j] == valor:
                return i, j  # Retorna la posición (fila, columna)
    return None  # Retorna None si no se encuentra el valor


def mostrar_matriz(m):
    """Imprime la matriz de forma legible."""
    for fila in m:
        print(fila)
    print()


# Definir la matriz 3x3
MATRIZ = [  # Ahora usamos 'MATRIZ' en mayúsculas para evitar conflictos
    [4, 8, 3],
    [7, 1, 9],
    [6, 2, 5]
]

# matriz original
print("Matriz:")
mostrar_matriz(MATRIZ)

# Definir el valor a buscar
valor_a_buscar = int(input("Ingrese el valor a buscar: "))

# Buscar el valor en la matriz
posicion = buscar_valor(MATRIZ, valor_a_buscar)

# Obtenemos el resultado
if posicion:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion} (fila {posicion[0]}, columna {posicion[1]}).")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la matriz.")
