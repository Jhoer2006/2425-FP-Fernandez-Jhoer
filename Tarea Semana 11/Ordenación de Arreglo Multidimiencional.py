def bubble_sort(fila):
    """Ordena una lista usando el algoritmo Bubble Sort."""
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de valores
    return fila


def mostrar_matriz(m):
    """Imprime la matriz de forma legible."""
    for fila in m:
        print(fila)
    print()


# Definir la matriz 3x3
matriz = [
    [9, 2, 7],
    [5, 1, 6],
    [8, 3, 4]
]

# Mostrar la matriz original
print("Matriz original:")
mostrar_matriz(matriz)

# Elegir la fila a ordenar (ejemplo: fila 1)
fila_a_ordenar = 1  # Índice 1 (segunda fila)

# Ordenar la fila específica
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar][:])  # Copia de la fila

# Mostrar la matriz con la fila ordenada
print(f"Matriz con la fila {fila_a_ordenar} ordenada:")
mostrar_matriz(matriz)
