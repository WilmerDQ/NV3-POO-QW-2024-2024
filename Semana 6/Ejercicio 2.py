import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_fuera_de_rango(self, min_valor, max_valor):
        actual = self.cabeza
        previo = None

        while actual is not None:
            if actual.valor < min_valor or actual.valor > max_valor:
                if previo is None:  # Si es el primer nodo
                    self.cabeza = actual.siguiente
                else:
                    previo.siguiente = actual.siguiente
            else:
                previo = actual
            actual = actual.siguiente

    def imprimir(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Crear lista enlazada y agregar 50 números aleatorios entre 1 y 999
lista = ListaEnlazada()
for _ in range(50):
    lista.agregar(random.randint(1, 999))

# Imprimir lista original
print("Lista original:")
lista.imprimir()

# Leer el rango desde el teclado
min_valor = int(input("Introduce el valor mínimo del rango: "))
max_valor = int(input("Introduce el valor máximo del rango: "))

# Eliminar nodos fuera del rango
lista.eliminar_fuera_de_rango(min_valor, max_valor)

# Imprimir lista después de eliminar los nodos fuera del rango
print("Lista después de eliminar los nodos fuera del rango:")
lista.imprimir()
