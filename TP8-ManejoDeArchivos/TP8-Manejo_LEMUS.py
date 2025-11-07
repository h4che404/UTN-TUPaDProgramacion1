#Actividades
'''1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad'''

productos = [("manzana", 2000,3),("banana", 2800,5),("mandarina",1800,2)]
with open("productos_lemus.txt", "w") as archivo:
    for nombre, precio, cantidad in productos:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

'''2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30'''

with open("productos_lemus.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f" Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

'''3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.'''

nombre = input("Ingresa el nombre del producto nuevo: ")
precio = input("Ingresa su precio: ")
cantidad = input ("Ahora su cantidad: ")
with open("productos_lemus.txt","a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

'''4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.'''

productos = []
with open("productos_lemus.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({"nombre":nombre,"precio":precio,"cantidad":cantidad})

print(productos)

'''5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.'''

consulta = input("Ingrese el nombre de un producto: ")
encontrado = False
for producto in productos:
    if producto["nombre"].lower() == consulta:
        print(f"Producto: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        encontrado = True
if encontrado == False:
    print("Producto no encontrado.")

'''6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.'''

with open("productos.txt", "w", encoding="utf-8") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

