print("Punto 1")
def suma_pares(n):
    if n < 2:
        return 0
    if n % 2 != 0:
        n -= 1
    return n + suma_pares(n - 2)

n = int(input("Ingrese un número: "))
print("Suma de pares:", suma_pares(n))

print("Punto 2")
def contar_letra(palabra, letra):
    if palabra == "":
        return 0
    if palabra[0] == letra:
        return 1 + contar_letra(palabra[1:], letra)
    else:
        return contar_letra(palabra[1:], letra)

palabra = input("\nIngrese una palabra: ")
letra = input("Ingrese una letra: ")
print("Cantidad de veces:", contar_letra(palabra, letra))

print("Punto 3")
def invertir_cadena(texto):
    if texto == "":
        return ""
    return invertir_cadena(texto[1:]) + texto[0]

texto = input("\nIngrese un texto: ")
print("Texto invertido:", invertir_cadena(texto))

print("Punto 4")
def contar_elementos(lista):
    if lista == []:
        return 0
    return 1 + contar_elementos(lista[1:])

lista = input("\nIngrese elementos separados por espacio: ").split()
print("Cantidad de elementos:", contar_elementos(lista))

print("Punto 5")
def contiene_letra(palabra, letra):
    if palabra == "":
        return False
    if palabra[0] == letra:
        return True
    return contiene_letra(palabra[1:], letra)

palabra = input("\nIngrese una palabra: ")
letra = input("Ingrese una letra: ")
print("Contiene la letra:", contiene_letra(palabra, letra))

print("Punto 6")
def multiplicar(a, b):
    if b == 0:
        return 0
    if b > 0:
        return a + multiplicar(a, b - 1)
    else:
        return -multiplicar(a, -b)

a = int(input("\nIngrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
print("Resultado de la multiplicación:", multiplicar(a, b))

print("Punto 7")
def cuenta_regresiva(n):
    if n == 0:
        return
    print(n)
    cuenta_regresiva(n - 1)

n = int(input("\nIngrese un número para cuenta regresiva: "))
cuenta_regresiva(n)

print("Punto 8")
def mostrar_letras(palabra):
    if palabra == "":
        return
    print(palabra[0])
    mostrar_letras(palabra[1:])

palabra = input("\nIngrese una palabra: ")
mostrar_letras(palabra)
