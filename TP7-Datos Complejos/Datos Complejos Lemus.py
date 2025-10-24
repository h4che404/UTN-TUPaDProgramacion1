
#Actividad 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Actividad 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#Actividad 3

lista_frutas = []
lista_frutas = precios_frutas.keys()

#actividad 4

numeros_usuarios = {}

for i in range (5):
    nombre = input("Ingrese un nombre:")
    numero = input("Ingrese su número:")
    numeros_usuarios[nombre] = numero

while True:
    opcion = input("Ingrese una opción (ver/salir):")
    if opcion == "ver":
        buscador = input("Ingrese un nombre:")
        if buscador in numeros_usuarios.keys():
            print(f"El número telefónico de {buscador} es {numeros_usuarios[buscador]}")
        else: 
            print("Nombre no encontrado.")
    elif opcion == "salir":
        break
    else:
        print("Opción inválida, vuelve a intentarlo.")

#Actividad 5

frase = input("Ingrese una frase:")
lista_palabras = frase.lower().split()

from collections import Counter

palabras_unicas = set(lista_palabras)
frecuencia = Counter(lista_palabras)
diccionario_palabras = dict(frecuencia)

#Actividad 6

alumnos = []
for i in range (3):
    nombre_alumno = input(f"Ingrese el nombre del alumno {i+1}:")

    primer_nota = float(input(f"Ingrese la primera nota de {nombre_alumno}:"))
    segunda_nota = float(input(f"Ingrese la segunda nota de {nombre_alumno}:"))
    tercera_nota = float(input(f"Ingrese la tercera nota de {nombre_alumno}:"))

    notas = (primer_nota, segunda_nota, tercera_nota)

    alumnos.append((nombre_alumno, notas))

for nombre, notas in alumnos:
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")

#Actividad 7

parcial_uno = {1, 2, 3, 4, 5}
parcial_dos = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

aprobo_ambos = parcial_uno.intersection(parcial_dos)
solo_uno = parcial_uno.symmetric_difference(parcial_dos)

print(f"los alumnos que aprobaron al menos un parcial son: {solo_uno.union(aprobo_ambos)}")

#Actividad 8

productos = {
    "manzanas": 5.0,
    "naranjas": 3.0,
    "leche": 10,
    "pan": 15.0,
    "huevos": 60
}

opcion = input("QUé desea hacer? (ver/agregar/nuevo/salir): ")

if opcion == "ver":
    producto = input("Ingrese el nombre del producto que desea ver el precio: ")
    if producto in productos:
        print(f"El precio de {producto} es {productos[producto]}")
    else:
        print("Producto no encontrado.")
elif opcion == "agregar":
    producto = input("A qué producto desea agregar stock? ")
    cantidad = float(input("Cuánto stock desea agregar? "))
    if producto in productos:
        productos[producto] += cantidad
        print(f"Se ha agregado {cantidad} al stock de {producto}. Nuevo stock: {productos[producto]}")
    else:
        print("Producto no encontrado.")
elif opcion == "nuevo":
    producto = input("Ingrese el nombre del nuevo producto: ")
    stock = float(input("Ingrese el stock del nuevo producto: "))
    productos[producto] = stock
    print(f"Se ha agregado el producto {producto} con un precio de {stock}.")
elif opcion == "salir":
    print("Saliendo del programa.")

#Actividad 9

agenda = {
    ("Lunes", "9:00"): "Minimarket",
    ("Martes", "15:00"): "Reunión PSA",
    ("Miercoles", "21:30"): "Célula igle",
    ("Jueves", "21:00"): "Sede LLA",
    ("Sabado", "20:30"): "Clase Preados"
}

dia = input("Ingrese el día de la semana: ")
hora = input("Ingrese la hora (formato 24 horas, ej. 15:00): ")

clave = (dia, hora)
if clave in agenda:
    print(f"Tiene programado: {agenda[clave]}")
else:
    print("No tiene nada programado en ese día y hora.")

#Actividad 10

capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "México": "Ciudad de México",
    "Japón": "Tokio"
}

invertido = {capital: pais for pais, capital in capitales.items()}
capitales = invertido
print(capitales)
