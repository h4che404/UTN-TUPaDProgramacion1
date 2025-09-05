"""
 Programación I
 Trabajo práctico - estructuras condicionales 
"""

"""
Ejercicio 1: Validación de contraseña
 Objetivo: Analizar un programa existente que verifica una contraseña.
 Instrucciones:
1. Lee el siguiente código y explica qué hace:
contrasena_correcta = "programacion1"
contrasena_usuario = input("Introduce la contraseña: ")
if contrasena_usuario == contrasena_correcta:
 print("Contraseña correcta. Bienvenido.")
else:
 print("Contraseña incorrecta. Intenta de nuevo.")
 Preguntas de reflexión:
• ¿Qué pasa si el usuario ingresa la contraseña con mayúsculas?
• ¿Cómo mejorarías el programa para dar más intentos?
"""
contraseña_correcta = "programación1"
contraseña_ususario = input("Introduce la contraseña: ")
if contraseña_ususario == contraseña_correcta:
    print("Contraseña correcta. bienvenido. ")
else: 
    print("Contraseña incorrecta. Intenta de nuevo. ")

"""
 - el codigo solicicta al usuario que ingrese una contraseña.
 - verifica si la contraseña ingresada por el usuario conincide con la que esta guardada en la variable contraseña_correcta
 - si es correcta, muestra por consola un mensaje "Contraseña correcta. Bienvenido. "
 - si es incorrecta, muestra por consola un mensaje "Contraseña incorrecta. Intenta de nuevo."


• ¿Qué pasa si el usuario ingresa la contraseña con mayúsculas?
probablemente salte error porque no estan guardada con mayúscula la contraseña

• ¿Cómo mejorarías el programa para dar más intentos?
usaría una estructura mientras. 
"""
contraseña_correcta = "programación1"
contraseña_ususario = input("Introduce la contraseña: ")
if contraseña_ususario == contraseña_correcta:
    print("Contraseña correcta. bienvenido. ")
else: 
    print("Contraseña incorrecta. Intenta de nuevo. ")
    contraseña_ususario = input("Introduce la contraseña: ")
    if contraseña_ususario == contraseña_correcta:
        print("Contraseña correcta. bienvenido. ")
    else: 
        print("Contraseña incorrecta. Intenta de nuevo. ")
        contraseña_ususario = input("Introduce la contraseña: ")
        if contraseña_ususario == contraseña_correcta:
             print("Contraseña correcta. bienvenido. ")
        else:
            print("Contraseña incorrecta. Intenta de nuevo. ")
            contraseña_ususario = input("Introduce la contraseña: ")
            if contraseña_ususario == contraseña_correcta:
                print("Contraseña correcta. bienvenido. ")
            else:
                print("Contraseña incorrecta. No quedan más intentos. Se procederá a bloquaer el dispositivo")


"""
Ejercicio 2: Identificador de vocales
 Objetivo: Clasificar caracteres usando condicionales.
 Instrucciones:
1. Solicita una letra al usuario.
2. Si es una vocal (a, e, i, o, u, en mayúscula o minúscula), imprime: "La letra
ingresada es una vocal".
3. En otro caso, imprime: "La letra ingresada no es una vocal".
 Preguntas de reflexión:
• ¿Cómo manejarías vocales acentuadas (á, é)?
• ¿Qué estructura usarías para simplificar las comparaciones?
"""
letra = input("Ingrese un letra: ")

vocal = "aeiouAEIOU"

if letra in vocal:
    print("La letra ingresada es una vocal")
else: 
    print("La letra ingresada no es una vocal. ")

"""
¿Como manejarías vocales acentuadas (á,é)?
La mejor manera que encuentro es agregarlas en la variable vocal = "aeiouAEIOUáéíóúÁÉÍÓÚ"
¿Qué estructura usarias para simplificar las comparaciones?
más simple que lo que hice no se si es posible, pero podría usar un while o arrays
"""
"""
 Ejercicio 3: Clasificador de números
 Objetivo: Determinar el signo de un número.
 Instrucciones:
1. Pide un número al usuario.
2. Si es positivo, imprime: "El número es positivo".
3. Si es negativo, imprime: "El número es negativo".
4. Si es cero, imprime: "El número es cero".
 Preguntas de reflexión:
• ¿Qué ocurre si el usuario ingresa un texto?
• ¿Cómo adaptarías el código para números decimales?
"""
num = int(input("Ingrese un número sea positivo o negrativo"))

if num == 0:
    print("El número es cero")
elif num > 0:
    print("El núemro es prositivo")
else:
    print("El número es negrativo") 


"""
• ¿Qué ocurre si el usuario ingresa un texto?
Saltara error porque no seria posible convertirlo a integer 
• ¿Cómo adaptarías el código para números decimales?
solo haria la conversión a flotante en ves de a integer
"""

"""
 Ejercicio 4: Comparador de números
 Objetivo: Comparar dos números con condicionales.
 Instrucciones:
1. Solicita dos números al usuario.
2. Si el primero es mayor, imprime: "El primer número ingresado es mayor".
3. Si el primero es menor, imprime: "El primer número ingresado es menor".
4. Si son iguales, imprime: "Los números ingresados son iguales".
 Preguntas de reflexión:
• ¿Cómo modificarías el programa para comparar más de dos números?
• ¿Qué pasa si se ingresan valores no numéricos?
"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"El primer número ingresado es mayor.")
elif num1 == num2:
    print("Los números ingresados son iguales.")
else: 
    print("El primer número ingresado es menor")

"""
• ¿Cómo modificarías el programa para comparar más de dos números?
agreagaría variables, lo que pediría más números al usuario
• ¿Qué pasa si se ingresan valores no numéricos?
salta error
"""

"""
Ejercicio 5: Clima según temperatura
 Objetivo: Clasificar temperaturas en rangos.
 Instrucciones:
1. Pide la temperatura actual en °C.
2. Si es ≤ 10°C, imprime: "Hace frío".
3. Si está entre 10°C y 25°C, imprime: "Está templado".
4. Si es > 25°C, imprime: "Hace calor".
 Preguntas de reflexión:
• ¿Cómo adaptarías el programa para usar °F?
• ¿Qué considerarías para añadir más rangos (ej: "Hace mucho frío")?
"""
temp = float(input("Ingrese la temperatura actual en celsius: "))

if temp <= 10:
    print("Hace frío")
elif temp > 10 and temp < 25:
    print("Está templado")
else:
    print("Hace calor")

"""
• ¿Cómo adaptarías el programa para usar °F?
Tendría que preguntarle al ususario si usa farenheit o celsius o hacer conversiones
"""

tipo = int(input("Ingrese 1 o 2: \n 1- Celsius (°C) \n 2- Farenheit (°F)"))

if tipo == 1:
    temp = float(input("Ingrese la temperatura actual en celsius: "))
    if temp <= 10:
        print("Hace frío")
    elif temp > 10 and temp < 25:
        print("Está templado")
    else:
        print("Hace calor")
else:
    temp = float(input("Ingrese la temperatura actual en Farenheit: "))
    temp = ((temp-32)*5/9)
    
    if temp <= 10:
        print("Hace frío")
    elif temp > 10 and temp < 25:
        print("Está templado")
    else:
        print("Hace calor")

"""
• ¿Qué considerarías para añadir más rangos (ej: "Hace mucho frío")?
"""

tipo = int(input("Ingrese 1 o 2: \n 1- Celsius (°C) \n 2- Farenheit (°F)"))

if tipo == 1:
    temp = float(input("Ingrese la temperatura actual en celsius: "))
    if temp < 0:
        print("Hace mucho frío")
    elif temp > 0 and temp <10:
        print("Hace frío")
    elif temp > 10 and temp < 25:
        print("Está templado")
    else:
        print("Hace calor")
else:
    temp = float(input("Ingrese la temperatura actual en Farenheit: "))
    temp = ((temp-32)*5/9)
    
    if temp <= 10:
        print("Hace frío")
    elif temp > 10 and temp < 25:
        print("Está templado")
    else:
        print("Hace calor")


"""
 Ejercicio 6: Detector de años bisiestos
 Objetivo: Aplicar condiciones compuestas.
 Instrucciones:
1. Pide un año al usuario.
2. Si es divisible por 4 pero no por 100, o divisible por 400, imprime: "Se
ingresó un año bisiesto".
3. En otro caso, imprime: "Se ingresó un año no bisiesto".
 Preguntas de reflexión:
• ¿Por qué el año 1900 no es bisiesto?
• ¿Cómo validarías que el año sea positivo?
"""

año = int(input("Ingrese un año"))

if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print("Se ingresó un año bisiesto.")
else:
    print("Se ingresó un año no bisiesto. ")

"""
• ¿Por qué el año 1900 no es bisiesto?
porque es divisible por 100
• ¿Cómo validarías que el año sea positivo?
comprobaría que el año ingresado sea mayor a 0
"""

"""
 Ejercicio 7: Ajustador de frases
 Objetivo: Manipular strings con condicionales.
 Instrucciones:
1. Pide una frase o palabra al usuario.
2. Si no termina en punto, añádelo al final.
3. Imprime el resultado.
 Preguntas de reflexión:
• ¿Cómo manejarías frases que terminan con espacios?
• ¿Qué otros caracteres de puntuación podrías considerar?
"""

palabra = input("Ingrese una palabra o frase")
punto = "."

if palabra in punto:
    print(palabra, ".")

"""
• ¿Cómo manejarías frases que terminan con espacios?
crearía una varible espacio = " " y la comprobaría igual que con el punto. usando palabra [-1] eliminaría ese espacio ya agregaría un punto
• ¿Qué otros caracteres de puntuación podrías considerar?
puntop y coma, la coma, el doble punto.
"""

"""
 Ejercicio 8: Validador de contraseña segura
 Objetivo: Implementar múltiples condiciones.
 Instrucciones:
1. Pide al usuario que cree una contraseña.
2. Verifica que cumpla:
o 8+ caracteres y ≤20 caracteres.
o Al menos 1 mayúscula (usa .isupper()).
o Al menos 1 número (usa .isdigit()).
3. Si es segura, imprime: "¡Felicitaciones! Creaste tu contraseña.".
4. Si no, imprime: "La contraseña no es segura.".
 Preguntas de reflexión:
• ¿Cómo añadirías la regla de usar un carácter especial?
• ¿Por qué es importante limitar la longitud máxima?
"""
contraseña = input("Crea una contraseña: ")

es_segura = True

if len(contraseña) < 8:
    es_segura = False

if len(contraseña) > 20:
    es_segura = False

tiene_mayuscula = False
if len(contraseña) > 0 and contraseña[0].isupper():
    tiene_mayuscula = True
if len(contraseña) > 1 and contraseña[1].isupper():
    tiene_mayuscula = True
if len(contraseña) > 2 and contraseña[2].isupper():
    tiene_mayuscula = True
if len(contraseña) > 3 and contraseña[3].isupper():
    tiene_mayuscula = True
if len(contraseña) > 4 and contraseña[4].isupper():
    tiene_mayuscula = True
if len(contraseña) > 5 and contraseña[5].isupper():
    tiene_mayuscula = True
if len(contraseña) > 6 and contraseña[6].isupper():
    tiene_mayuscula = True
if len(contraseña) > 7 and contraseña[7].isupper():
    tiene_mayuscula = True

if not tiene_mayuscula:
    es_segura = False

tiene_numero = False
if len(contraseña) > 0 and contraseña[0].isdigit():
    tiene_numero = True
if len(contraseña) > 1 and contraseña[1].isdigit():
    tiene_numero = True
if len(contraseña) > 2 and contraseña[2].isdigit():
    tiene_numero = True
if len(contraseña) > 3 and contraseña[3].isdigit():
    tiene_numero = True
if len(contraseña) > 4 and contraseña[4].isdigit():
    tiene_numero = True
if len(contraseña) > 5 and contraseña[5].isdigit():
    tiene_numero = True
if len(contraseña) > 6 and contraseña[6].isdigit():
    tiene_numero = True
if len(contraseña) > 7 and contraseña[7].isdigit():
    tiene_numero = True

if not tiene_numero:
    es_segura = False

if es_segura:
    print("¡Felicitaciones! Creaste tu contraseña.")
else:
    print("La contraseña no es segura.")

"""
• ¿Cómo añadirías la regla de usar un carácter especial?
usaría varios if simples para verificar si la contraseña contiene algún carácter especial permitido. 
Por ejemplo, verificar si contiene "!", "@", "#" u otros:

tiene_especial = False

if "!" in contraseña:
    tiene_especial = True
if "@" in contraseña:
    tiene_especial = True
if "#" in contraseña:
    tiene_especial = True


• ¿Por qué es importante limitar la longitud máxima?
1- facilidad para recordar, al ser corta el usuario no la olvida
2- una mejor seguridad lo que garantiza mantener el cotrol de ella
3- no sobrecarga el sistema
"""

"""
Ejercicio 9: Mejorando mensajes de error
 Objetivo: Dar retroalimentación específica al usuario.
 Instrucciones:
1. Basado en el Ejercicio 8, mejora los mensajes de error:
o Si tiene <8 caracteres: "La contraseña no es segura. Debe tener al
menos 8 caracteres.".
o Si tiene >20 caracteres: "...no más de 20 caracteres.".
o Si falta mayúscula: "...al menos una mayúscula.".
o Si falta número: "...al menos un número.".
 Preguntas de reflexión:
• ¿Cómo evitarías repetir código al verificar cada condición?
• ¿Qué ventajas tiene este enfoque para el usuario?
"""
contraseña = input("Crea una contraseña: ")

es_segura = True

if len(contraseña) < 8:
    print("La contraseña no es segura. Debe tener al menos 8 caracteres.")
    es_segura = False

if len(contraseña) > 20:
    print("La contraseña no es segura. No debe tener más de 20 caracteres.")
    es_segura = False

tiene_mayuscula = False
if len(contraseña) > 0 and contraseña[0].isupper():
    tiene_mayuscula = True
if len(contraseña) > 1 and contraseña[1].isupper():
    tiene_mayuscula = True
if len(contraseña) > 2 and contraseña[2].isupper():
    tiene_mayuscula = True
if len(contraseña) > 3 and contraseña[3].isupper():
    tiene_mayuscula = True
if len(contraseña) > 4 and contraseña[4].isupper():
    tiene_mayuscula = True
if len(contraseña) > 5 and contraseña[5].isupper():
    tiene_mayuscula = True
if len(contraseña) > 6 and contraseña[6].isupper():
    tiene_mayuscula = True
if len(contraseña) > 7 and contraseña[7].isupper():
    tiene_mayuscula = True

if not tiene_mayuscula:
    print("La contraseña no es segura. Debe contener al menos una mayúscula.")
    es_segura = False

tiene_numero = False
if len(contraseña) > 0 and contraseña[0].isdigit():
    tiene_numero = True
if len(contraseña) > 1 and contraseña[1].isdigit():
    tiene_numero = True
if len(contraseña) > 2 and contraseña[2].isdigit():
    tiene_numero = True
if len(contraseña) > 3 and contraseña[3].isdigit():
    tiene_numero = True
if len(contraseña) > 4 and contraseña[4].isdigit():
    tiene_numero = True
if len(contraseña) > 5 and contraseña[5].isdigit():
    tiene_numero = True
if len(contraseña) > 6 and contraseña[6].isdigit():
    tiene_numero = True
if len(contraseña) > 7 and contraseña[7].isdigit():
    tiene_numero = True

if not tiene_numero:
    print("La contraseña no es segura. Debe contener al menos un número.")
    es_segura = False

if es_segura:
    print("¡Felicitaciones! Creaste tu contraseña.")

"""
• ¿Cómo evitarías repetir código al verificar cada condición?
usar bien el if y escribir cada verificación solo una vez

if len(contraseña) < 8:
    print("Debe tener al menos 8 caracteres.")

• ¿Qué ventajas tiene este enfoque para el usuario?
- El usuario recibe mensajes claros y específicos que le dicen exactamente qué corregir.
- Le permite corregir todos los errores de una vez, sin tener que intentar varias veces.
- Hace que el programa sea más fácil de usar y entender.
- Es una mejor experiencia en general, porque el usuario no se frustra.
"""


"""
 Ejercicio 10: Piedra, papel o tijera
 Objetivo: Implementar lógica de juego con condicionales anidados.
 Instrucciones:
1. Pide al usuario las jugadas del Jugador 1 y Jugador 2 (piedra, papel o tijera).
2. Usa la tabla proporcionada para determinar el resultado (ganador o
empate).
Resultado Jugador 1 Jugador 2
EMPATE Piedra Piedra
GANA JUGADOR 2 Piedra Papel
GANA JUGADOR 1 Piedra Tijera
GANA JUGADOR 1 Papel Piedra
EMPATE Papel Papel
GANA JUGADOR 2 Papel Tijera
GANA JUGADOR 2 Tijera Piedra
GANA JUGADOR 1 Tijera Papel
EMPATE Tijera Tijera
3. Imprime: "GANA JUGADOR 1", "GANA JUGADOR 2" o "EMPATE".
 Preguntas de reflexión:
• ¿Cómo manejarías entradas inválidas (ej: "piedra" mal escrito)?
• ¿Qué estructura usarías para simplificar las comparaciones?
 Bonus:
• Diagrama de flujo: Dibuja el diagrama de flujo del Ejercicio 10.
"""
jugador1 = input("Jugador 1 elige (piedra, papel o tijera): ")
jugador2 = input("Jugador 2 elige (piedra, papel o tijera): ")

if jugador1 == "piedra" and jugador2 == "piedra":
    print("EMPATE")

if jugador1 == "piedra" and jugador2 == "papel":
    print("GANA JUGADOR 2")

if jugador1 == "piedra" and jugador2 == "tijera":
    print("GANA JUGADOR 1")

if jugador1 == "papel" and jugador2 == "piedra":
    print("GANA JUGADOR 1")

if jugador1 == "papel" and jugador2 == "papel":
    print("EMPATE")

if jugador1 == "papel" and jugador2 == "tijera":
    print("GANA JUGADOR 2")

if jugador1 == "tijera" and jugador2 == "piedra":
    print("GANA JUGADOR 2")

if jugador1 == "tijera" and jugador2 == "papel":
    print("GANA JUGADOR 1")

if jugador1 == "tijera" and jugador2 == "tijera":
    print("EMPATE")


"""
• ¿Cómo manejarías entradas inválidas (ej: "piedra" mal escrito)?

if jugador1 != "piedra" and jugador1 != "papel" and jugador1 != "tijera":
    print("Jugador 1 ingresó una opción inválida.")

if jugador2 != "piedra" and jugador2 != "papel" and jugador2 != "tijera":
    print("Jugador 2 ingresó una opción inválida.")

• ¿Qué estructura usarías para simplificar las comparaciones?

pienso que de por si es lo más simple que se me ocurió

 Bonus:
• Diagrama de flujo: Dibuja el diagrama de flujo del Ejercicio 10.

┌────────────────────────────┐
│      INICIO DEL JUEGO      │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│Leer jugada del Jugador 1   │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│Leer jugada del Jugador 2   │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│¿Jugadas válidas?           │
│(piedra, papel o tijera)    │
└───────┬───────────┬────────┘
        │           │
   [NO] ▼           ▼ [SÍ]
┌─────────────┐  ┌────────────────────────┐
│Mostrar error│  │¿Jugador 1 == Jugador 2?│
│"Entrada inválida"                     │
└────┬────────┘  └──────────┬─────────────┘
     │                     │
     ▼                     ▼
 ┌──────────────┐     ┌────────────────────────────┐
 │   FIN DEL    │     │  Mostrar "EMPATE"          │
 │   JUEGO      │     └────────────┬───────────────┘
 └──────────────┘                  │
                                   ▼
                        ┌────────────────────────────┐
                        │¿Jugador 1 gana?            │
                        │(según reglas del juego)    │
                        └──────┬──────────────┬──────┘
                               │              │
                            [SÍ]            [NO]
                               ▼              ▼
              ┌────────────────────────┐ ┌───────────────────────┐
              │Mostrar "GANA JUGADOR 1"│ │Mostrar "GANA JUGADOR 2"│
              └─────────────┬──────────┘ └────────────┬──────────┘
                            ▼                         ▼
                     ┌──────────────┐          ┌──────────────┐
                     │   FIN DEL    │          │   FIN DEL    │
                     │   JUEGO      │          │   JUEGO      │
                     └──────────────┘          └──────────────┘

"""