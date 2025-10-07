"""escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces"""
#punto 1
palabra = input("ingrese una palabra:")
for i in range(10):
    print(palabra)
    
print("--------")
"""escribir un programa que le pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido(desde 1 hasta su edad actual)"""
#punto 2
edad = int(input("ingrese se edad "))
for i in range(1, edad + 1):
    print(f"Año {i}: Cumplí {i} años")
    
    print("---------")
    """escribir un programa que pida al usuario un numero y muestre pro panatalla un triangulo rectangulo como el de mas abajo, de altura el numero introduciodo"""
#PUNTO 3
num = int(input("ingrese un numero"))
for i in range(1, num + 1):
    print("*" * i)
    print("---------")
    """escribir un programa que muestre por pantalla la tabla  de multiplicar de 1 al 10"""
#punto 4
num = int(input("ingrese un numero para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("---------")
"""escribir un programa que  almacen la cadena de caracteres "contraseña" en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta"""
#punto 5
contrasena = "ponti32"
while True:
    ingreso = input("ingrese la contraseña:")
    if ingreso == contrasena:
        print("contraseña correcta")
        break
    else:
        print(" contacseña incorrecta, intente de nuevo")
print("---------")
"""escribir un programa que muestre eco de todo lo que el usauario untridusca hasta que el usuario escriba "salir" que terminará"""
#punto 6
while True:
    entrada = input('ingrese algo (escriba "salir" para terminar):')
    if entrada.lower() == " salir":
        print("programa termianado")
        print("---------")
        """escribe un bucle que imprima  los nuemros pares del 2 al 20"""
        #punto 7
        num =print("ingrese un numero")
        for i in range(2, 21, 2):
            print(i)
            
    print("---------")
    """imprime nuemros del 1 al 100 pero : para multiplos ->"fizz" para multiplos de 5 ->"buzz" para multiplos de 3 y 5 ->"fizzbuzz"""
#punto 8
    num = int(input("ingrese un numero"))
    for i in range(1,100, 3):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
    else:
        if i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        print("----------")
        """desarrollar un programa que solicite la caraga de 10 numeros e imprima su suma de los ultimos 5 valores ingrsados"""
        #punto 9
        numeros = []
        for i in range(10):
            num = int(input("ingrese un nuemro"))
        numeros.append(num)
        suma_ultimos_cinco = sum(numeros[-5:])
        print(f"La suma de los últimos 5 números es: {suma_ultimos_cinco}")
        print("-------")
         


