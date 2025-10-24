#Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
print("\nPunto 1")
with open("productos.txt", "w") as archivo:
    archivo.write("Manzana,50,100\n")
    archivo.write("Banana,30,150\n")
    archivo.write("Naranja,40,120\n")
print("Archivo 'productos.txt' creado con éxito.")

# Leer y mostrar productos: Crear un programa que abra productos.txt,
# lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30
print("\nPunto 2")
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.
print("\nPunto 3")
nuevo_producto = input("Ingrese un nuevo producto (nombre,precio, cantidad) separado por comas: ")
with open ("productos.txt", "a") as archivo:
    archivo.write("\n" + nuevo_producto)
    print("Producto agregado con extio")

#Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad
print("\nPunto 4")
productos = []
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre.strip(),
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)
print(productos)

#Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos.
# Si no existe, mostrar un mensaje de error
print("\nPunto 5")
nombre_buscar = input("\n Ingrese el nombre del producto a buscar: ")
encontrado = False
for producto in productos:
    if producto[nombre] == nombre_buscar:
        print(f"Producto encontrado: Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
        encontrado = True
        break
    else:
        print("Producto no encontrado.")

#Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.
print("\nPunto 6")
with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
print("Archivo 'productos.txt' actualizado con éxito.")






