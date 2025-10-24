'''
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
'''
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300   
print(precios_frutas)

'''
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
'''
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800   
print(precios_frutas)


'''
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
'''
frutas = list(precios_frutas.keys())
print(frutas)

'''
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
• Si el nombre no existe, indicáselo al usuario.
'''
agenda = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero del contacto: ")
    agenda[nombre] = numero
buscar = input("Ingrese el nombre a buscar: ")
if buscar in agenda:
    print(f"El numero de {buscar} es {agenda[buscar]}")
else:
    print(f"El contacto {buscar} no existe en la agenda.")

'''
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
'''

frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print("Cantidad de veces que aparece cada palabra:", contador_palabras)

'''
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
'''
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es {promedio}")

'''
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
'''
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107, 108}
aprobados_ambos = parcial1.intersection(parcial2)
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
aprobados_solo_uno = parcial1.symmetric_difference(parcial2)
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)
aprobados_al_menos_uno = parcial1.union(parcial2)
print("Estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)

'''
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
'''
stock_productos = {}
while True:
    accion = input("Ingrese 'consultar', 'agregar' o 'nuevo' para realizar una acción (o 'salir' para terminar): ").lower()
    if accion == 'salir':
        break
    elif accion == 'consultar':
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in stock_productos:
            print(f"El stock de {producto} es {stock_productos[producto]}")
        else:
            print(f"El producto {producto} no existe en el stock.")
    elif accion == 'agregar':
        producto = input("Ingrese el nombre del producto al que desea agregar stock: ")
        if producto in stock_productos:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            stock_productos[producto] += cantidad
            print(f"Nuevo stock de {producto} es {stock_productos[producto]}")
        else:
            print(f"El producto {producto} no existe en el stock.")
    elif accion == 'nuevo':
        producto = input("Ingrese el nombre del nuevo producto: ")
        cantidad = int(input("Ingrese la cantidad inicial de stock: "))
        stock_productos[producto] = cantidad
        print(f"Producto {producto} agregado con un stock de {cantidad}.")
    else:
        print("Acción no reconocida. Por favor, intente de nuevo.")

'''
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.
'''

agenda_eventos = {}
for i in range(3):
    dia = input("Ingrese el día del evento (formato DD/MM): ")
    hora = input("Ingrese la hora del evento (formato HH:MM): ")
    evento = input("Ingrese el nombre del evento: ")
    agenda_eventos[(dia, hora)] = evento
consulta_dia = input("Ingrese el día a consultar (formato DD/MM): ")
consulta_hora = input("Ingrese la hora a consultar (formato HH:MM): ")
if (consulta_dia, consulta_hora) in agenda_eventos:
    print(f"El evento en {consulta_dia} a las {consulta_hora} es: {agenda_eventos[(consulta_dia, consulta_hora)]}")
else:
    print(f"No hay eventos programados para {consulta_dia} a las {consulta_hora}.")

'''
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
'''
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido de capitales y países:", capitales_paises)