# Aplicación de Principios SOLID en el código

# Principio de Responsabilidad Única (SRP): Cada clase tiene una única responsabilidad
# Principio de Abierto/Cerrado (OCP): Las clases están abiertas para extensión, pero cerradas para modificación
# Principio de Sustitución de Liskov (LSP): Se pueden usar instancias de clases derivadas sin afectar la funcionalidad
# Principio de Segregación de Interfaces (ISP): No aplicable en este caso porque no tenemos interfaces
# Principio de Inversión de Dependencias (DIP): Usamos la superclase para definir una interfaz común

# Definición de una interfaz para representar una entidad con información
from abc import ABC, abstractmethod

class Informable(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

# Definición de la clase base (superclase)
class Persona(Informable):
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo encapsulado (con un guion bajo para indicar uso interno)
        self._edad = edad  # Atributo encapsulado
    
    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"
    
    def hablar(self):
        return "Hola, soy una persona."

# Clase derivada (herencia de Persona)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.carrera = carrera  # Nuevo atributo exclusivo de Estudiante
    
    # Polimorfismo: Sobrescribiendo el método hablar
    def hablar(self):
        return f"Hola, soy un estudiante de {self.carrera}."
    
    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Carrera: {self.carrera}"

# Separación de responsabilidades en la gestión de cuentas bancarias
class TransaccionBancaria(ABC):
    @abstractmethod
    def ejecutar(self, cantidad):
        pass

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular  # Atributo encapsulado
        self.__saldo = saldo  # Atributo privado (doble guion bajo para indicar ocultamiento)
    
    def mostrar_saldo(self):
        return f"Saldo actual: ${self.__saldo}"

    def _actualizar_saldo(self, cantidad):
        self.__saldo += cantidad

class Deposito(TransaccionBancaria):
    def __init__(self, cuenta):
        self.cuenta = cuenta
    
    def ejecutar(self, cantidad):
        if cantidad > 0:
            self.cuenta._actualizar_saldo(cantidad)
            return f"Depósito exitoso. Nuevo saldo: {self.cuenta.mostrar_saldo()}"
        return "Cantidad inválida."

class Retiro(TransaccionBancaria):
    def __init__(self, cuenta):
        self.cuenta = cuenta
    
    def ejecutar(self, cantidad):
        if 0 < cantidad <= self.cuenta._CuentaBancaria__saldo:
            self.cuenta._actualizar_saldo(-cantidad)
            return f"Retiro exitoso. Nuevo saldo: {self.cuenta.mostrar_saldo()}"
        return "Fondos insuficientes."

# Creación de instancias y demostración de funcionalidad
persona = Persona("Carlos", 40)
estudiante = Estudiante("Ana", 22, "Ingeniería")
cuenta = CuentaBancaria("Luis", 1000)
deposito = Deposito(cuenta)
retiro = Retiro(cuenta)

# Uso de métodos
print(persona.mostrar_info())  # Nombre: Carlos, Edad: 40
print(persona.hablar())        # Hola, soy una persona.
print(estudiante.mostrar_info())  # Nombre: Ana, Edad: 22, Carrera: Ingeniería
print(estudiante.hablar())        # Hola, soy un estudiante de Ingeniería.
print(deposito.ejecutar(500))  # Depósito exitoso
print(retiro.ejecutar(300))    # Retiro exitoso
print(cuenta.mostrar_saldo()) # Muestra el saldo actual
print(retiro.ejecutar(800))    # Fondos insuficientes