class Empleado:
    def __init__(self, id, nombre, cargo, departamento):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.departamento = departamento

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cargo: {self.cargo}, Departamento: {self.departamento}"


class Aporte:
    def __init__(self, empleado_id, monto, fecha):
        self.empleado_id = empleado_id
        self.monto = monto
        self.fecha = fecha

    def __str__(self):
        return f"EmpleadoID: {self.empleado_id}, Monto: ${self.monto:.2f}, Fecha: {self.fecha}"


class RegistroDeAportes:
    def __init__(self):
        self.empleados = []
        self.aportes = []

    def agregar_empleado(self, id, nombre, cargo, departamento):
        self.empleados.append(Empleado(id, nombre, cargo, departamento))
        print("Empleado agregado con éxito.")

    def registrar_aporte(self, empleado_id, monto, fecha):
        empleado = next((e for e in self.empleados if e.id == empleado_id), None)
        if empleado:
            self.aportes.append(Aporte(empleado_id, monto, fecha))
            print("Aporte registrado con éxito.")
        else:
            print("Empleado no encontrado.")

    def consultar_aportes_por_empleado(self, empleado_id):
        empleado = next((e for e in self.empleados if e.id == empleado_id), None)
        if empleado:
            print(f"Aportes para el empleado: {empleado.nombre}")
            for aporte in [a for a in self.aportes if a.empleado_id == empleado_id]:
                print(aporte)
        else:
            print("Empleado no encontrado.")

    def generar_reporte(self):
        print("Reporte de Aportes Totales por Empleado:")
        for empleado in self.empleados:
            total = sum(a.monto for a in self.aportes if a.empleado_id == empleado.id)
            print(f"{empleado.nombre}: ${total:.2f}")


def menu():
    registro = RegistroDeAportes()

    while True:
        print("\n=== Sistema de Registro de Aportes ===")
        print("1. Agregar Empleado")
        print("2. Registrar Aporte")
        print("3. Consultar Aportes por Empleado")
        print("4. Generar Reporte General")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("Ingrese ID del empleado: "))
            nombre = input("Ingrese nombre: ")
            cargo = input("Ingrese cargo: ")
            departamento = input("Ingrese departamento: ")
            registro.agregar_empleado(id, nombre, cargo, departamento)

        elif opcion == "2":
            empleado_id = int(input("Ingrese ID del empleado: "))
            monto = float(input("Ingrese monto del aporte: "))
            fecha = input("Ingrese fecha del aporte (YYYY-MM-DD): ")
            registro.registrar_aporte(empleado_id, monto, fecha)

        elif opcion == "3":
            empleado_id = int(input("Ingrese ID del empleado: "))
            registro.consultar_aportes_por_empleado(empleado_id)

        elif opcion == "4":
            registro.generar_reporte()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()