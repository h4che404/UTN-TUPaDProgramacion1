'''
Ejercicio 1 – Listas básicas
Crea una lista llamada materias con al menos 5 materias.
Agrega una materia nueva con append().
Elimina una materia con remove().
Ordena la lista alfabéticamente y muéstrala por pantalla.
'''
materias = ["Matematica", "Fisica", "Quimica", "Biologia", "Historia"]
materias.append("Ingles")
materias.remove("Quimica")
materias.sort()
print(materias)

'''
Ejercicio 2 – Búsqueda en listas
Crea una lista con los nombres de 5 alumnos.
Solicita al usuario un nombre y verifica si está en la lista.
Si está, muestra su posición en la lista.
Si no está, muestra un mensaje apropiado.
'''
alumnos = ["Ana", "Luis", "Maria", "Jorge", "Sofia"]
nombre_buscar = input("Ingrese el nombre del alumno a buscar: ")
if nombre_buscar in alumnos:
    posicion = alumnos.index(nombre_buscar)
    print(f"{nombre_buscar} está en la posición {posicion} de la lista.")
else:
    print(f"{nombre_buscar} no está en la lista de alumnos.")

'''
Ejercicio 3 – Contar elementos repetidos
Crea una lista con varios números (algunos repetidos).
Usa el método count() para mostrar cuántas veces aparece un número elegido por
el usuario.
'''
numeros = [1, 2, 3, 4, 2, 5, 3, 2, 6, 1]
numero_elegido = int(input("Ingrese un número para contar sus repeticiones: "))
repeticiones = numeros.count(numero_elegido)
print(f"El número {numero_elegido} aparece {repeticiones} veces en la lista.")

'''
Ejercicio 4 – Tuplas básicas
Crea una tupla llamada colores con al menos 5 colores.
Muestra el primer y el último color usando índices.
Verifica si un color ingresado por el usuario está en la tupla.
Muestra la cantidad total de elementos con len().
PROGRAMACIÓN I
'''
colores = ("rojo", "azul", "verde", "amarillo", "negro")
print(f"Primer color: {colores[0]}")
print(f"Último color: {colores[-1]}")
color_buscar = input("Ingrese un color para buscar en la tupla: ")
if color_buscar in colores:
    print(f"El color {color_buscar} esta en la tupla.")
else:
    print(f"El color {color_buscar} no esta en la tupla.")
print(f"La tupla contiene {len(colores)} colores.")

'''
Ejercicio 5 – Tuplas de alimentos
Crea una tupla llamada alimentos con 4 comidas diferentes.
Muestra el segundo y el último alimento usando índices.
Luego muestra cuántos elementos contiene la tupla.
'''

alimentos = ("pizza", "hamburguesa", "ensalada", "sushi")
print(f"Segundo alimento: {alimentos[1]}")
print(f"Último alimento: {alimentos[-1]}")
print(f"La tupla contiene {len(alimentos)} alimentos.")

'''
Ejercicio 6 – Conjuntos sin duplicados
Crea un conjunto con los nombres de tus amigos (algunos repetidos).
Muestra el conjunto para observar el comportamiento con duplicados.
Agrega y elimina un nombre.
Muestra la cantidad total de elementos.
'''

amigos = {"Carlos", "Ana", "Luis", "Ana", "Maria", "Carlos"}
print("Conjunto de amigos (sin duplicados):", amigos)
amigos.add("Jorge")
amigos.remove("Luis")
print("Conjunto actualizado de amigos:", amigos)
print(f"La cantidad total de amigos es: {len(amigos)}")

'''
Ejercicio 7 – Operaciones con conjuntos
Crea dos conjuntos:
materias_1 = {"Programacion" , "Matematica" , "Ingles"}
materias_2 = {"Programacion" , "Base de Datos" , "Ingles"}
Muestra:
a) Materias comunes
b) Materias exclusivas del primer conjunto
c) Todas las materias sin repetir
'''
materias_1 = {"Programacion" , "Matematica" , "Ingles"}
materias_2 = {"Programacion" , "Base de Datos" , "Ingles"}
comunes = materias_1.intersection(materias_2)
exclusivas_1 = materias_1.difference(materias_2)
todas_sin_repetir = materias_1.union(materias_2)    
print("Materias comunes:", comunes)
print("Materias exclusivas del primer conjunto:", exclusivas_1)
print("Todas las materias sin repetir:", todas_sin_repetir)

'''
Ejercicio 8 – Diccionario de alumnos
Crea un diccionario con 3 alumnos y sus notas.
Agrega un nuevo alumno.
Modifica la nota de uno existente.
Muestra todas las claves y valores.
'''
alumnos_notas = {"Ana": 85, "Luis": 90, "Maria": 95}
alumnos_notas["Jorge"] = 88
alumnos_notas["Luis"] = 92
print("Alumnos y sus notas:")
for alumno, nota in alumnos_notas.items():
    print(f"{alumno}: {nota}")

'''
Ejercicio 9 – Verificación de acceso
Crea un diccionario con las claves "usuario" y "contraseña" .
Solicita los datos al usuario y verifica si coinciden.
Muestra “Acceso concedido” o “Acceso denegado”.
'''
credenciales = {"usuario": "admin", "contraseña": "1234"}
usuario_input = input("Ingrese el usuario: ")
contraseña_input = input("Ingrese la contraseña: ")
if (usuario_input == credenciales["usuario"] and 
    contraseña_input == credenciales["contraseña"]):
    print("Acceso concedido")
else:
    print("Acceso denegado")

'''
Ejercicio 10 – Eliminar clave de diccionario
PROGRAMACIÓN I
Crea un diccionario con tres ciudades y su cantidad de habitantes.
Elimina una ciudad usando pop().
Muestra el diccionario actualizado.
'''
ciudades = {"Buenos Aires": 3000000, "Cordoba": 1500000, "Rosario": 1200000}
ciudades.pop("Cordoba")
print("Diccionario actualizado de ciudades:", ciudades)

'''
Ejercicio 11 – Diccionario de precios
Crea un diccionario con al menos 4 productos y sus precios.
Permite al usuario ingresar el nombre de un producto.
Muestra su precio si existe, o un mensaje si no se encuentra.
'''
precios_productos = {
    "manzana": 150,
    "banana": 100,
    "naranja": 120,
    "pera": 130
}
producto_buscar = input("Ingrese el nombre del producto: ").lower()
if producto_buscar in precios_productos:
    print(f"El precio de {producto_buscar} es {precios_productos[producto_buscar]}")
else:
    print(f"El producto {producto_buscar} no se encuentra en el diccionario.")

'''
Ejercicio 12 – Convertir lista en conjunto
Crea una lista con números repetidos.
Convierte la lista en conjunto para eliminar los duplicados.
Muestra ambos (lista y conjunto) para comparar los resultados.
'''
numeros_repetidos = [1, 2, 3, 2, 4, 3, 5, 1]
conjunto_numeros = set(numeros_repetidos)
print("Lista con números repetidos:", numeros_repetidos)
print("Conjunto sin duplicados:", conjunto_numeros)

'''
Ejercicio 13 – Intersección de conjuntos
Crea dos conjuntos de números enteros.
Muestra los números que tienen en común (intersección).
'''
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}
interseccion = conjunto_a.intersection(conjunto_b)
print("Números en común entre ambos conjuntos:", interseccion)

'''
Ejercicio 14 – Promedio de notas
Crea un diccionario con 3 alumnos y sus notas numéricas.
Calcula y muestra el promedio general de todas las notas.
'''
notas_alumnos = {"Ana": 85, "Luis": 90, "Maria": 95}
promedio = sum(notas_alumnos.values()) / len(notas_alumnos)
print(f"El promedio general de las notas es: {promedio}")

'''
Ejercicio 15 – Agregar productos y mostrar precios
Crea un diccionario vacío llamado productos.
Permite al usuario ingresar 3 productos con su precio.
'''

productos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos[nombre] = precio
print("Productos y sus precios:")
for producto, precio in productos.items():
    print(f"{producto}: {precio}")
