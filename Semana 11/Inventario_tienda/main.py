from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()
    archivo = 'inventario.json'
    inventario.cargar_desde_archivo(archivo)

    while True:
        print("\n📋 MENÚ DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("👉 Seleccione una opción: ")

        if opcion == '1':
            try:
                id_producto = input("🆔 ID del producto: ")
                nombre = input("📦 Nombre: ")
                cantidad = int(input("📦 Cantidad: "))
                precio = float(input("💰 Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcion == '2':
            id_producto = input("🆔 ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("🆔 ID del producto a actualizar: ")
            cantidad = input("📦 Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("💰 Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            nombre = input("🔍 Nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)
        elif opcion == '5':
            inventario.mostrar_todos()
        elif opcion == '6':
            inventario.guardar_en_archivo(archivo)
        elif opcion == '7':
            inventario.guardar_en_archivo(archivo)
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
