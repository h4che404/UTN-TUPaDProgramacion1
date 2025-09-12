'''
Escribir un programa que pida al usuario una palabra y la muestre por
pantalla 10 veces.
'''

palabra = str(input("Ingrese una palabra"))
for i in range (10):
    print(palabra)

'''
Escribir un programa que pregunte al usuario su edad y muestre por
pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

edad = int(input("Ingrese su edad:"))

for i in range(edad):
    print(i+1)

'''
Escribir un programa que pida al usuario un número entero y muestre
por pantalla un triángulo rectángulo como el de más abajo, de altura el
número introducido.
*
**
***
****
*****
'''

letra = "*"
num2 = int(input("ingrese un numero entero:"))
for i in range(1, num2 + 1):
    print(letra * i)

    
'''
Escribir un programa que muestre por pantalla la tabla de multiplicar
del 1 al 10.
'''

for i in range(1, 11):
    for j in range(1, 11):
        print(j * i, end="|")
    print("\n")

'''
Escribir un programa que almacene la cadena de
caracteres contraseña en una variable, pregunte al usuario por la
contraseña hasta que introduzca la contraseña correcta
'''

contraseña = "contraseña"
ingreso = str(input("Ingrese la contraseña:"))
while ingreso != contraseña:
    ingreso = str(input("Contraseña incorrecta, ingrese nuevamente:"))
print("Contraseña correcta")

'''
Escribir un programa que muestre el eco de todo lo que el usuario
introduzca hasta que el usuario escriba “salir” que terminará.
'''

ingreso = str(input("Ingrese algo:"))
while ingreso.lower() != "salir":
    print(ingreso)
    ingreso = str(input("Ingrese algo:"))
print("Programa terminado")

'''
Escribe un bucle for que imprima los números pares del 2 al 20
(inclusive).
'''

for i in range(2, 21, 2):
    print(i)

'''
Imprime números del 1 al 100, pero:
Para múltiplos de 3 → "Fizz".
Para múltiplos de 5 → "Buzz".
Para múltiplos de ambos → "FizzBuzz".
'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


'''
Desarrollar un programa que solicite la carga de 10 números e imprima
la suma de los últimos 5 valores ingresados.
'''

suma = 0
for i in range(10):
    num = int(input("Ingrese un numero:"))
    if i >= 5:
        suma += num
print(f"La suma de los ultimos 5 numeros es: {suma}")


'''
Realizar un programa que lea los lados de n triángulos.
Informar después de cada triángulo si es equilátero (tres lados iguales),
isósceles (dos lados iguales) o escaleno (ningún lado igual). Informar
después del total de triángulos de cada tipo.
'''

equilateros = 0
isosceles = 0
escalenos = 0
n = int(input("Ingrese la cantidad de triángulos a evaluar: "))
for i in range(n):
    lado1 = float(input(f"Ingrese el lado 1 del triángulo {i + 1}: "))
    lado2 = float(input(f"Ingrese el lado 2 del triángulo {i + 1}: "))
    lado3 = float(input(f"Ingrese el lado 3 del triángulo {i + 1}: "))
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
        equilateros += 1
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
        isosceles += 1
    else:
        print("El triángulo es escaleno.")
        escalenos += 1
print(f"Total de triángulos equiláteros: {equilateros}")
print(f"Total de triángulos isósceles: {isosceles}")
print(f"Total de triángulos escalenos: {escalenos}")
