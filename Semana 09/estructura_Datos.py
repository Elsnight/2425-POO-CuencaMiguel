class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = []
    
    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        if any(p.id_producto == id_producto for p in self.productos):
            print("Error: ID de producto ya existente.")
            return
        self.productos.append(Producto(id_producto, nombre, cantidad, precio))
        print("Producto añadido con éxito.")
    
    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado con éxito.")
    
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                print("Producto actualizado con éxito.")
                return
        print("Error: Producto no encontrado.")
    
    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")
    
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)

def menu():
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(id_producto, nombre, cantidad, precio)
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (dejar en blanco si no cambia): ")
            nuevo_precio = input("Nuevo precio (dejar en blanco si no cambia): ")
            
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu()
