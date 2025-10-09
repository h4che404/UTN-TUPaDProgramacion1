'''
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
'''
def imprimir_hola_mundo():
    print("Hola Mundo!")

'''
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
'''
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = "Marcos"
print(saludar_usuario(nombre_usuario))

'''
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta función con los valores in-
gresados.
'''

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

informacion_personal("Juan", "Pérez", 30, "Madrid")

'''
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo. calcular_peri-
metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
bas funciones para mostrar los resultados.
'''

pi = 3.1416
def calcular_area_circulo(radio):
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

radio_usuario = 5
print(f"Área del círculo: {calcular_area_circulo(radio_usuario)}")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio_usuario)}")

'''
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos-
trar el resultado usando esta función.
'''

def segundos_a_horas(segundos):
    return segundos / 3600
segundos_usuario = 7200
print(f"Horas: {segundos_a_horas(segundos_usuario)}")

'''
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun-
ción.
'''

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero_usuario = 7
tabla_multiplicar(numero_usuario)

'''
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta-
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
sultados de forma clara.
'''

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return (suma, resta, multiplicacion, division)
resultados = operaciones_basicas(10, 2)
print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicación: {resultados[2]}, División: {resultados[3]}")

'''
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
ción para mostrar el resultado con dos decimales.
'''

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)
peso_usuario = 70
altura_usuario = 1.75
print(f"IMC: {calcular_imc(peso_usuario, altura_usuario)}")

'''
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
'''
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius_usuario = 25
print(f"Fahrenheit: {celsius_a_fahrenheit(celsius_usuario)}")

'''
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
'''

def calcular_promedio(a, b, c):
    return (a + b + c) / 3
num1 = 5
num2 = 10
num3 = 15
print(f"Promedio: {calcular_promedio(num1, num2, num3)}")