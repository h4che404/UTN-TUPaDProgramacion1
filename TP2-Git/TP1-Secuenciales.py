#Punto 1
print("PUNTO 1")
"""
Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
"""

print('Hola Mundo!')

print("--------------")

#Punto 2
print("PUNTO 2")

"""
 Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla
"""
nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}, Bienvenido")

print("--------------")

#Punto 3
print("PUNTO 3")

""""
Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
"""
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")

print("--------------")

#Punto 4
print("PUNTO 4")

"""
Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro
"""
radio = input("Ingrese el radio de un circulo: ")
radio = float(radio)

area = 3.14159 * (radio ** 2) #math.pi

perimetro = 3.14159 * area  #math.pi

print("Si el radio es {radio}, entonces el area es  ")

print("--------------")

#Punto 5
print("PUNTO 5")

"""
 Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
"""
seg = input("Ingrese una cantidad de segundos: ")

seg = int(seg)

hr = (seg / 3600)

print(f"{seg} equivalen a {hr} horas")

print("--------------")

#Punto 6
print("PUNTO 6")

"""
 Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.
"""

num = input("Ingrese un número: ")

num = int(num)

print(f"{num} x 1 = {num * 1}")
print(f"{num} x 2 = {num * 2}")
print(f"{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}")
print(f"{num} x 5 = {num * 5}")
print(f"{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}")
print(f"{num} x 8 = {num * 8}")
print(f"{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}")

print("--------------")

#Punto 7
print("PUNTO 7")

"""
Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
"""
num1 = int(input("Ingrese un número distinto de cero: "))
num2 = int(input("Igrese otro número distinto de cero: "))
    
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} x {num2} = {num1*num2}")

print("--------------")

#Punto 8
print("PUNTO 8")

"""
Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:
IMC = (peso en kg)/(altura en m)**2
"""

peso = input("Ingrese su peso en kg (no use la unidad kg): ")
h = input("Ingrese su altura en metros (no use la unidad de m): ")

peso = int(peso)
h = float(h)

indice = peso / h**2

print(f"Su índice de masa corporal o IMC es {indice}")

print("--------------")

#Punto 9
print("PUNTO 9")

"""
 Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
T° en F = (9/5)*C° + 32
"""
print("Convertir de Celsius a Fahrenheit")

c = input("Ingrese la temperatura en Celsius: ")

c = float(c)

f = ((9 / 5) * c) + 32

print(f"{c}° Celius equivalen a {f}F")

print("--------------")

#Punto 10
print("PUNTO 10")

"""
Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.
"""

num1 = input("Ingrese un número: ")
num1 = float(num1)

num2 = input("Ingrese un número: ")
num2 = float(num2)

num3 = input("Ingrese un número: ")
num3 = float(num3)

print(f"El promedio entre {num1}, {num2}, {num3} es {(num1+num2+num3)/3}")

print("--------------")
