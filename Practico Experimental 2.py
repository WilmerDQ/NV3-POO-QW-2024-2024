class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.numero_asiento = None  # None si aún no tiene asiento.


class Atraccion:
    def __init__(self):
        self.cola = []
        self.asientos = [False] * 30  # True significa ocupado, False libre.
        self.max_asientos = 30

    def agregar_persona(self, persona):
        if len(self.cola) + self.asientos_ocupados() < self.max_asientos:
            self.cola.append(persona)
            print(f"{persona.nombre} ha sido agregado a la cola.")
        else:
            print("No hay asientos disponibles. La cola está cerrada.")

    def asignar_asiento(self):
        if not self.cola:
            print("No hay personas en la cola.")
            return

        for i in range(self.max_asientos):
            if not self.asientos[i]:
                persona = self.cola.pop(0)
                self.asientos[i] = True
                persona.numero_asiento = i + 1
                print(f"{persona.nombre} ha recibido el asiento {persona.numero_asiento}.")
                return

        print("No quedan asientos disponibles.")

    def reporte(self):
        print("\n--- Reporte de Asientos ---")
        for i in range(self.max_asientos):
            estado = "Ocupado" if self.asientos[i] else "Libre"
            print(f"Asiento {i + 1}: {estado}")

        print("\n--- Personas en la cola ---")
        for persona in self.cola:
            print(f"Nombre: {persona.nombre}, Edad: {persona.edad}")

    def asientos_ocupados(self):
        return sum(self.asientos)


# Programa principal
if __name__ == "__main__":
    atraccion = Atraccion()

    # Agregar personas a la cola
    atraccion.agregar_persona(Persona("Juan", 25))
    atraccion.agregar_persona(Persona("María", 30))
    atraccion.agregar_persona(Persona("Pedro", 20))

    # Asignar asientos
    atraccion.asignar_asiento()
    atraccion.asignar_asiento()

    # Mostrar el reporte
    atraccion.reporte()
