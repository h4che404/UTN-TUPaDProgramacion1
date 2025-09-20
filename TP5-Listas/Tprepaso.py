#Tprepaso
"""
a) Nombre, edad y preguntas del día
Escribe un programa que pida al usuario su nombre y edad, muestre un mensaje de bienvenida y 
le pregunte dos cosas de su día (por ejemplo: si comió y si estudió). Finalmente, muestra un resumen.
"""
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")
print(f"\n¡Hola, {nombre}! Bienvenido, veo que tienes {edad} años")
comio = input("Ya comiste hoy? (sí/no): ")
estudio = input("Ya has estudiado hoy? (sí/no): ")
print("\n--- Resumen de tu dia ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Comio?: {comio}")
print(f"Estudio?: {estudio}")
print("-------------------------")

"""
b) Mantel para mesa
Escribe un programa que calcule cuánto mantel se necesita para cubrir una mesa rectangular. 
El usuario ingresa largo y ancho (en metros).
"""
largo = float(input("Ingresa el largo de la mesa (en metros): "))
ancho = float(input("Ingresa el ancho de la mesa (en metros): "))
area = largo * ancho
print(f"\nNecesitas {area:.2f} metros cuadrados de mantel para cubrir la mesa.")
print("-------------------------")
"""
c) Conversor de minutos a horas
Pide al usuario un número de minutos y muestra cuántas horas y minutos equivalen.
"""
minutos_totales = int(input("Ingresa un numero de minutos: "))
horas = minutos_totales // 60
minutos = minutos_totales % 60
print(f"\n{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")

print("-------------------------")
"""
Estructuras Condicionales
a) Velocidad del vehículo
Pide al usuario la velocidad a la que viaja (km/h) y muestra si va lento (<40), rápido (>120) o normal.
"""
velocidad = float(input("Ingresa la velocidad a la que viajas (km/h): "))
if velocidad < 40:
    print("Vas lento.")
elif velocidad > 120:
    print("Vas rapido.")
else:
    print("Vas a una velocidad normal.")

print("-------------------------")
"""
b) Mayor de edad con análisis de vida
Pide la edad y determina si es mayor de edad. 
Luego pregunta si trabaja y su pasatiempo, y muestra un mensaje final describiendo cómo es su vida.
"""
edad = int(input("¿Cuántos años tienes? "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
trabaja = input("Trabajas? (si o no): ")
pasatiempo = input("Cual es tu pasatiempo favorito?: ")
print("\n--- Descripcion de tu vida ---")
print("Tienes", edad, "años.")
print("Trabajas:" if trabaja == "si" else "No trabajas.")
print("Tu pasatiempo favorito es:", pasatiempo)

print("-------------------------")
"""
c) Par o impar
Pide un número al usuario e indica si es par o impar.
"""
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

print("-------------------------")
"""
Estructuras Repetitivas
a) Números del 1 al 10 con for
Muestra los números del 1 al 10.
"""
for numero in range(1, 11):
    print(numero)
print("-------------------------")
"""
b) Suma del 1 al 100 con while
Calcula la suma de los números del 1 al 100.
"""
numero = 1
suma = 0
while numero <= 100:
    suma += numero
    numero += 1
print("La suma de los numeros del 1 al 100 es:", suma)
print("-------------------------")
"""
c) Tabla de multiplicar
Pide un número y muestra su tabla de multiplicar del 1 al 10.
"""
numero = int(input("Ingresa un numero para ver su tabla de multiplicar: "))
print(f"Tabla del {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
print("-------------------------")
"""
Bucles con Condicionales
a) Suma hasta ingresar 0
Pide números hasta que se ingrese 0. Luego muestra la suma total.
"""
suma = 0
while True:
    numero = int(input("Ingresa un numero (si utiliza el numero 0 el programa finalizara): "))
    if numero == 0:
        break  
    suma += numero  
print("\nLa suma total es:", suma)

print("-------------------------")
"""
b) Contraseña correcta
Pide una contraseña. Mientras no sea correcta, vuelve a pedirla.
"""
contraseña_correcta = "1234"
contraseña = input("Ingresa la contraseña: ")
while contraseña != contraseña_correcta:
    print("Contraseña incorrecta. Intenta de nuevo.")
    contraseña = input("Ingresa la contraseña: ")
print("Contraseña correcta. Bienvenido.")
print("-------------------------")
"""
c) Adivinar número secreto
Genera un número secreto y deja que el usuario lo adivine con pistas.
"""
import random
numero_secreto = random.randint(1, 20)
print("¡Adivina el número secreto entre 1 y 20!")
while True:
    intento = int(input("Ingresa tu intento: "))
    
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta un número más alto.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta un número más bajo.")
    else:
        print(f"Bien hecho. Adivinaste el número secreto: {numero_secreto}")
        break
print("-------------------------")
"""
Listas
a) Nombres de compañeros
Declara una lista con 5 nombres y muestra el primero y el último.
"""
lista_nombre =["Nahuel","Agustin","Juan Cruz", "Joaco","David"]
print("primer compañero", lista_nombre[0])
print("quinto compañero", lista_nombre[-1])
print("-------------------------")
"""
b) Reemplazar elemento
Crea una lista de 5 números, reemplaza el tercero por 99 y muestra la lista.
Lista desordenada
"""
lista = [10, 20, 30, 40, 50]
lista[2] = 99
print(lista[0:])
print("-------------------------")
"""
c) Lista desordenada
Con la lista [7, 42, 15, 3, 28, 91, 54], muestra los primeros 3 elementos y los últimos 2.
"""
lista=[7, 42, 15, 3, 28, 91, 54]
print(lista[0:2])
print(lista[5:])
print("-------------------------")
"""
d) Lista de frutas
Pide al usuario 3 frutas y muéstralas en una lista.
"""
frutas = []
for i in range(3):
    fruta = input(f"Ingresa la fruta #{i+1}: ")
    frutas.append(fruta)
print("\n Las frutas que ingresaste son:", frutas)

print("-------------------------")
"""
e) Lista anidada (matriz)
Declara una matriz 2x3 e imprime los elementos en [0][1], [1][0] y [1][2].
"""
matriz = [[10, 20, 30],[40, 50, 60]]
print("Elemento en [0][1]:", matriz[0][1])
print("Elemento en [1][0]:", matriz[1][0])
print("Elemento en [1][2]:", matriz[1][2])
print("-------------------------")
"""
f) Números positivos y negativos
Crea una lista de 6 números (algunos positivos y otros negativos). Muestra por separado solo los positivos y solo los negativos.
Menú con Listas (Mini Proyecto — Tienda de ropa)
Consigna:
Una tienda de ropa necesita llevar el control de las prendas.
Crea dos listas:
•	prendas[] → nombres de las prendas.
•	stock[] → cantidad disponible.
Menú con las siguientes opciones:
1.	Ingresar prendas y stock.
2.	Ver inventario.
3.	Ver prendas agotadas.
4.	Salir.
"""
print("Menu de lista de numeros psotivos y negativos")
numeros = [10, -5, 3, -1, 0, -8]
positivos = []
negativos = []
for num in numeros:
    if num > 0:
        positivos.append(num)
    elif num < 0:
        negativos.append(num)
print("Numeros positivos:", positivos)
print("Nymeros negativos:", negativos)
print("--------------------------")

print("Menu de ropa")
prendas = []
stock = []
while True:
    print("\n--- menu de Tienda de Ropa ---")
    print("1. Ingresar prendas y stock")
    print("2. Ver inventario")
    print("3. Ver prendas agotadas")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        nombre = input("Nombre de la prenda: ")
        cantidad = int(input("Cantidad en stock: "))
        prendas.append(nombre)
        stock.append(cantidad)
        print(f"Prenda '{nombre}' con stock {cantidad} agregada.")
    
    elif opcion == "2":
        print("\nInventario completo:")
        if len(prendas) == 0:
            print("No hay prendas ingresadas.")
        else:
            for i in range(len(prendas)):
                print(f"{prendas[i]} - Stock: {stock[i]}")
    elif opcion == "3":
        print("\nPrendas agotadas:")
        agotadas = False
        for i in range(len(prendas)):
            if stock[i] == 0:
                print(prendas[i])
                agotadas = True
        if not agotadas:
            print("No hay prendas agotadas.")
    elif opcion == "4":
        print("Saliendo del programa.  .  .")
        break
    else:
        print("Opcion invalida, prueba otro")
print("-------------------------")