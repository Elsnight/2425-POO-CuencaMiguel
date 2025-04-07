import tkinter as tk
from tkinter import messagebox, font

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📋 Lista de Tareas")

        # Fuente tachada
        self.font_normal = font.Font(family="Helvetica", size=12)
        self.font_tachado = font.Font(family="Helvetica", size=12, overstrike=1)

        # Entrada de tarea
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.agregar_tarea())

        # Listbox para mostrar tareas
        self.lista_tareas = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.lista_tareas.pack()
        self.lista_tareas.bind("<Double-1>", lambda event: self.marcar_completada())

        # Diccionario para guardar estado de completado
        self.estado_tareas = {}  # índice -> bool

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="➕ Añadir Tarea", command=self.agregar_tarea).pack(side="left", padx=5)
        tk.Button(btn_frame, text="✅ Marcar como Completada", command=self.marcar_completada).pack(side="left", padx=5)
        tk.Button(btn_frame, text="🗑️ Eliminar Tarea", command=self.eliminar_tarea).pack(side="left", padx=5)

    def agregar_tarea(self):
        texto = self.entry.get().strip()
        if texto:
            self.lista_tareas.insert(tk.END, texto)
            idx = self.lista_tareas.size() - 1
            self.estado_tareas[idx] = False
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Escribe una tarea antes de añadirla.")

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            idx = seleccion[0]
            actual = self.lista_tareas.get(idx)
            completada = self.estado_tareas.get(idx, False)

            if not completada:
                self.lista_tareas.itemconfig(idx, fg="gray", font=self.font_tachado)
                self.estado_tareas[idx] = True
            else:
                self.lista_tareas.itemconfig(idx, fg="black", font=self.font_normal)
                self.estado_tareas[idx] = False
        else:
            messagebox.showinfo("Selecciona una tarea", "Debes seleccionar una tarea para marcarla.")

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            idx = seleccion[0]
            self.lista_tareas.delete(idx)
            del self.estado_tareas[idx]
            self.estado_tareas = {i: self.estado_tareas.get(i + 1, False) for i in range(self.lista_tareas.size())}
        else:
            messagebox.showinfo("Selecciona una tarea", "Debes seleccionar una tarea para eliminarla.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
