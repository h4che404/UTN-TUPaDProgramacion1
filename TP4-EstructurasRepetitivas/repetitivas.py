#Practico 4: Estructuras repetitivas
#Nahuel Lemus

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numusuario = int(input("Ingrese un número entero:"))
contador = 0
while numusuario != 0:
    numusuario = numusuario - (numusuario % 10)
    numusuario = numusuario / 10
    contador = contador + 1
print(f"El número tiene {contador} digitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

rangoinferior = int(input("Ingrese el primer número entero:")) + 1
rangosuperior = int(input("Ingrese el segundo número entero:"))
contador = 0
for i in range(rangoinferior, rangosuperior, 1):
    contador = contador + i
    print(contador)
print (f"La suma de los números comprendidos es: {contador}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

numusuario = int(input("Ingresa un número:"))
suma = 0
while numusuario != 0:
    suma = suma + numusuario 
    numusuario = int(input("Ingresa otro número para sumar(0 para terminar):"))
print(f"La suma es de: {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
aleatorio = random.randint(0, 9)
intento = 10
intentos = 0
while intento != aleatorio:
    intento = int(input("Intenta con un número:"))
    intentos = intentos +1
print(f"Acertaste! Tuviste un total de {intentos} intentos.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range (100, -1, -2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

rangosuperior = int(input("Ingrese el segundo número entero positivo:"))
contador = 0
if rangosuperior > 0:
    for i in range(0, rangosuperior, 1):
        contador = contador + i
        print(contador)
    print (f"La suma de los números comprendidos es: {contador}")
else: print("El número ingresado no es válido.")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contadorpares = 0
contadorimpares = 0
contadorpositivos = 0
contadornegativos = 0
for i in range(100):
    numusuario = int(input("Ingrese un número:"))
    if (numusuario % 2) == 0:
        contadorpares += 1
    elif (numusuario % 2) !=0: contadorimpares += 1
    if numusuario > 0:
        contadorpositivos += 1
    elif numusuario < 0: contadornegativos += 1
print(f"Ingresaste {contadorpares} números pares, {contadorimpares} números impares, {contadorpositivos} números positivos y {contadornegativos} números negativos.")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

suma = 0
for i in range(100):
    numusuario = int(input("Ingrese un número:"))
    suma = suma + numusuario
suma = suma / 100
print(f"El promedio de los números ingresados es de {suma}.")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numeronuevo = 0
numusuario = int(input("Ingrese un número entero:"))
cifras = len(str(numusuario))
for i in range(cifras):
    digito = numusuario % 10
    numeronuevo = numeronuevo * 10 + digito
    numusuario //= 10
print(f"La inversa es {numeronuevo}.")