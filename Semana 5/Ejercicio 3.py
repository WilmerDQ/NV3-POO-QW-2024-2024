# Definimos la lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Creamos un diccionario para almacenar las notas
notas = {}

# Pedimos al usuario que ingrese la nota de cada asignatura
for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")
    notas[asignatura] = nota  # Guardamos la nota en el diccionario

# Mostramos el resultado por pantalla
print("\nTus notas son:")
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")
