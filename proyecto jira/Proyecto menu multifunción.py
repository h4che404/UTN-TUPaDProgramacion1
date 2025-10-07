import tkinter as tk

def abrir_calculadora():
 import tkinter as tk

def abrir_calculadora():
    # Crear la ventana de calculadora
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Calculadora")
    ventana_secundaria.geometry("300x450")

    # Variable vinculada al cuadro de texto
    entrada_var = tk.StringVar()

    # Cuadro de texto (solo lectura)
    entrada = tk.Entry(ventana_secundaria, textvariable=entrada_var, font=("Arial", 20), justify="right")
    entrada.pack(pady=10, fill="x", padx=10)

    # Función para agregar contenido al cuadro
    def agregar(valor):
        entrada_var.set(entrada_var.get() + str(valor))

    # Función para calcular el resultado
    def calcular():
        try:
            resultado = eval(entrada_var.get())  # eval evalúa la expresión matemática
            entrada_var.set(str(resultado))
        except:
            entrada_var.set("Error")

    # Función para limpiar
    def limpiar():
        entrada_var.set("")

    # Frame para los botones
    frame_botones = tk.Frame(ventana_secundaria)
    frame_botones.pack()

    # Botones de números (1–9)
    for i in range(1, 10):
        boton = tk.Button(frame_botones, text=str(i), font=("Arial", 16), width=5, height=2,
                          command=lambda n=i: agregar(n))
        boton.grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)

    # Botón 0
    boton_cero = tk.Button(frame_botones, text="0", font=("Arial", 16), width=5, height=2,
                           command=lambda: agregar(0))
    boton_cero.grid(row=3, column=0, padx=5, pady=5)

    # Botón limpiar
    boton_clear = tk.Button(frame_botones, text="C", font=("Arial", 16), width=5, height=2, command=limpiar)
    boton_clear.grid(row=3, column=1, padx=5, pady=5)

    # Botón igual
    boton_igual = tk.Button(frame_botones, text="=", font=("Arial", 16), width=5, height=2, command=calcular)
    boton_igual.grid(row=3, column=2, padx=5, pady=5)

    # Operadores
    operadores = ["+", "-", "*", "/"]
    for i, op in enumerate(operadores):
        boton = tk.Button(frame_botones, text=op, font=("Arial", 16), width=5, height=2,
                          command=lambda o=op: agregar(o))
        boton.grid(row=i, column=3, padx=5, pady=5)

    # Botón para cerrar
    tk.Button(ventana_secundaria, text="Cerrar", command=ventana_secundaria.destroy).pack(pady=10)

# Ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Menú multifunción")
ventana_principal.geometry("500x500")

tk.Label(ventana_principal, text="Opciones:").pack(pady=20)
tk.Button(ventana_principal, text="Abrir calculadora", command=abrir_calculadora).pack(pady=10)

ventana_principal.mainloop()
