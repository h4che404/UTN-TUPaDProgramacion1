#Crea una función recursiva que calcule el factorial de un número. 
#Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario
print("Punto 1")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Ingrese un numero entero positivo para calcular factoriales hasta ese numero: "))
for i in range(1, num + 1):
    print(f"Factorial de {i} es {factorial(i)}")

#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.
print("Punto 2")
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
pos = int(input("Ingrese la posicion hasta la cual desea ver la serie de Fibonacci: "))
for i in range(pos + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")   

#Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
# Prueba esta función en un algoritmo general.
print("Punto 3")
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
if exponente < 0:
    print("El exponente debe ser un entero no negativo.")
else:
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es {resultado}")
#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.
#Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
#unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
#procedimiento:
#1. Dividir el número por 2.
#2. Guardar el resto (0 o 1).
#3. Repetir el proceso con el cociente hasta que llegue a 0.
#4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
print("Punto 4")
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
num = int(input("Ingrese un numero entero positivo para convertir a binario: "))
if num < 0:
    print("Por favor, ingrese un numero entero positivo.")
else:
    print(f"El numero {num} en binario es: {decimal_a_binario(num)}")
#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().
print("Punto 5")
def es_polindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_polindromo(palabra[1:-1])
palabra = input("Ingrese una palabra para verificar si es palindromo: ").lower()
if es_polindromo(palabra):
    print(f"La palabra '{palabra}' es un palindromo.")
# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
#Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión
print("Punto 6")
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
numero = int(input("Ingrese un numero entero positivo para sumar sus digitos: "))
if numero < 0:
    print("Por favor, ingrese un numero entero positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los digitos de {numero} es: {resultado}")
#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide
print("Punto 7")
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)
niveles = int(input("Ingrese la cantidad de bloques en el nivel mas bajo de la piramide: "))
if niveles < 0:
    print("Por favor, ingrese un numero entero positivo.")
else:
    total_bloques = contar_bloques(niveles)
    print(f"El total de bloques necesarios para construir la piramide es: {total_bloques}")

#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
num = int(input("Ingrese un numero entero positivo: "))
dig = int(input("Ingrese un digito entre 0 y 9 para contar en el numero: "))
if num < 0 or dig < 0 or dig > 9:
    print("Ingrese un numero entero positivo y un digito valido.")
else:
    cantidad = contar_digito(num, dig)
    print(f"El digito {dig} aparece {cantidad} veces en el numero {num}.")