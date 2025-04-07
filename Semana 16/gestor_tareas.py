import tkinter as tk
from tkinter import messagebox, font

class GestorTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✅ Gestor de Tareas Pendientes")

        # Fuente normal y tachada
        self.font_normal = font.Font(family="Helvetica", size=12)
        self.font_tachado = font.Font(family="Helvetica", size=12, overstrike=1)

        # Campo de entrada
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Listbox de tareas
        self.lista = tk.Listbox(root, width=60, height=12, selectmode=tk.SINGLE)
        self.lista.pack(pady=5)

        # Diccionario para almacenar el estado de tareas
        self.estado = {}  # index: True (completada) / False (pendiente)

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="➕ Añadir", command=self.agregar_tarea).pack(side="left", padx=5)
        tk.Button(btn_frame, text="✅ Completar", command=self.completar_tarea).pack(side="left", padx=5)
        tk.Button(btn_frame, text="🗑️ Eliminar", command=self.eliminar_tarea).pack(side="left", padx=5)

        # Bind de teclas
        root.bind('<Return>', lambda e: self.agregar_tarea())
        root.bind('<c>', lambda e: self.completar_tarea())
        root.bind('<C>', lambda e: self.completar_tarea())
        root.bind('<d>', lambda e: self.eliminar_tarea())
        root.bind('<D>', lambda e: self.eliminar_tarea())
        root.bind('<Delete>', lambda e: self.eliminar_tarea())
        root.bind('<Escape>', lambda e: root.quit())

    def agregar_tarea(self):
        texto = self.entry.get().strip()
        if texto:
            self.lista.insert(tk.END, texto)
            idx = self.lista.size() - 1
            self.estado[idx] = False
            self.entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Entrada vacía", "Escribe una tarea para añadir.")

    def completar_tarea(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            return
        idx = seleccion[0]
        actual = self.lista.get(idx)
        estado_actual = self.estado.get(idx, False)

        if not estado_actual:
            self.lista.itemconfig(idx, fg="gray", font=self.font_tachado)
            self.estado[idx] = True
        else:
            self.lista.itemconfig(idx, fg="black", font=self.font_normal)
            self.estado[idx] = False

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            return
        idx = seleccion[0]
        self.lista.delete(idx)
        del self.estado[idx]
        # Reajustar índices en self.estado
        self.estado = {i: self.estado.get(i + 1, False) for i in range(self.lista.size())}

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareasApp(root)
    root.mainloop()
