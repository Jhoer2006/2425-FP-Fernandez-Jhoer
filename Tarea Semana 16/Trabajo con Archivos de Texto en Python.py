# Escritura de Archivo de Texto
# Se crea y escribe en el archivo "my_notes.txt"
with open("my_notes.txt", "w") as file:
    file.write("Primera nota: Aprender a manejar archivos en Python.\n")
    file.write("Segunda nota: Practicando la lectura y escritura de archivos.\n")
    file.write("Tercera nota: Cerrando archivos correctamente porque es muy importante.\n")

# Lectura de Archivo de Texto
# Se abre el archivo en modo lectura y se leen las líneas una por una
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() elimina los saltos de línea adicionales
