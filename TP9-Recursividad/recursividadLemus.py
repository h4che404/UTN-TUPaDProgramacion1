''' Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario'''

def facto(numero):
    if numero == 1:
        return 1
    else:
        return numero * facto(numero-1)
    
num = int(input("Ingrese un número entero positivo: "))

for i in range(1, num + 1):
    print(f"El factorial de {i} es {facto(i)}")

'''Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
'''
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)
    
pos = int(input("Ingrese la posición hasta donde desea ver la serie de Fibonacci: "))
for i in range(pos + 1):
    print(f"Fibonacci de {i} es {fibonacci(i)}")

'''Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1)
. Prueba esta función en un
algoritmo general.'''

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base} elevado a {exponente} es {potencia(base, exponente)}")

'''Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.'''

def binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return binario(numero // 2) + str(numero % 2)
    
''' Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.'''
def invertir(palabra):
    if palabra == "":
        return ""
    else:
        return palabra[-1] + invertir(palabra[:-1])
def es_palindromo(palabra):
    palabra_invertida = invertir(palabra)
    return palabra == palabra_invertida

'''Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos'''
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
    
'''Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.

Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.'''

def contar_bloques(numero):
    if numero == 1:
        return 1
    else:
        return numero + contar_bloques(numero - 1)
    
'''Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.'''

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        cuenta = 1 if numero % 10 == digito else 0
        return cuenta + contar_digito(numero // 10, digito)