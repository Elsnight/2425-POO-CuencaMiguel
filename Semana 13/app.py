import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📋 Gestor de Lista de Datos")

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese un dato:")
        self.label.pack(pady=5)

        # Campo de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Botón Agregar
        self.boton_agregar = tk.Button(root, text="Agregar", command=self.agregar_dato)
        self.boton_agregar.pack(pady=5)

        # Lista de datos
        self.lista_datos = tk.Listbox(root, width=50, height=10)
        self.lista_datos.pack(pady=10)

        # Botón Limpiar
        self.boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_dato)
        self.boton_limpiar.pack(pady=5)

    def agregar_dato(self):
        texto = self.entry.get().strip()
        if texto:
            self.lista_datos.insert(tk.END, texto)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "⚠️ Por favor ingrese un dato válido.")

    def limpiar_dato(self):
        seleccion = self.lista_datos.curselection()
        if seleccion:
            self.lista_datos.delete(seleccion)
        else:
            self.lista_datos.delete(0, tk.END)  # Si no hay selección, limpiar toda la lista
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
