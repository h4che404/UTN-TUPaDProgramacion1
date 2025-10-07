import tkinter as tk
from tkinter import messagebox

def opcion1():
    messagebox.showinfo("Opción 1", "Has seleccionado la Opción 1")
def opcion2():
    messagebox.showinfo("Opción 2", "Has seleccionado la Opción 2")
    
ventana = tk.Tk()
ventana.title("Menú Multifunción")

tk.Button(ventana, text="Opción 1", command=opcion1).pack(pady=10)
tk.Button(ventana, text="Opción 2", command=opcion2).pack(pady=10)
tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=10)

ventana.mainloop()