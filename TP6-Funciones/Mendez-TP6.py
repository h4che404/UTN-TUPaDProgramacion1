print("Actividades")
print("-----------------------")
print("Punto 1")
"""
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""
def inmprimir_hola_mundo ():
    print("Hola Mundo!")
inmprimir_hola_mundo()
print("-----------------------")
print("Punto 2")

"""
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"),
 deberá devolver: “Hola Marcos!”. 
Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
nom = input("¿Cuál es us nombre?: ")
print(saludar_usuario(nom))
print("-----------------------")
print("Punto 3")

"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nom = input("Ingrese su nombre: ")
apell = input("Ingrese su apellido: ")
ed = input("Ingrese su edad: ")
reci = input("Ingrese su lugar de recidencia: ")

print(informacion_personal(nom,apell,ed,reci))
print("-----------------------")
print("Punto 4")

"""
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
 como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y
 devuelva el perímetro del círculo. Solicitar el 
radio al usuario y llamar ambas funciones para mostrar los resultados.
"""

def calcular_area_circulo(radio):
    area = 0
    area = 3.14 * radio**2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro

rad = int(input("Ingrese el radio del circulo: "))

print(f"Area = {calcular_area_circulo(rad)} \n Perimetro = {calcular_perimetro_circulo(rad)}")
print("-----------------------")
print("Punto 5")
"""
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y 
mostrar el resultado usando esta función.
"""

def segundos_a_horas(segundos):
    horas = 3600 / segundos
    return horas

seg = int(input("Ingrese los segundos: "))

print(f"{seg} segundos equivalen a {segundos_a_horas(seg)} horas")
print("-----------------------")
print("Punto 6")

"""
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

num = int(input("Ingrese un número para obtener su tabla de multiplicar: "))
print(tabla_multiplicar(num))
print("-----------------------")
print("Punto 7")
"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado 
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
"""

def operaciones_basicas(a, b):
    print(f" {a} + {b} = {a+b} \n {a} - {b} = {a-b} \n {a} * {b} = {a*b} \n {a} / {b} = {a/b} ")

while True:

    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    if a == 0 or b == 0:
        print("El número no puede ser cero: ")
    else:
        break

print(operaciones_basicas(a,b))
print("-----------------------")
print("Punto 8")

"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
función para mostrar el resultado con dos decimales.
"""

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    print(f"IMC = {imc}")

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
print(calcular_imc(peso,altura))
print("-----------------------")
print("Punto 9")

"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
def celsius_a_fahrenheit(celsius):
    far = (celsius * 9/5) + 32 
    print(f"{celsius} °C equivalen a {far} F")
celsius = float(input("Ingrese la temperatura en Celsius: "))
print(celsius_a_fahrenheit(celsius))
print("-----------------------")
print("Punto 10")

"""
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
def calcular_promedio(a,b,c):
    promedio = (a+b+c)/3
    return promedio
num1 = float(input("Primer Número: "))
num2 = float(input("Segundo Número: "))
num3 = float(input("Tercer Número: "))
print(f"El promedio de {num1}, {num2}, {num3} es {calcular_promedio(num1,num2,num3)}")