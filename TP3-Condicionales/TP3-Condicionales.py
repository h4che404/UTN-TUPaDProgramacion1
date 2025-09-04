''' ((David))
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
'''

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

'''  ((Nahuel))
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.
'''
nota=float(input("Ingrese su nota:"))
if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")

'''  ((Agus))
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.
'''
numeros = int(input("Ingrese un numero:"))
if numeros % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")




''' ((Juan))
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
'''
#pedirle al usuario que ingrese su edad y clasificarlo segun su edad
edad = int(input("ingrese su edad"))
if edad >= 0 and edad <= 12:
    print("eres un niño/a")
elif edad >= 13 and edad <= 18:
    print("eres un adolecente")
elif edad >= 18 and edad <= 30:
    print("Eres adulto/a joven")
elif edad >= 30:
    print("eres un adulto mayor")
else: print("eres un mayor de edad")

'''  ((Juan Cruz))
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
'''
# Pedir al usuario que ingrese una contraseña
contraseña = input("Ingrese una contraseña: ")

# Evaluar la longitud de la contraseña
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


'''  ((Juan Cruz))
6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números. 
'''
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("La lista de numeros aleatorios es:", numeros_aleatorios)
print("La moda es:", mode(numeros_aleatorios))
print("La mediana es:", median(numeros_aleatorios))
print("La media es:", mean(numeros_aleatorios))
if mean(numeros_aleatorios) > median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("La distribución tiene sesgo positivo (a la derecha).")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("La distribución tiene sesgo negativo (a la izquierda).")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("La distribución no tiene sesgo (simétrica).")
else:
    print("No se puede determinar un sesgo claro con estos valores.")

'''  ((Joaco))
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
'''
texto = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"
if texto and texto[-1] in vocales:
    texto += "!"
print("Resultado:", texto)

'''  ((Nahuel))
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
'''
nombre=input("Ingrese su nombre:")
print("Seleccione una opción: \n 1 : Su nombre en mayúsculas. \n 2 : Su nombre en minúsculas \n 3 : Su nombre con la primer letra mayúscula.")
opcion=int(input(""))
if opcion==1:
    print(nombre.upper())
elif opcion==2:
    print(nombre.lower())
elif opcion==3:
    print(nombre.title())
else:
    print("Opción inválida")
'''  ((Juan))
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
'''
#el usuario debe ingresar la magnitud del terremto y el programa debe clasificarla

magnitud = float(input("ingrese la magnitud del terremoto"))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:  
    print("Extremo (puede causar graves daños a gran escala).")

'''  ((Agus))
10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
''' 
hesmisferio = input("Ingrese en que hemisferio se encuentra (N/S): ")
mes = int(input("Ingrese el mes en numero (1-12): "))
dia = int (input("ingrese el dia de mes (1-31): "))

if hesmisferio == "N":
    if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Estás en primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 22):
        print("Estás en verano")
    elif (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Estás en otoño")
    elif (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Estás en invierno")
    else:
        print("Los datos ingresados no son correctos")
        if hesmisferio == "S":
            if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
                print("Estás en otoño")
            elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 22):
                print("Estás en invierno")
            elif (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
                print("Estás en primavera")
            elif (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
                print("Estás en verano")
            else:
                print("Los datos ingresados no son correctos")
