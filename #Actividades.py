#Actividades
#actividad1
contrasena_correcta = "programacion1"
contrasena_usuario = input("Introduce la contraseña: ")
if contrasena_usuario == contrasena_correcta:
 print("Contraseña correcta. Bienvenido.")
else:
 print("Contraseña incorrecta. Intenta de nuevo.")
#Lo que sucede aqui, es que para ingresar el programa pide una contraseña, al ingresar la correcta 
#el programa en este caso, cambiara el valor del variable a otra y dara la bienvenida al usuario
#si se ingresa la incorrecta este ira directamente al "else" y dara contraseña incorrecta
"""
si el usuario ingresa una letra en mayuscula el programa lo tomara como error
para dar mas intentos usaria el bucle while hasta que la contraseña sea identica 
"""

#actividad2
#el usuario debe ingresar una letra y el programa debera decir si es vocal o no 
letra = input("ingrese una letra: ")
if len(letra) !=1:
    print("debes ingresar solo una letra")
elif letra in "aeiouAEIOU":
    print("la letra ingresada es vocal")
else:
    print("la letra ingresada no es vocal")
"""
para mejorar las vocales con acentuacion deberia usar una extencion que el programa
permite interpretarlas, creo.
creo que esta bien como quedo, y no creo que haga falta simplificarlo, pero seguramente con un bucle 
que dar mas intentos

"""

#actividad 3
numero = float(input("Ingrese un numero: "))

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")
"""
si el usuario ingresa una letra, el programa toma error.
y para ingresar numeros en decimales use el float para evitar ese problema
"""

#actividad 4
#Solicita dos números al usuario.
#Si el primero es mayor, imprime: "El primer número ingresado es mayor".
#Si el primero es menor, imprime: "El primer número ingresado es menor".
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))
if num1 > num2:
    print("El primer numero ingresado es mayor")
elif num1 < num2:
    print("El primer numero ingresado es menor")
else:
    print("Los numeros ingresados son iguales")
"""
para que le programa usara mas de dos numeros usaraia and u or 
y el programa entrara en error si se ingresa un valor no numerico, 
igual no use el float para valores decimales
"""
# actividad 5
temp = float(input("Ingresa la temperatura actual en °C: "))
if temp <= 10:
    print("Hace frio")
elif temp <= 25:
    print("Está templado")
else:
    print("Hace calor")
"""
para adaptar a valores °F, deberia cambiar los valores, o hacer el calculo dentro del programa
para agregar el valor de hace mucho frio usaria temp<=5
"""
#actividad 6
#el usuario debe ingresar un año y el programa dice si es bisiesto
anio = int(input("Ingresa un año: ")) #iba a poner ano pero era peor
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Se ingresó un año bisiesto")
else:
    print("Se ingresó un año no bisiesto")
"""
porque, aunque es divisible por 4, el calendario gregoriano estableció
 una excepción para los años divisibles por 100:
solo son bisiestos si también son divisibles por 400, fuentes google :D
y para validar si el año es positvo habria que validar que la variable sae mayor a 0
"""
#actividad 7
tex = input("ingrese una frase o palabra: ")
if not tex.endswith("."):
    tex += "."
print("Resultado:", tex)
"""
para frases que terminan en espacio, habria que eliminar ese espacio 
y otros caracteres a tomar en cuenta serian los de exclamacion, interrogacion o parentesis
"""
#actividad8
# Pide al usuario que cree una contraseña
contra = input("Crea una contraseña: ")
long_val = 8 <= len(contra) <= 20
tiene_mayuscula = any(caracter.isupper() for caracter in contra)
tiene_numero = any(caracter.isdigit() for caracter in contra)
if long_val and tiene_mayuscula and tiene_numero:
    print("¡Felicitaciones! Creaste tu contraseña.")
else:
    print("La contraseña no es segura.")
""""
para caracteres especiales, habria que darle el valor a una variable que tenga el valor
de todos los signos especiales y a este al momento de interpretar la contraseña
identificar si alguno de estos valores esta introducidos en la misma

La longitud maxima es importante para maximizar las seguridad y tambien
para evitar introducir una tan larga
"""
#actividad9
import re

contraseña = input("Crea una contraseña: ")

if len(contraseña) < 8:
    print("La contraseña no es segura. Debe tener al menos 8 caracteres.")
elif len(contraseña) > 20:
    print("La contraseña no es segura. Debe tener no más de 20 caracteres.")
elif not re.search(r"[A-Z]", contraseña):
    print("La contraseña no es segura. Debe tener al menos una mayúscula.")
elif not re.search(r"[0-9]", contraseña):
    print("La contraseña no es segura. Debe tener al menos un número.")
else:
    print("¡Felicitaciones! Creaste tu contraseña.")
"""
tal vez hacer una lista de errores y este cuando este vacia diga que la contraseña es segura
la ventaja es que el usario puede ver sus errores para no cometerlos
"""
#actividad10
jugador1 = input("Jugador 1, ingresa tu jugada (Piedra, Papel o Tijera): ")
jugador2 = input("Jugador 2, ingresa tu jugada (Piedra, Papel o Tijera): ")
if jugador1 == jugador2:
    print("EMPATE")
elif (jugador1 == "Piedra" and jugador2 == "Tijera") or \
     (jugador1 == "Papel" and jugador2 == "Piedra") or \
     (jugador1 == "Tijera" and jugador2 == "Papel"):
    print("GANA JUGADOR 1")
else:
    print("GANA JUGADOR 2")
""""
Convertir la entrada a minúsculas para evitar errores por mayúsculas y minúsculas
"""