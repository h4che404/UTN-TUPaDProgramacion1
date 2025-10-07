'''
a) Nombre, edad y preguntas del día
Escribe un programa que pida al usuario su nombre y edad, muestre un mensaje de bienvenida y le pregunte dos cosas de su día (por ejemplo: si comió y si estudió). Finalmente, muestra un resumen.
'''

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print(f"¡Bienvenido/a, {nombre}! Tienes {edad} años.")
comio = input("¿Comiste hoy? (sí/no): ")
if comio.lower() not in ['sí', 'si', 'no']:
    print("Respuesta no válida. Por favor, responde con 'sí' o 'no'.")
    comio = input("¿Comiste hoy? (sí/no): ")
estudio = input("¿Estudiaste hoy? (sí/no): ")
if estudio.lower() not in ['sí', 'si', 'no']:
    print("Respuesta no válida. Por favor, responde con 'sí' o 'no'.")
    estudio = input("¿Estudiaste hoy? (sí/no): ")
print(f"Resumen: Nombre: {nombre}, Edad: {edad}, Comió: {comio}, Estudió: {estudio}")


'''
b) Mantel para mesa
Escribe un programa que calcule cuánto mantel se necesita para cubrir una mesa rectangular. El usuario ingresa largo y ancho (en metros).
'''
largo = float(input("Ingrese el largo de la mesa en metros: "))
ancho = float(input("Ingrese el ancho de la mesa en metros: "))
area_mesa = largo * ancho
print(f"Se necesita {area_mesa:.2f} metros cuadrados de mantel para cubrir la mesa.")

'''
c) Conversor de minutos a horas
Pide al usuario un número de minutos y muestra cuántas horas y minutos equivalen.
'''
minutos = int(input("Ingrese un número de minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{minutos} minutos equivalen a {horas} horas y {minutos_restantes} minutos.")


'''
Estructuras Condicionales
a) Velocidad del vehículo
Pide al usuario la velocidad a la que viaja (km/h) y muestra si va lento (<40), rápido (>120) o normal.
'''

velocidad = input("ingrese la velocidad a la que viaja (km/h): ")
try:
    velocidad = float(velocidad)
    if velocidad < 40:
        print("Va lento")
    elif velocidad > 120:
        print("Va rápido")
    else:
        print("Va a una velocidad normal")
except ValueError:
    print("Por favor, ingrese un número válido para la velocidad.")


'''
b) Mayor de edad con análisis de vida
Pide la edad y determina si es mayor de edad. Luego pregunta si trabaja y su pasatiempo, y muestra un mensaje final describiendo cómo es su vida.
'''
edad = input("Ingrese su edad: ")
try:
    edad = int(edad)
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
    trabaja = input("¿Trabajas? (sí/no): ")
    pasatiempo = input("¿Cuál es tu pasatiempo favorito?: ")
    print(f"Tienes {edad} años, {'trabajas' if trabaja.lower() in ['sí', 'si'] else 'no trabajas'}, y te gusta {pasatiempo}.")
except ValueError:
    print("Por favor, ingrese un número válido para la edad.")

'''
c) Par o impar
Pide un número al usuario e indica si es par o impar.
'''

numero = input("Ingrese un número: ")
try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
except ValueError:
    print("Por favor, ingrese un número válido.")


'''
Estructuras Repetitivas
a) Números del 1 al 10 con for
Muestra los números del 1 al 10.
'''

for i in range(1, 11):
    print(i)


'''
b) Suma del 1 al 100 con while
Calcula la suma de los números del 1 al 100.
'''

suma = 0
contador = 1
while contador <= 100:
    suma += contador
    contador += 1
print(f"La suma de los números del 1 al 100 es: {suma}")


'''
c) Tabla de multiplicar
Pide un número y muestra su tabla de multiplicar del 1 al 10.
'''

num = input("Ingrese un número para ver su tabla de multiplicar: ")
try:
    num = int(num)
    print(f"Tabla de multiplicar del {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Por favor, ingrese un número válido.")


'''
Bucles con Condicionales
a) Suma hasta ingresar 0
Pide números hasta que se ingrese 0. Luego muestra la suma total.
'''

suma_total = 0
while True:
    numero = input("Ingrese un número (0 para terminar): ")
    try:
        numero = int(numero)
        if numero == 0:
            break
        suma_total += numero
    except ValueError:
        print("Por favor, ingrese un número válido.")
print(f"La suma total es: {suma_total}")


'''
b) Contraseña correcta
Pide una contraseña. Mientras no sea correcta, vuelve a pedirla.
'''

contraseña_correcta = "contrasena"
while True:
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == contraseña_correcta:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Intente de nuevo.")

'''
c) Adivinar número secreto
Genera un número secreto y deja que el usuario lo adivine con pistas.
'''

import random
numero_secreto = random.randint(1, 100)
while True:
    intento = input("Adivina el número secreto (entre 1 y 100): ")
    try:
        intento = int(intento)
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print("¡Felicidades! Adivinaste el número secreto.")
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")


'''
Listas

a) Nombres de compañeros
Declara una lista con 5 nombres y muestra el primero y el último.
'''

nombres = ["Ana", "Luis", "María", "Carlos", "Sofía"]
print(f"El primer nombre es: {nombres[0]}")
print(f"El último nombre es: {nombres[-1]}")   


'''
b) Reemplazar elemento
Crea una lista de 5 números, reemplaza el tercero por 99 y muestra la lista.
'''

numeros = [10, 20, 30, 40, 50]
numeros[2] = 99
print("Lista después de reemplazar el tercer elemento por 99:", numeros)


'''
Lista desordenada

c) Lista desordenada
Con la lista [7, 42, 15, 3, 28, 91, 54], muestra los primeros 3 elementos y los últimos 2.
'''

lista = [7, 42, 15, 3, 28, 91, 54]
print("Primeros 3 elementos:", lista[:3])
print("Últimos 2 elementos:", lista[-2:])


'''
d) Lista de frutas
Pide al usuario 3 frutas y muéstralas en una lista.
'''

frutas = []
for i in range(3):
    fruta = input(f"Ingrese la fruta {i+1}: ")
    frutas.append(fruta)
print("Lista de frutas:", frutas)


'''
e) Lista anidada (matriz)
Declara una matriz 2x3 e imprime los elementos en [0][1], [1][0] y [1][2].
'''

matriz = [[1, 2, 3], [4, 5, 6]]
print("Elemento en [0][1]:", matriz[0][1])
print("Elemento en [1][0]:", matriz[1][0])
print("Elemento en [1][2]:", matriz[1][2])


'''
f) Números positivos y negativos
Crea una lista de 6 números (algunos positivos y otros negativos). Muestra por separado solo los positivos y solo los negativos.
Menú con Listas (Mini Proyecto — Tienda de ropa)
'''
'''
Consigna:
Una tienda de ropa necesita llevar el control de las prendas.
Crea dos listas:

• prendas[] → nombres de las prendas.
• stock[] → cantidad disponible.
Menú con las siguientes opciones:

1. Ingresar prendas y stock.
2. Ver inventario.
3. Ver prendas agotadas.
4. Salir.
'''
prendas = []
stock = []
while True:
    print("\nMenú de la tienda de ropa:")
    print("1. Ingresar prendas y stock")
    print("2. Ver inventario")
    print("3. Ver prendas agotadas")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        prenda = input("Ingrese el nombre de la prenda: ")
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            prendas.append(prenda)
            stock.append(cantidad)
            print(f"Prenda '{prenda}' con stock {cantidad} agregada.")
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")
    
    elif opcion == '2':
        print("\nInventario de prendas:")
        for i in range(len(prendas)):
            print(f"{prendas[i]}: {stock[i]} unidades")
    
    elif opcion == '3':
        print("\nPrendas agotadas:")
        agotadas = False
        for i in range(len(prendas)):
            if stock[i] == 0:
                print(prendas[i])
                agotadas = True
        if not agotadas:
            print("No hay prendas agotadas.")
    
    elif opcion == '4':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")k 