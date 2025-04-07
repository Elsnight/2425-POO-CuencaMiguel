from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario

def main():
    biblio = Biblioteca()

    # Agregar libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "1234")
    libro2 = Libro("1984", "George Orwell", "Distopía", "5678")
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Ana López", "u001")
    usuario2 = Usuario("Carlos Pérez", "u002")
    biblio.registrar_usuario(usuario1)
    biblio.registrar_usuario(usuario2)

    # Préstamos
    biblio.prestar_libro("1234", "u001")
    biblio.listar_prestamos_usuario("u001")

    # Devolución
    biblio.devolver_libro("1234", "u001")
    biblio.listar_prestamos_usuario("u001")

    # Buscar libros
    biblio.buscar_libros("autor", "Orwell")

    # Baja usuario
    biblio.dar_baja_usuario("u002")

if __name__ == "__main__":
    main()
