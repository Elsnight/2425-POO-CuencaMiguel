import time

class UserSession:
    """
    Clase que gestiona la sesión de un usuario.
    """

    def __init__(self, username):
        """
        Constructor: Inicia sesión del usuario.

        :param username: Nombre del usuario.
        """
        self.username = username
        self.logged_in = True
        print(f"🔓 Usuario '{self.username}' ha iniciado sesión.")

    def get_profile(self):
        """
        Simula la obtención de datos del perfil del usuario.
        """
        if self.logged_in:
            print(f"👤 Mostrando perfil de '{self.username}'...")
            time.sleep(1)  # Simula el tiempo de consulta
            print(f"📄 Datos de usuario: Nombre: {self.username}, Estado: Activo")
        else:
            print("❌ Error: Usuario no ha iniciado sesión.")

    def __del__(self):
        """
        Destructor: Cierra sesión automáticamente cuando el objeto se destruye.
        """
        if self.logged_in:
            self.logged_in = False
            print(f"🔒 Usuario '{self.username}' ha cerrado sesión.")

# --------------- Ejemplo de uso ---------------

# Crear un objeto UserSession (usuario inicia sesión)
user1 = UserSession("JuanPerez")

# Consultar perfil del usuario
user1.get_profile()

# Eliminar la referencia al objeto (desencadena el destructor)
del user1

# Fin del programa: La sesión del usuario se cierra automáticamente
