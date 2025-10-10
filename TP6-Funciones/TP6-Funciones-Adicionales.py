'''
Ejercicio 1: Tabla de multiplicar 
       Objetivo: Generar una tabla de multiplicar usando funciones. 
          Instrucciones: 
1. Crea una función tabla_multiplicar que reciba un número entero positivo. 
2. Devuelve una lista con su tabla de multiplicar del 1 al 10. 
o Ejemplo: Para 3 → [3, 6, 9, ..., 30]. 
      Preguntas de reflexión: 
• ¿Cómo adaptarías la función para recibir el rango (ej: hasta 12)? 
• ¿Qué ocurre si se ingresa un número negativo? 
'''

def tabla_multiplicar(numero):
    return [numero * i for i in range(1, 11)]
print(tabla_multiplicar(3))
while True:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero > 0:
            tabla_multiplicar(numero)
            break
        else:
            print("Por favor, ingrese un número válido.")


'''
    Ejercicio 2: Suma de números pares 
       Objetivo: Sumar elementos pares de una lista con una función. 
          Instrucciones: 
1. Define una función suma_pares que reciba una lista de enteros. 
2. Retorna la suma de los números pares. 
o Ejemplo: Para [1, 2, 3, 4, 5, 6] → 12. 
      Preguntas de reflexión: 
• ¿Cómo manejarías listas vacías o con decimales? 
• ¿Qué ventaja tiene usar una función en lugar de código inline? 
'''
def suma_pares(lista):
    return sum(x for x in lista if x % 2 == 0)
print(suma_pares([1, 2, 3, 4, 5, 6]))

'''
     Ejercicio 3: Área y perímetro de un rectángulo 
       Objetivo: Calcular múltiples valores en una función. 
          Instrucciones: 
1. Crea una función rectángulo que reciba longitud y anchura. 
2. Retorna una tupla con el área y el perímetro. 
o Fórmulas: 
▪ Área = longitud * anchura. 
▪ Perímetro = 2 * (longitud + anchura). 
      Preguntas de reflexión: 
• ¿Por qué usar una tupla en lugar de una lista? 
• ¿Cómo validarías que las dimensiones sean positivas? 
'''
def rectangulo(longitud, anchura):
    area = longitud * anchura
    perimetro = 2 * (longitud + anchura)
    return (area, perimetro)
print(rectangulo(5, 3))

'''
      Ejercicio 4: Conversión de temperatura 
       Objetivo: Convertir temperaturas con condiciones. 
          Instrucciones: 
1. Define una función convertir_temperatura que reciba: 
o Temperatura en Celsius. 
o Unidad de destino ("F" o "K"). 
2. Retorna la temperatura convertida usando: 
o Fahrenheit: F = C * 9/5 + 32. 
o Kelvin: K = C + 273.15. 
      Preguntas de reflexión: 
• ¿Qué pasa si se ingresa una unidad no válida? 
• ¿Cómo extenderías la función para convertir entre otras unidades? 
'''
def convertir_temperatura(celsius, unidad):
    if unidad == "F":
        return celsius * 9/5 + 32
    elif unidad == "K":
        return celsius + 273.15
    else:
        return None
print(convertir_temperatura(25, "F"))
print(convertir_temperatura(25, "K"))

'''
     Ejercicio 5: Verificador de números primos 
       Objetivo: Implementar una función para detectar primos. 
          Instrucciones: 
1. Crea una función es_primo que reciba un entero positivo. 
2. Retorna True si es primo (solo divisible por 1 y sí mismo), False en caso 
contrario. 
o Ejemplo: 7 → True, 8 → False. 
      Preguntas de reflexión: 
• ¿Cómo optimizarías la función para números grandes? 
• ¿Qué estructura de control es más eficiente aquí: for o while? 
'''
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
print(es_primo(7))
print(es_primo(8))

'''
        Ejercicio 6: Promedio de calificaciones 
       Objetivo: Calcular promedios con funciones. 
          Instrucciones: 
1. Define una función promedio_calificaciones que reciba una lista de notas 
(0 a 10). 
2. Retorna el promedio. Si la lista está vacía, retorna 0. 
o Ejemplo: [8.5, 9.0, 7.5, 8.0] → 8.25. 
      Preguntas de reflexión: 
• ¿Cómo manejarías notas fuera del rango 0-10? 
• ¿Qué ventaja tiene retornar 0 en lugar de None para listas vacías? 
'''
def promedio_calificaciones(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)
print(promedio_calificaciones([8.5, 9.0, 7.5, 8.0]))
print(promedio_calificaciones([]))

'''
     Ejercicio 7: Factorial con validación 
       Objetivo: Combinar funciones para validar y calcular. 
          Instrucciones: 
1. Usa dos funciones: 
o validar_entrada: Verifica si un número es entero no negativo. 
o factorial: Calcula el factorial (ej: 5! = 120). 
2. El programa principal debe: 
o Pedir un número al usuario. 
o Validarlo y mostrar el factorial o un error. 
      Preguntas de reflexión: 
• ¿Por qué separar la validación del cálculo? 
• ¿Cómo manejarías el desbordamiento para números grandes? 
'''
def validar_entrada(numero):
    return isinstance(numero, int) and numero >= 0
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado
numero_usuario = 5
if validar_entrada(numero_usuario):
    print(f"Factorial de {numero_usuario}: {factorial(numero_usuario)}")
else:
    print("Error: Ingrese un entero no negativo.")

'''
     Ejercicio 8: Números primos con funciones auxiliares 
       Objetivo: Modularizar la lógica de primos. 
          Instrucciones: 
1. Usa dos funciones: 
o es_divisible: Retorna True si un número divide a otro. 
o es_primo: Usa es_divisible para verificar si es primo. 
2. El programa principal pide un número y muestra si es primo. 
      Preguntas de reflexión: 
• ¿Cómo reutilizarías es_divisible en otros contextos? 
• ¿Qué optimizaciones aplicarías a es_primo? 
'''
def es_divisible(a, b):
    return a % b == 0
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if es_divisible(numero, i):
            return False
    return True
numero_usuario = 11
print(f"¿{numero_usuario} es primo? {es_primo(numero_usuario)}")

'''
      Ejercicio 9: Conversor de temperatura con menú 
       Objetivo: Integrar funciones con interacción de usuario. 
          Instrucciones: 
1. Usa tres funciones: 
o convertir_a_fahrenheit: Convierte Celsius a Fahrenheit. 
o convertir_a_kelvin: Convierte Celsius a Kelvin. 
o menu_conversion: Muestra un menú para elegir la unidad. 
2. El programa principal: 
o Pide la temperatura en Celsius. 
o Muestra el resultado según la unidad elegida. 
      Preguntas de reflexión: 
• ¿Cómo mejorarías la experiencia de usuario del menú? 
• ¿Qué pasa si el usuario ingresa una opción inválida? 
'''
def convertir_a_fahrenheit(celsius):
    return celsius * 9/5 + 32
def convertir_a_kelvin(celsius):
    return celsius + 273.15
def menu_conversion():
    print("Elige la unidad de conversión:")
    print("1. Fahrenheit")
    print("2. Kelvin")
    opcion = input("Opción (1/2): ")
    return opcion
celsius_usuario = 25
opcion = menu_conversion()
if opcion == "1":
    print(f"{celsius_usuario}°C = {convertir_a_fahrenheit(celsius_usuario)}°F")
elif opcion == "2":
    print(f"{celsius_usuario}°C = {convertir_a_kelvin(celsius_usuario)}K")
else:
    print("Opción inválida.")


'''
     Ejercicio 10: Rectángulo con validación 
       Objetivo: Validar entradas antes de calcular. 
          Instrucciones: 
1. Usa tres funciones: 
o validar_dimensiones: Verifica que longitud y anchura sean positivas. 
o calcular_area: Retorna el área del rectángulo. 
o calcular_perimetro: Retorna el perímetro. 
2. El programa principal: 
o Pide las dimensiones al usuario. 
o Valida y muestra resultados o un error. 
      Preguntas de reflexión: 
• ¿Por qué es importante validar las entradas? 
• ¿Cómo extenderías el programa para otras figuras geométricas?
'''
def validar_dimensiones(longitud, anchura):
    return longitud > 0 and anchura > 0
def calcular_area(longitud, anchura):
    return longitud * anchura
def calcular_perimetro(longitud, anchura):
    return 2 * (longitud + anchura) 
longitud_usuario = 5
anchura_usuario = 3
if validar_dimensiones(longitud_usuario, anchura_usuario):
    print(f"Área: {calcular_area(longitud_usuario, anchura_usuario)}")
    print(f"Perímetro: {calcular_perimetro(longitud_usuario, anchura_usuario)}")
else:
    print("Error: Las dimensiones deben ser positivas.")