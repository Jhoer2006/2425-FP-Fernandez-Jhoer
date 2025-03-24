# Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Fernando Sanchez",
    "edad": 25,
    "ciudad": "Shell",
    "profesion": "Ingeniero"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Shell"

# Agregar una nueva clave-valor (en este caso, ya existe "profesion", pero si no existiera, la agregaríamos)
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-789"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final
tipo = "\n".join(f"{clave}: {valor}" for clave, valor in informacion_personal.items())
print(tipo)

