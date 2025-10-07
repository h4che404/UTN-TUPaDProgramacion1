"crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 incluyendo ambos extremos), en orden creciente, mostrando un número por línea"
# punto 1
for i in range(101):
    print(i)

print("------------------")
""" Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene""" 
# punto 2
num = int(input("ingrese un numero entero: "))
contador = 0
for i in str(abs(num)):
    contador += 1
print(f" el numero {num} tiene {contador} digitos")

print("------------------")
"""Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores"""
# punto 3
num1 = int(input("ingrese el primer numero entero:"))
num2 = int(input("ingrese el segundo numero entero:"))
suma = 0
for i in range(num1 + 1, num2):
    suma += i
print(f"la suma de los nemeros entre {num1} y {num2}, excluyendo ambos es : {suma}")

print("------------------")
"""Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0"""
# punto 4
suma = 0
while True:
    num = int(input("ingrese un numero entero (0 para finalizar)"))
    if num == 0:
        break
    suma += num
print(f"la suma total acumulada es: {suma}")

print("------------------")
""""Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número"""
# punto 5
import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
for i in range(100): # limitar a 100 intentos para evitar bucles infinitos
    intentos += 1
    intento = int(input("adivina el numero (entre 0 y 9):"))
    if intento == numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos")
        break
    else:
        print("Número incorrecto, intenta de nuevo")
else:
    print(f"Lo siento, no adivinaste el número {numero_aleatorio}.")
    
    print("------------------")
    """Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente"""
    #punto 6
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)
    print("------------------")
    
    """Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio"""
#punto 8


par = 0
impar = 0
positivo = 0
negativo = 0


for i in range (100):
    num4 = int(input("ingrese un numero entero"))
    if num4 % 2 == 0:
        par += 1
    elif num4 % 2 != 0:
        impar += 1
    if num4 < 0:
        negativo += 1
    elif num4 > 0:
        positivo += 1
    else:
        print ("no es un numero")

print(f"Los pares:{par}, Los impares:{impar}, Los positivos:{positivo}, Los negativos:{negativo}")

print("------------------")

""" Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor"""
#punto 9

media = 0
num5 = 0
for i in range(100):
    num5 += input("Ingrese numeros enteros")

media = num5 / 100
print(media)

print("------------------")

"""Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745"""
#punto 10
num6 = input("ingrese un nuemro entero:")
num_invertido = num6[::-1]
print(f"el nuemro invertido es: {num_invertido}")
        