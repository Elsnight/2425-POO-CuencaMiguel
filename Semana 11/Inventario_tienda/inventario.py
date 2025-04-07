import json
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("❌ ID de producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("✅ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.productos.get(id_producto)
        if producto:
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print("✅ Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            for p in resultados:
                self.mostrar_producto(p)
        else:
            print("🔍 No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            for producto in self.productos.values():
                self.mostrar_producto(producto)

    def mostrar_producto(self, producto):
        print(f"🆔 ID: {producto.id_producto} | 📦 Nombre: {producto.nombre} | Cantidad: {producto.cantidad} | 💰 Precio: ${producto.precio:.2f}")

    def guardar_en_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'w') as archivo:
                data = {id: p.to_dict() for id, p in self.productos.items()}
                json.dump(data, archivo, indent=4)
            print("💾 Inventario guardado exitosamente.")
        except Exception as e:
            print(f"❌ Error al guardar: {e}")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                data = json.load(archivo)
                self.productos = {id: Producto.from_dict(p) for id, p in data.items()}
            print("📂 Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("⚠️ Archivo no encontrado. Se creará un inventario nuevo.")
        except Exception as e:
            print(f"❌ Error al cargar: {e}")
