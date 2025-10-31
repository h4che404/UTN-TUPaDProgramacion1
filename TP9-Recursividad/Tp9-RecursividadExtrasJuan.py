#Crear una función recursiva suma_pares(n) que calcule la suma de todos
#los números pares desde 2 hasta n
print("Punto 1")
def suma_pares(n):
    if n < 2:
        return 0
    elif n % 2 == 0:
        return n + suma_pares(n - 2)
    else:
        return suma_pares(n - 1)
resultado = suma_pares(10)
print(f"La suma de los numeros pares desde 2 hasta 10 es: {resultado}")
#Crear una función recursiva contar_letra(palabra, letra) que cuente cuántas
#veces aparece una letra dentro de una cadena de texto.
print("Punto 2")
def contar_letra(palabra, letra):
    if len(palabra) == 0:
        return 0
    elif palabra[0] == letra:
        return 1 + contar_letra(palabra[1:], letra)
    else:
        return contar_letra(palabra[1:], letra)
print(f"La letra 'r' aparece {contar_letra('recursividad', 'r')} veces en la palabra 'recursividad'")
#Definir una función recursiva invertir_cadena(texto) que devuelva el texto
#invertido
print("Punto 3")
def invertir_cadena(texto):
    if len(texto) == 0:
        return ""
    else:
        return texto[:-1] + invertir_cadena(texto[:-1])
print(f"La cadena 'recursividad' invertida es: {invertir_cadena('recursividad')}")
#Diseñar una función recursiva contar_elementos(lista) que cuente la
#cantidad total de elementos en una lista, sin usar len().
print("Punto 4")
def contar_elementos(lista):
    if lista == []:
        return 0
    else:
        return 1 + contar_elementos(lista[1:])
print(f"La cantidad de elementos en la lista [1, 2, 3, 4, 5] es: {contar_elementos([1, 2, 3, 4, 5])}")
#Crear una función recursiva contiene_letra(palabra, letra) que indique si
#una letra está presente en la palabra.
print("Punto 5")
def contiene_palabra(palabra, letra):
    if len(palabra) == 0:
        return False
    elif palabra[0] == letra:
        return True
    else:
        return contiene_palabra(palabra[1:], letra)
print(f"La letra 'a' {'esta' if contiene_palabra('recursividad', 'a') else 'no esta'} en la palabra 'recursividad'")

#Definir una función recursiva multiplicar(a, b) que calcule la multiplicación
#de dos números utilizando solo sumas.
print("Punto 6")
def multiplicar(a, b):
    if b == 0:
        return 0
    else:
        return a + multiplicar(a, b - 1)
num1 = int(input("Ingrese el primer numero a multiplicar: "))
num2 = int(input("Ingrese el segundo numero a multiplicar: "))
print(f"La multiplicacion de {num1} y {num2} es: {multiplicar(num1, num2)}")

#Crear una función recursiva llamada cuenta_regresiva(n) que reciba un
#número entero positivo y muestre todos los números desde n hasta 1, en
#orden descendente.
print("Punto 7")
def cuenta_regresiva(n):
    if n <= 0:
        return
    else:
        print(n)
        cuenta_regresiva(n - 1)
num = int(input("Ingrese un numero para la cuenta regresiva: "))
cuenta_regresiva(num)

#Crear una función recursiva llamada mostrar_letras(palabra) que reciba
#una cadena de texto y la muestre letra por letra, una debajo de otra, usando
#recursividad.
print("Punto 8")
def mostrar_letras(palabra):
    if len(palabra) == 0:
        return
    else:
        print(palabra[0])
        mostrar_letras(palabra[1:])
palabra_agreg = input("Ingrese una palabra para mostrar sus letras: ")
mostrar_letras(palabra_agreg)
