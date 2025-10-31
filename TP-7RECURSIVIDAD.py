print("Punto 1")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def mostrar_factoriales(n, i=1):
    if i > n:
        return
    print(f"{i}! = {factorial(i)}")
    mostrar_factoriales(n, i + 1)

num = int(input("Ingrese un número: "))
mostrar_factoriales(num)
print("Punto 2")
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci(pos, i=0):
    if i > pos:
        return
    print(fibonacci(i), end=" ")
    mostrar_fibonacci(pos, i + 1)

pos = int(input("\nIngrese la posición de Fibonacci: "))
print("Serie de Fibonacci:")
mostrar_fibonacci(pos)
print()
print("Punto 3")
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")
print("Punto 4")
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

n = int(input("Ingrese un número decimal: "))
resultado = decimal_a_binario(n)
if resultado == "":
    resultado = "0"
print(f"El número {n} en binario es: {resultado}")
print("Punto 5")
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()
if es_palindromo(texto):
    print("Es un palíndromo ✅")
else:
    print("No es un palíndromo ❌")
print("Punto 6")
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número para sumar sus dígitos: "))
print(f"Suma de los dígitos: {suma_digitos(num)}")
print("Punto 7")
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese el número de bloques del nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")
print("Punto 8")
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número: "))
dig = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {dig} aparece {contar_digito(numero, dig)} veces.")

