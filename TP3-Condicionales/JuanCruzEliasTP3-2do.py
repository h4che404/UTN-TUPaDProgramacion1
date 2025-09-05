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
# Si el usuario ingresa la contraseña con mayúsculas, el programa la considerará incorrecta, ya que la comparación es sensible a mayúsculas y minúsculas.
# Para mejorar el programa y permitir más intentos, se podría usar un bucle que permita al usuario intentar ingresar la contraseña varias veces hasta que sea correcta o se agoten los intentos permit
contrasena_correcta = "juan1"
contrasena_usuario = input("Introduce la contraseña: ").lower()
if contrasena_usuario == contrasena_correcta:
    print("Contraseña correcta. Bienvenido.")
else:
    print("Contraseña incorrecta. Intenta de nuevo.")
    if contrasena_usuario == contrasena_correcta:
        print("Contraseña correcta. Bienvenido.")
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")
        if contrasena_usuario == contrasena_correcta:
            print("Contraseña correcta. Bienvenido.")
        else:
            print("Contraseña incorrecta. Intenta de nuevo.")


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
# Para manejar vocales acentuadas, incluiría las vocales acentuadas en la cadena de comparación.
# Para simplificar las comparaciones, usaría la palabra clave 'in' para verificar si la letra ingresada está en una cadena que contiene todas las vocales posibles.
vocal = str(input("Ingrese una letra: "))

if vocal in "aeiouAEIOUáéíóúÁÉÍÓÚ":
    print("La letra ingresada es una vocal")
else:
    print("La letra ingresada no es una vocal")

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
# Si el usuario ingresa un texto, el programa lanzará un error al intentar convertirlo a entero.
# Para adaptar el código a números decimales, cambiaría la conversión de int() a float().
num = float(input("Ingrese un numero: "))
if num > 0:
    print("El numero es positivo")
elif num < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")


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
# Para comparar más de dos números, agregaría más variables y pediría más números al usuario.
# Si se ingresan valores no numéricos, el programa lanzará un error al intentar convertirlos a enteros.
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > num2:
    print("El primer numero ingresado es mayor")
elif num1 < num2:
    print("El primer numero ingresado es menor")
else:
    print("Los numeros ingresados son iguales")

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
# Para adaptar el programa a °F, usaría la fórmula de conversión (°C * 9/5) + 32 para convertir la temperatura ingresada a °C antes de hacer las comparaciones.
temp = float(input("Ingrese la temperatura actual en °C: "))
if temp <= 10:
    print("Hace frio")
elif 10 < temp <= 25:
    print("Esta templado")
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
# El año 1900 no es bisiesto porque es divisible por 100 pero no por 400.
# Para validar que el año sea positivo, comprobaría que el año ingresado sea mayor a 0.
año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Se ingresó un año bisiesto")
else:
    print("Se ingresó un año no bisiesto")

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
# Para manejar frases que terminan con espacios, crearía una varible espacio = " " y la comprobaría igual que con el punto. usando palabra [-1] eliminaría ese espacio ya agregaría un punto
# Otros caracteres de puntuación que podría considerar son el punto y coma, la coma, el doble punto.
palabra = str(input("Ingrese una frase o palabra: "))
if palabra[-1] != ".":
    palabra = palabra + "."
print(palabra)

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
# Para añadir la regla de usar un carácter especial, usaría varios if simples para verificar si la contraseña contiene algún carácter especial permitido. 
# Es importante limitar la longitud máxima por facilidad para recordar, una mejor seguridad y para no sobrecargar el sistema.
contraseña = str(input("Cree una contraseña: "))
tiene_mayuscula = False
tiene_numero = False
if len(contraseña) >= 8 and len(contraseña) <= 20:
    for char in contraseña:
        if char.isupper():
            tiene_mayuscula = True
        if char.isdigit():
            tiene_numero = True
    if tiene_mayuscula and tiene_numero:
        print("¡Felicitaciones! Creaste tu contraseña.")
    else:
        print("La contraseña no es segura.")
else:
    print("La contraseña no es segura.")


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
# Para evitar repetir código al verificar cada condición, usaría bien el if y escribiría cada verificación solo una vez.
# Las ventajas de este enfoque para el usuario son que recibe mensajes claros y específicos que le dicen exactamente qué corregir, le permite corregir todos los errores de una vez sin tener que intentar varias veces, hace que el programa sea más fácil de usar y entender, y es una mejor experiencia en general porque el usuario no se frustra.
contraseña = str(input("Cree una contraseña: "))
tiene_mayuscula = False
tiene_numero = False
if len(contraseña) < 8:
    print("La contraseña no es segura. Debe tener al menos 8 caracteres.")
elif len(contraseña) > 20:
    print("La contraseña no es segura. No debe tener más de 20 caracteres.")
else:
    for char in contraseña:
        if char.isupper():
            tiene_mayuscula = True
        if char.isdigit():
            tiene_numero = True
    if not tiene_mayuscula:
        print("La contraseña no es segura. Debe tener al menos una mayúscula.")
    if not tiene_numero:
        print("La contraseña no es segura. Debe tener al menos un número.")
    if tiene_mayuscula and tiene_numero:
        print("¡Felicitaciones! Creaste tu contraseña.")


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

# Para manejar entradas inválidas, usaría un conjunto de opciones válidas y comprobaría si la entrada del usuario está en ese conjunto. Si no lo está, pediría al usuario que ingrese una opción válida.
# Para simplificar las comparaciones, usaría un diccionario que mapee cada jugada a las jugadas que derrota, y luego compararía las jugadas de los jugadores usando ese diccionario.
jugador1 = str(input("Jugador 1, ingrese su jugada (piedra, papel o tijera): ")).lower()
jugador2 = str(input("Jugador 2, ingrese su jugada (piedra, papel o tijera): ")).lower()
