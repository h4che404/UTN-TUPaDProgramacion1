#Trabajo adicional
#1 Escribir un programa que pida al usuario una palabra y la muestre por 
#pantalla 10 veces.
palabra = input("Ingrese una palabra: ")
for i in range(1,11):
    print(i, palabra)
#2 Escribir un programa que pregunte al usuario su edad y muestre por 
#pantalla todos los años que ha cumplido (desde 1 hasta su edad). 
edad = int(input("Ingrese su edad: "))
edad += 1
for i in range(1,edad):
    print(f"años cumplidos: {i}")
#3 Escribir un programa que pida al usuario un número entero y muestre 
#por pantalla un triángulo rectángulo como el de más abajo, de altura el 
#número introducido
altura = int(input("Ingrese la altura del triÃ¡ngulo rectangulo: "))
altura += 1
for i in range(0,altura):
    for j in range(0,i):
        print("*",end="")
print("\n") 
#4 Escribir un programa que muestre por pantalla la tabla de multiplicar 
#del 1 al 10. 
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}\n")
#5 Escribir un programa que almacene la cadena de 
#caracteres contraseña en una variable, pregunte al usuario por la 
#contraseña hasta que introduzca la contraseña correcta 
contrasena = "contraseña"
correcto = 0
print("Ingrese la contraseña: ")
while correcto == 0:
    contra_usuario = input()
    if contra_usuario == contrasena:
        correcto = 1
        print("Contraseña correcta: ")
    else:
        print("Vuelve a intentar: ")
#6 Escribir un programa que muestre el eco de todo lo que el usuario 
#introduzca hasta que el usuario escriba “salir” que terminará.  
palabra = input("Ingrese algo: ")
while palabra.lower() != "salir":
    print(palabra)
palabra = input("Ingrese algo: ")
#7 Escribe un bucle for que imprima los números pares del 2 al 20 (inclusive).  
for i in range(2,21):
    if i % 2 == 0:
        print(i)
print("")
#8 Imprime números del 1 al 100, pero: 
#Para múltiplos de 3 → "Fizz".  
#Para múltiplos de 5 → "Buzz".  
#Para múltiplos de ambos → "FizzBuzz". 
for i in range(1,101):
    if i % 3 == 0:
        print(f"{i} -> Fizz")  
    elif i % 5 == 0:
        print(f"{i} -> Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print(f"{i} -> FizzBuzz")

#9 Desarrollar un programa que solicite la carga de 10 números e imprima 
#la suma de los últimos 5 valores ingresados. 

for i in range(0,10):
    num = int(input())
    if i == 5:
        suma = 0
        suma += num
print(f"La suma de los ultimos 5 nummeros ingresados es: {suma}")
#10Realizar un programa que lea los lados de n triángulos. 
#Informar después de cada triángulo si es equilátero (tres lados iguales), 
#isósceles (dos lados iguales) o escaleno (ningún lado igual). Informar 
#después del total de triángulos de cada tipo.
quilateros = 0
isosceles = 0
escalenos = 0
n = int(input("Ingrese los lados del triangulos a evaluar: "))
for i in range(n):
    lado1 = float(input(f"Ingrese el lado 1 del triangulo {i + 1}: "))
    lado2 = float(input(f"Ingrese el lado 2 del triangulo {i + 1}: "))
    lado3 = float(input(f"Ingrese el lado 3 del triangulo {i + 1}: "))
    if lado1 == lado2 == lado3:
        print("El triangulo es equilatero.")
        equilateros += 1
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triangulo es isosceles.")
        isosceles += 1
    else:
        print("El triangulo es escaleno.")
        escalenos += 1
print(f"Total de triangulos equilateros: {equilateros}")
print(f"Total de triangulos isosceles: {isosceles}")
print(f"Total de triangulos escalenos: {escalenos}")