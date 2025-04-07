from libro import Libro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # {ISBN: Libro}
        self.usuarios_registrados = {}  # {ID: Usuario}
        self.ids_usuarios = set()  # Para verificar unicidad de ID

    def agregar_libro(self, libro):
        if libro.isbn in self.libros_disponibles:
            print("❌ El libro ya existe.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print("✅ Libro agregado.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print("✅ Libro eliminado.")
        else:
            print("❌ Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("❌ ID de usuario ya registrado.")
        else:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("✅ Usuario registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("✅ Usuario eliminado.")
        else:
            print("❌ Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros_disponibles:
            print("❌ Libro no disponible.")
            return
        if id_usuario not in self.usuarios_registrados:
            print("❌ Usuario no registrado.")
            return
        libro = self.libros_disponibles.pop(isbn)
        self.usuarios_registrados[id_usuario].libros_prestados.append(libro)
        print("📚 Libro prestado con éxito.")

    def devolver_libro(self, isbn, id_usuario):
        usuario = self.usuarios_registrados.get(id_usuario)
        if not usuario:
            print("❌ Usuario no registrado.")
            return
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print("📦 Libro devuelto.")
                return
        print("❌ El usuario no tiene este libro.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == 'titulo' and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == 'autor' and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == 'categoria' and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("🔍 No se encontraron libros.")

    def listar_prestamos_usuario(self, id_usuario):
        usuario = self.usuarios_registrados.get(id_usuario)
        if usuario:
            if usuario.libros_prestados:
                print(f"📚 Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("📭 No tiene libros prestados.")
        else:
            print("❌ Usuario no registrado.")
