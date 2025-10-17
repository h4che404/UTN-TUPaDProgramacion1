#Actividades
#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
#Añadir las siguientes frutas con sus respectivos precios:
#Naranja = 1200
#Manzana = 1500
#Pera = 2300
print("Punto 1")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800
print('Punto 2')
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.
print('Punto 3')
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#Luego, pedí un nombre y mostrale el número asociado, si existe
print('Punto 4')
agenda = {}
for i in range(5):
    nombre = input(f'Ingrese el nombre del contacto {i+1}: ')
    numero = input(f'Ingrese el número de teléfono de {nombre}: ')
    agenda[nombre] = numero

consulta = input('Ingrese el nombre a consultar: ')
if consulta in agenda:
    print(f'El número de {consulta} es {agenda[consulta]}')
else:
    print(f'El contacto {consulta} no existe en la agenda.')

#5) Solicita al usuario una frase e imprime:
#Las palabras únicas (usando un set).
#Un diccionario con la cantidad de veces que aparece cada palabra.
print('Punto 5')
frase = input('Ingrese una frase: ')
palabras = frase.split()
palabras_unicas = set(palabras)
print('Palabras únicas:')
for palabra in palabras_unicas:
    print(f'- {palabra}')
conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1
print('Cantidad de veces que aparece cada palabra:')
for palabra, cantidad in conteo_palabras.items():
    print(f'- {palabra}: {cantidad}')

#Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
print('Punto 6')
alumnos = {}
for i in range(3):
    nombre = input(f'Ingrese el nombre del alumno {i+1}: ')
    notas = []
    for j in range(3):
        nota = float(input(f'Ingrese la nota {j+1} de {nombre}: '))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f'El promedio de {nombre} es {promedio:.2f}')

#Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#Mostrá los que aprobaron ambos parciales.
#Mostrá los que aprobaron solo uno de los dos.
#Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
print('Punto 7')
parcial1 = {'Juan', 'Ana', 'Jose', 'Marta'}
parcial2 = {'Ana', 'Jose', 'Luis', 'Pedro'}
#Ambos parciales
print('Aprobaron ambos parciales:')
print(parcial1.intersection(parcial2))
#Solo uno de los dos
print('Aprobaron solo uno de los dos:')
print(parcial1.symmetric_difference(parcial2))
#Al menos un parcial
print('Aprobaron al menos un parcial:')
print(parcial1.union(parcial2))

#8)Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.
print('Punto 8')
stock_productos = {}
while True:
    accion = input('Ingrese una accion (consultar/agregar/salir): ').lower()
    if accion == 'salir':
        break
    elif accion == 'consultar':
        producto = input('Ingrese el nombre del producto a consultar: ')
        if producto in stock_productos:
            print(f'El stock de {producto} es {stock_productos[producto]} unidades.')
        else:
            print(f'El producto {producto} no existe en el stock.')
    elif accion == 'agregar':
        producto = input('Ingrese el nombre del producto a agregar o actualizar: ')
        cantidad = int(input('Ingrese la cantidad a agregar: '))
        if producto in stock_productos:
            stock_productos[producto] += cantidad
            print(f'Se han agregado {cantidad} unidades a {producto}. Nuevo stock: {stock_productos[producto]} unidades.')
        else:
            stock_productos[producto] = cantidad
            print(f'Se ha agregado un nuevo producto {producto} con un stock de {cantidad} unidades.')
    else:
        print('Accion no reconocida. Por favor, intente de nuevo.')

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.
print('Punto 9')
agenda_eventos = {
    ('Lunes', '10:00'): 'Reunion de equipo',
    ('Martes', '14:00'): 'Futbol con amigos',
    ('Miércoles', '09:00'): 'Cita con el dentista',
}
dia = input('Ingrese el dia de la semana: ')
hora = input('Ingrese la hora (HH:MM): ')
if (dia, hora) in agenda_eventos:
    print(f'Actividad en {dia} a las {hora}: {agenda_eventos[(dia, hora)]}')
else:
    print(f'No hay actividad programada en {dia} a las {hora}.')

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo, construí un nuevo diccionario donde:
#Las capitales sean las claves.
#Los países sean los valores
print('Punto 10')
paises= {
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Perú': 'Lima'
}
invertido = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:")
print(invertido)