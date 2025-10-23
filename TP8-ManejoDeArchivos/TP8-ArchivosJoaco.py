"""
1 - Crear un archivo con 3 productos: lapicera, cuaderno, regla
"""
def crear_archivo_inicial():
    with open("productos.txt", "w") as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,450.0,10\n")
        archivo.write("Regla,80.0,50\n")
    print("Archivo 'productos.txt' creado correctamente.")
"""
Use el modo w que sirve para escribir archivos, en este caso al no existir uno,
crea uno nuevo

Use With open() para que el archivo se cierra automaticamente sin usar close()
"""
"""
2 - Leer y mostrar productos
"""
def leer_y_mostrar_productos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
    except FileNotFoundError:
        print("El archivo 'productos.txt' no existe. Primero créelo desde el menú.")
"""
Uso r para leer el archivo, .strip() para eliminar los saltos de linea o espacios
y .split(",") para dividir la linea en partes separadas por como.
"""
"""
3 - Agregar productis desde teclado 
"""
def agregar_producto():
    nombre = input("Ingrese nombre del producto: ")
    precio = input("Ingrese precio: ")
    cantidad = input("Ingrese cantidad: ")

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado correctamente.")

"""
se usa a para agregar contenido al final sin eliminar lo anterior
"""
"""
4 - Cargar productos en una lista de diccionarios
"""
def cargar_productos():
    productos = []
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
    except FileNotFoundError:
        print("No se encontró el archivo 'productos.txt'.")
    return productos
"""
al separar con .split() puedo convertir los datos en estructuras mas complejas
como diccionarios o listas para manejarlos en memoria
"""
"""
5 - Buscar producto por nombre
"""
def buscar_producto():
    productos = cargar_productos()
    if not productos:
        return

    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False

    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            print(f"Producto encontrado: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print("El producto no existe en la lista.")
"""
Use lower() para evitar errores por mayusculas/minusculas.
"""
"""
6 - Guardar los productos actualizados
"""
def guardar_productos():
    productos = cargar_productos()
    if not productos:
        return

    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Archivo actualizado correctamente.")
"""
Uso el modo w para sobreescribir el archivo con el contenido actual, garantizando que la informacion
en memoria se guarde de forma persisitente.
"""

"""
A continuacion creo un menu para ordenar cada punto segun su actividad
"""

while True:
    print("\n----------------------------")
    print("      MENÚ DE OPCIONES      ")
    print("----------------------------")
    print("1. Crear archivo inicial (Punto 1)")
    print("2. Leer y mostrar productos (Punto 2)")
    print("3. Agregar producto (Punto 3)")
    print("4. Cargar productos en lista (Punto 4)")
    print("5. Buscar producto por nombre (Punto 5)")
    print("6. Guardar productos actualizados (Punto 6)")
    print("7. Salir")
    print("----------------------------")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_archivo_inicial()
    elif opcion == "2":
        leer_y_mostrar_productos()
    elif opcion == "3":
        agregar_producto()
    elif opcion == "4":
        productos = cargar_productos()
        if productos:
            print("Productos cargados correctamente en memoria.")
    elif opcion == "5":
        buscar_producto()
    elif opcion == "6":
        guardar_productos()
    elif opcion == "7":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida, intente nuevamente.")