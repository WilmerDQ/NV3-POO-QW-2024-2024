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

    def contar_elementos(self):
        contador = 0
        actual = self.cabeza

        while actual is not None:
            contador += 1
            actual = actual.siguiente  # Avanzamos al siguiente nodo

        return contador

# Crear lista y agregar elementos
lista = ListaEnlazada()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

# Imprimir número de elementos
print("Número de elementos en la lista:", lista.contar_elementos())
