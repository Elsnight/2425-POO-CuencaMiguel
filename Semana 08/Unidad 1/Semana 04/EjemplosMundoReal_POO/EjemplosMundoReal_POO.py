# SOLID aplicado: Responsabilidad Única (Single Responsibility Principle)
# Esta clase representa una habitación en el hotel.
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False

    def reservar(self):
        """Marca la habitación como reservada."""
        if not self.reservada:
            self.reservada = True
            return True
        return False

    def liberar(self):
        """Libera la habitación."""
        if self.reservada:
            self.reservada = False
            return True
        return False


# SOLID aplicado: Abierto/Cerrado (Open/Closed Principle)
# La clase Hotel puede extenderse fácilmente sin modificar el código existente.
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """Agrega una nueva habitación al hotel."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        """Muestra habitaciones no reservadas."""
        disponibles = [hab for hab in self.habitaciones if not hab.reservada]
        if disponibles:
            print("\nHabitaciones disponibles:")
            for hab in disponibles:
                print(f"- Número {hab.numero}, Tipo: {hab.tipo}, Precio: ${hab.precio}")
        else:
            print("\nNo hay habitaciones disponibles.")

    def buscar_habitacion_por_numero(self, numero):
        """Busca una habitación por su número."""
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                return habitacion
        return None


# Función principal para la interacción con el usuario
def menu_interactivo():
    # Crear un hotel con habitaciones de ejemplo
    hotel = Hotel("Hotel Interactivo POO")
    hotel.agregar_habitacion(Habitacion(101, "Simple", 50))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 80))
    hotel.agregar_habitacion(Habitacion(103, "Suite", 150))

    while True:
        print("\n--- Menú ---")
        print("1. Mostrar habitaciones disponibles")
        print("2. Reservar una habitación")
        print("3. Liberar una habitación")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            hotel.mostrar_habitaciones_disponibles()
        elif opcion == "2":
            try:
                numero = int(input("Ingrese el número de la habitación que desea reservar: "))
                habitacion = hotel.buscar_habitacion_por_numero(numero)
                if habitacion:
                    if habitacion.reservar():
                        print(f"Habitación {numero} reservada con éxito.")
                    else:
                        print(f"La habitación {numero} ya está reservada.")
                else:
                    print("Número de habitación inválido.")
            except ValueError:
                print("Debe ingresar un número válido.")
        elif opcion == "3":
            try:
                numero = int(input("Ingrese el número de la habitación que desea liberar: "))
                habitacion = hotel.buscar_habitacion_por_numero(numero)
                if habitacion:
                    if habitacion.liberar():
                        print(f"Habitación {numero} liberada con éxito.")
                    else:
                        print(f"La habitación {numero} ya está disponible.")
                else:
                    print("Número de habitación inválido.")
            except ValueError:
                print("Debe ingresar un número válido.")
        elif opcion == "4":
            print("¡Gracias por usar el sistema del hotel!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el menú interactivo si el archivo es ejecutado directamente
if __name__ == "__main__":
    menu_interactivo()
