# Inicializamos una lista vacía para los números ganadores
numeros_ganadores = []

# Pedimos al usuario que ingrese los números ganadores
print("Introduce los números ganadores de la lotería primitiva (uno por uno):")
for i in range(6):  # Suponiendo que son 6 números ganadores
    while True:
        try:
            numero = int(input(f"Número {i + 1}: "))
            if numero < 1 or numero > 49:  # Validamos que el número esté en el rango típico de 1 a 49
                print("El número debe estar entre 1 y 49. Inténtalo de nuevo.")
            elif numero in numeros_ganadores:  # Evitamos números repetidos
                print("Este número ya ha sido ingresado. Por favor, introduce otro.")
            else:
                numeros_ganadores.append(numero)
                break
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

# Ordenamos la lista de números ganadores
numeros_ganadores.sort()

# Mostramos los números ganadores ordenados
print("\nLos números ganadores, ordenados de menor a mayor, son:")
print(numeros_ganadores)
