import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🗓️ Agenda Personal")
        self.root.geometry("600x400")

        # Frame superior - Lista de eventos
        self.frame_eventos = tk.Frame(root)
        self.frame_eventos.pack(pady=10, padx=10, fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame_eventos, columns=("fecha", "hora", "descripcion"), show="headings")
        self.tree.heading("fecha", text="📅 Fecha")
        self.tree.heading("hora", text="🕒 Hora")
        self.tree.heading("descripcion", text="📝 Descripción")
        self.tree.pack(fill="both", expand=True)

        # Frame medio - Formulario
        self.frame_form = tk.Frame(root)
        self.frame_form.pack(pady=5)

        tk.Label(self.frame_form, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_form, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_form, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = tk.Entry(self.frame_form, width=10)
        self.hora_entry.grid(row=0, column=3, padx=5)

        tk.Label(self.frame_form, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.frame_form, width=40)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5)

        # Frame inferior - Botones
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        tk.Button(self.frame_botones, text="➕ Agregar Evento", command=self.agregar_evento).pack(side="left", padx=10)
        tk.Button(self.frame_botones, text="❌ Eliminar Seleccionado", command=self.eliminar_evento).pack(side="left", padx=10)
        tk.Button(self.frame_botones, text="🚪 Salir", command=root.quit).pack(side="left", padx=10)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if not (fecha and hora and descripcion):
            messagebox.showwarning("Campos incompletos", "⚠️ Por favor completa todos los campos.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Selecciona un evento", "Debes seleccionar un evento para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
        if confirmacion:
            self.tree.delete(seleccionado)

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
