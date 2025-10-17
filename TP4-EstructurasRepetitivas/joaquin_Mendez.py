print("TP Estuctuas Repetitivas")

"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
print("PUNTO 1")
for i in range(0,101):
    print(i)

print("------------------------------")
"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene.
"""
print("PUNTO 2")
num = input("Ingrese un númeo entero:")
print(f"El número {num} contiene {len(num)} dígitos")
print("------------------------------")
"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores.
"""
print("PUNTO 3")
suma = 0
num1 =int(input("Ingrese un número:"))
num2 = int(input("Ingrese otro un número:"))
num1+=1
for i in range(num1, num2):
    suma +=i
print(f"la sumatoria entre {num1} y {num2} da {suma}")

print("------------------------------")
"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0.
"""
print("PUNTO 4")

suma = 0
fin = 1
print("Ingrese un número entero:")
while fin == 1:
    num = input()
    suma += num
    print("El valo es: ",suma)
    if num == 0:
        print("El esultado final es:",suma)
        fin = 0
print("------------------------------")
"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
import random
print("PUNTO 5")
alea = random.randit(1, 20)
valor = 1
contador = 0
while valor == 1:
    num = print(input("Adivina un número del 1 al 20"))
    contador +=1
    if valor != num:
       valor = 0
print(f"Cantidad de intentos: {contador}")


print("------------------------------")
"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente.
"""
print("PUNTO 6")
for i in range(101,0):
    if i % 2 == 0:
        print(i)


print("------------------------------")
"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario.
"""
print("PUNTO 6")
suma = 0
num = int(input("Ingrese un número entero positivo:"))
for i in range(0, num):
    suma += i
    print(suma)
print("------------------------------")
"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
print("PUNTO 8")
negativos = 0
positivos = 0
pares = 0
impares = 0 
print("Ingrese 100 números enteros")
for i in 100:
    num = int(input())
    if num < 0:
        negativo += 1
    if num > 0:
        positivo += 1
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Cantidad de pares {par} \n impares {impar} \n positivos {positivo} \n negativos {negativo} ")

print("------------------------------")
"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor).
"""
print("PUNTO 9")

cantidad_numeros = 100
contador = 0
suma = 0

print("Ingresa", cantidad_numeros, "números enteros:")

while contador < cantidad_numeros:
    numero = input("Número #" + str(contador + 1) + ": ")
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        suma += numero
        contador += 1
    else:
        print("Entrada inválida. Por favor, ingresa un número entero.")

media = suma / cantidad_numeros
print("La media de los", cantidad_numeros, "números es:", media)


print("------------------------------")
"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
print("PUNTO 10")
numero = input("Ingresa un número: ")

negativo = False
if numero[0] == '-':
    negativo = True
    numero = numero[1:]

digitos = []
i = 0
while i < len(numero):
    digitos.append(int(numero[i]))
    i += 1

n = len(digitos)
i = 0
while i < n:
    j = n - 1
    while j > i:
        temp = digitos[j]
        digitos[j] = digitos[j - 1]
        digitos[j - 1] = temp
        j -= 1
    i += 1

inverso = 0
i = 0
while i < len(digitos):
    inverso = inverso * 10 + digitos[i]
    i += 1

if negativo:
    inverso = -inverso

print("Número invertido:", inverso)

print("------------------------------")