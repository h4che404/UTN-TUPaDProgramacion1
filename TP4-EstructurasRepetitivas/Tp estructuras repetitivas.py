#Anglat Juan
#Tp estructuras repetitivas
print("TP Estuctuas Repetitivas")


"""

1) Crea un programa que imprima en pantalla todos los numeros enteros desde 0 hasta 100 

(incluyendo ambos extremos), en orden creciente, mostrando un nÃºmero por lÃ­nea.

"""
#Actividad 1
i = 0
for i in range(101):
    print (i)
    i = i + 1
print("------------------------------")

"""

2) Desarrolla un programa que solicite al usuario un nÃºmero entero y determine la cantidad de 

dÃ­gitos que contiene.

"""
#Actividad 2
num = int(input("ingrese un numero: "))
n = abs(num)
if n == 0:
    cant_digitos = 1
else:
    cant_digitos = 0
    for i in range(100):
        if n == 0:
            break
        n = n // 10
        cant_digitos += 1

print(f"El número {num} tiene {cant_digitos} dígitos.")

print("------------------------------")

"""
3) Escribe un programa que sume todos los numeros enteros comprendidos entre dos valores 

dados por el usuario, excluyendo esos dos valores.

"""
#Actividad3
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un segundo numero: "))
if num1 > num2:
    num1, num2 = num2, num1
    suma = 0
for i in range(num1 + 1, num2):
   suma += i 
   print(f"la suma entre {num1} y {num2}, excluyendo los extremos es: {suma}")

print("------------------------------")

"""

4) Elabora un programa que permita al usuario ingresar numeros enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0.

"""
#Actividad 4
suma = 0
while True:
    a = int(input("ingrese un numero entero (ingrese el numero 0 para finalizar): "))
    if a == 0:
        break
    suma1 =+ a
    print(f"el total de numeros acumlados es de: {suma1}")

print("------------------------------")

"""

5) Crea un juego en el que el usuario deba adivinar un numero aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuantos intentos fueron necesarios para acertar el numero.

"""
#Actividad 5
import random
num_secreto = random.randint(0,9)
intentos = 0
acertado = False

print("Adivina el numero secreto (entre 0 y 9)")

while not acertado:
    intento = int(input("Ingresa tu numero: "))
    intentos += 1
    if intento == num_secreto:
        acertado = True
    else:
        print("has fallado, intenta de nuevo...")

print(f"Acertaste, El numero secreto era {num_secreto}.")
print(f"Te hicieron falta {intentos} intentos para acertar.")

print("------------------------------")

"""

6) Desarrolla un programa que imprima en pantalla todos los numeros pares comprendidos 

entre 0 y 100, en orden decreciente.

"""
#Actividad 6
for i in range(100, -1, -2):
    print (i)


print("------------------------------")

"""

7) Crea un programa que calcule la suma de todos los numeros comprendidos entre 0 y un 
numero entero positivo indicado por el usuario.

"""
#Actividad 7
num3 = int(input("Introduce un numero entero positivo: "))
if num3 < 0:
    print("El numero debe ser un entero positivo.")
else:
    suma = 0
    for i in range(num3 + 1):  # incluye el número indicado
        suma += i
print(f"La suma de los numeros desde 0 hasta {num3} es: {suma}")

print("------------------------------")

"""

8) Escribe un programa que permita al usuario ingresar 100 nÃºmeros enteros. Luego, el

programa debe indicar cuÃ¡ntos de estos nÃºmeros son pares, cuÃ¡ntos son impares, cuÃ¡ntos son 

negativos y cuÃ¡ntos son positivos. (Nota: para probar el programa puedes usar una cantidad 

menor, pero debe estar preparado para procesar 100 nÃºmeros con un solo cambio).

"""
#Actividad8
total_numeros = 100 
pares = 0
impares = 0
positivos = 0
negativos = 0
print(f"Introduce {total_numeros} numeros enteros:")

for i in range(total_numeros):
      numero = int(input(f"Numero {i+1}: "))
if numero % 2 == 0:
        pares += 1
else:
     impares += 1

if numero > 0:
        positivos += 1
elif numero < 0:
        negativos += 1

print("\n--- Resultados ---")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")



print("------------------------------")

"""

9) Elabora un programa que permita al usuario ingresar 100 nÃºmeros enteros y luego calcule la 

media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 

poder procesar 100 nÃºmeros cambiando solo un valor).

"""
#Actividad 9
total_numeros = 100
suma = 0
print(f"Introduce {total_numeros} numeros enteros:")
for i in range(total_numeros):
    numero = int(input(f"numero {i+1}: "))
    suma += numero
    media = suma / total_numeros
print("\n--- Resultado ---")
print(f"La media de los {total_numeros} numeros ingresados es: {media}")

print("------------------------------")

"""

10) Escribe un programa que invierta el orden de los digitos de un nummero ingresado por el 

usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

"""
#Actividad 10
numero = int(input("Ingresa un número entero: "))
numero = abs(numero)
numero_invertido = 0
while numero != 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10
print(f"El número invertido es: {numero_invertido}")
print("------------------------------")
