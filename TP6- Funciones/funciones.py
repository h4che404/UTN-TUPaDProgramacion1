#funciones
#Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”.
# Llamar a esta función desde el programa principal.
print("Punto 1")
def imprimir_hola_mundo():
    print("Hola Mundo!")
#Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
print("Punto 2")
def saludar_usuario(nombre):
    return f"Hola, {nombre}"
#Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima:
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y
# llamar a esta función con los valores ingresados.
print("Punto 3")
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
print("Punto 4")
def calcular_area_circulo(radio):
    import math
    area = math.pi * radio ** 2
    print("El área del círculo es:", area)
def calcular_perimetro_circulo(radio):
    import math
    perimetro = 2 * math.pi * radio
    print("El perímetro del círculo es:", perimetro)

#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función
print("Punto 5")
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos son {horas} horas")
#Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. 
# Pedir al usuario el número y llamar a la función.
print("punto 6")
def tabla_de_multiplicar(numero):
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
#Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara
print("Punto 7")
def operaciones_basicas(a, b):
    while True:
        if b == 0:
            print("Error: No se puede dividir por cero. Por favor, ingrese un valor diferente para b.")
            b = float(input("Ingrese un nuevo valor para b: "))
        else:
            break
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    return (suma, resta, multiplicacion, division)
#Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC).
#  Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales
print("Punto 8")
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {round(imc, 2)}")
    return round(imc, 2)
#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
print("Punto 9")
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")
    return fahrenheit
#Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
print("Punto 10")
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de {a}, {b} y {c} es: {promedio}")
    return promedio
