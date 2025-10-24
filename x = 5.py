
#para lograr que fucione hay q llamarla . saludar()
from re import match


def hola_mundo():
    print("hola_mundo")
    
hola_mundo()
print("--------")
def saludar_usuario(nombre):
    print(f"hola {nombre}")

nombre= input("ingresa tu nombre: ")
saludar_usuario(nombre)
print("-----")
def informacion_personal(nombre,apellido,edad,residencia):

    print(f"soy {nombre} {apellido} tengo {edad}, y vivo en {residencia}")

apellido = input("apellido: ")
edad = input("edad: ")
residencia = input("residencia: ")

informacion_personal(nombre, apellido, edad, residencia)
print("------")

# 4. Funciones para área y perímetro de un círculo
def calcular_area_circulo(radio):
    return match.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * match.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f}\n")

# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f}\n")

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero)
print()

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir entre 0"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}\n")

# 8. Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}\n")

# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}\n")

# 10. Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")