'''Ejercicio 1 – Listas básicas
Crea una lista llamada materias con al menos 5 materias.
Agrega una materia nueva con append().
Elimina una materia con remove().
Ordena la lista alfabéticamente y muéstrala por pantalla.'''

materias = ["Matemáticas", "Arquitectura y Sistemas", "Organización de empresas", "Inglés", "Programación"]
materias.append("Base de datos")
materias.remove("Inglés")
materias.sort()
print(materias)

'''Ejercicio 2 – Búsqueda en listas
Crea una lista con los nombres de 5 alumnos.
Solicita al usuario un nombre y verifica si está en la lista.
Si está, muestra su posición en la lista.
Si no está, muestra un mensaje apropiado.'''
alumnos = ["Ana", "Luis", "María", "Carlos", "Sofía"]
nombre_buscar = input("Ingrese el nombre del alumno a buscar: ")
if nombre_buscar in alumnos:
    posicion = alumnos.index(nombre_buscar)
    print(f"{nombre_buscar} está en la posición {posicion} de la lista.")
else:
    print(f"{nombre_buscar} no está en la lista de alumnos.")

'''Ejercicio 3 – Contar elementos repetidos
Crea una lista con varios números (algunos repetidos).
Usa el método count() para mostrar cuántas veces aparece un número elegido por
el usuario.'''

numeros = [1, 2, 3, 4, 2, 5, 3, 2, 6, 4, 7]
numero_elegido = int(input("Ingrese un número para contar sus repeticiones: "))
repeticiones = numeros.count(numero_elegido)
print(f"El número {numero_elegido} aparece {repeticiones} veces en la lista.")

'''Ejercicio 4 – Tuplas básicas
Crea una tupla llamada colores con al menos 5 colores.
Muestra el primer y el último color usando índices.
Verifica si un color ingresado por el usuario está en la tupla.
Muestra la cantidad total de elementos con len().'''

colores = ("rojo", "azul", "verde", "amarillo", "naranja")
print(f"El primer color es {colores[0]} y el último color es {colores[-1]}.")
color_usuario = input("Ingrese un color para verificar si está en la tupla: ")
if color_usuario in colores:
    print(f"El color {color_usuario} está en la tupla.")
else:
    print(f"El color {color_usuario} no está en la tupla.")

'''Ejercicio 5 – Tuplas de alimentos
Crea una tupla llamada alimentos con 4 comidas diferentes.
Muestra el segundo y el último alimento usando índices.
Luego muestra cuántos elementos contiene la tupla.'''

alimentos = ("pizza", "hamburguesa", "ensalada", "sushi")
print(f"El segundo alimento es {alimentos[1]} y el último alimento es {alimentos[-1]}.")
print(f"La tupla contiene {len(alimentos)} elementos.")

'''Ejercicio 6 – Conjuntos sin duplicados
Crea un conjunto con los nombres de tus amigos (algunos repetidos).
Muestra el conjunto para observar el comportamiento con duplicados.
Agrega y elimina un nombre.
Muestra la cantidad total de elementos'''

amigos = {"JUAN", "ELIAS", "AGUS", "JOACO", "LUCAS", "MUNICIPAL"}
print(amigos)
amigos.add("JOEL")
amigos.remove("MUNICIPAL")
print(f"El conjunto ahora tiene {len(amigos)} amigos.")

'''Ejercicio 7 – Operaciones con conjuntos
Crea dos conjuntos:'''

materias_1 = {"Programación", "Matemática", "Inglés"}
materias_2 = {"Programación", "Base de Datos", "Inglés"}

'''Muestra:
a) Materias comunes
b) Materias exclusivas del primer conjunto
c) Todas las materias sin repetir'''

comunes = materias_1.intersection(materias_2)
print(comunes)
exclusivas_1 = materias_1.difference(materias_2)
print(exclusivas_1)
sin_repetir = materias_1.symmetric_difference(materias_2)
print(sin_repetir)

'''Ejercicio 8 – Diccionario de alumnos
Crea un diccionario con 3 alumnos y sus notas.
Agrega un nuevo alumno.
Modifica la nota de uno existente.
Muestra todas las claves y valores.
'''

alumnos_y_notas = {"ANA": 8, "LUIS": 7, "MARIA": 9}
alumnos_y_notas["CARLOS"] = 7
alumnos_y_notas["LUIS"] = 6
for alumno, nota in alumnos_y_notas.items():
    print(f"{alumno}: {nota}")

'''Ejercicio 9 – Verificación de acceso
Crea un diccionario con las claves "usuario" y "contraseña".
Solicita los datos al usuario y verifica si coinciden.
Muestra “Acceso concedido” o “Acceso denegado”.'''

credenciales = {"usuario": "admin", "contraseña": "1234"}
usuario_input = input("Ingrese su usuario: ")
contrasena_input = input("Ingrese su contraseña: ")
if (usuario_input == credenciales["usuario"] and 
    contrasena_input == credenciales["contraseña"]):
    print("Acceso concedido")
else:
    print("Acceso denegado")

'''Ejercicio 10 – Eliminar clave de diccionario
Crea un diccionario con tres ciudades y su cantidad de habitantes.
Elimina una ciudad usando pop().
Muestra el diccionario actualizado'''

ciudades = {"CABA": 3121707, "Córdoba": 83890, "Rosario": 1029619}
ciudades.pop("Córdoba")
print(ciudades)

'''Ejercicio 11 – Diccionario de precios
Crea un diccionario con al menos 4 productos y sus precios.
Permite al usuario ingresar el nombre de un producto.
Muestra su precio si existe, o un mensaje si no se encuentra.'''

productos = {"manzanas": 5.0,
    "naranjas": 3.0,
    "leche": 10,
    "pan": 15.0}
producto = input("Ingrese el nombre del producto que desea ver el precio: ")
if producto in productos:
    print(f"El precio de {producto} es {productos[producto]}")
else:
    print("Producto no encontrado.")

'''Ejercicio 12 – Convertir lista en conjunto
Crea una lista con números repetidos.
Convierte la lista en conjunto para eliminar los duplicados.
Muestra ambos (lista y conjunto) para comparar los resultados.'''

numeros_repetidos = [1, 2, 3, 2, 4, 3, 5, 1]
conjunto_numeros = set(numeros_repetidos)
print("Lista original:", numeros_repetidos)
print("Conjunto sin duplicados:", conjunto_numeros)

'''Ejercicio 13 – Intersección de conjuntos
Crea dos conjuntos de números enteros.
Muestra los números que tienen en común (intersección).'''

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}
interseccion = conjunto_a.intersection(conjunto_b)
print("Números en común:", interseccion)

'''Ejercicio 14 – Promedio de notas
Crea un diccionario con 3 alumnos y sus notas numéricas.
Calcula y muestra el promedio general de todas las notas.
'''

notas_alumnos = {"ANA": 8, "LUIS": 7, "MARIA": 9}
promedio = sum(notas_alumnos.values()) / len(notas_alumnos)
print(f"El promedio general de las notas es: {promedio:.2f}")

'''Ejercicio 15 – Agregar productos y mostrar precios
Crea un diccionario vacío llamado productos.
Permite al usuario ingresar 3 productos con su precio.
Luego, muestra todos los productos con sus precios.'''

productos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    productos[nombre] = precio
for producto, precio in productos.items():
    print(f"{producto}: ${precio:.2f}")

