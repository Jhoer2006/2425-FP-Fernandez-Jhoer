# Función para calcular la temperatura promedio de múltiples ciudades

def calcular_temperatura_promedio(datos):
    """
    Calcula la temperatura promedio de cada ciudad.

    :param datos: Diccionario con ciudades como claves y listas de temperaturas semanales como valores.
    :return: Diccionario con la temperatura promedio de cada ciudad.
    """
    promedios_ciudades = {}
    for ciudad_nombre, temps in datos.items():
        promedio_temp = sum(temps) / len(temps)
        promedios_ciudades[ciudad_nombre] = round(promedio_temp, 2)  # Redondeamos a 2 decimales
    return promedios_ciudades


# Datos de prueba (3 ciudades durante 4 semanas)
datos_ciudades = {
    "Puyo": [30, 32, 29, 31, 28, 30, 33, 27, 29, 31, 30, 32],
    "Shell": [22, 24, 23, 25, 21, 22, 24, 23, 26, 22, 23, 24],
    "Mera": [15, 17, 14, 16, 18, 15, 14, 16, 17, 18, 15, 16]
}

# Ejecutar la función y mostrar los resultados
resultados_promedio = calcular_temperatura_promedio(datos_ciudades)
print("Temperaturas promedio por ciudad:")
for ciudad, temp in resultados_promedio.items():
    print(f"{ciudad}: {temp}°C")
