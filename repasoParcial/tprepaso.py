'''
1 Consigna:
Un cine necesita un programa para administrar las funciones y la cantidad de butacas disponibles. Usar listas paralelas peliculas[] y butacas[].
El programa debe utilizar un menú con bucle while que permita al usuario elegir diferentes opciones hasta que decida salir.
Opciones del menú:
Agregar película:
El usuario ingresa el nombre de la película y la cantidad inicial de butacas.
Validar que el nombre no esté vacío ni repetido.
La cantidad de butacas debe ser un número entero mayor o igual a 0.
Consultar butacas disponibles de una película:
El usuario ingresa el nombre de una película.
El programa muestra cuántas butacas le quedan disponibles.
Si no existe, informar al usuario.
Ver cartelera completa:
Mostrar todas las películas con la cantidad de butacas disponibles.
Listar películas sin butacas:
Mostrar únicamente aquellas películas cuyo número de butacas sea 0.
Reservar / Cancelar butacas:
El usuario ingresa el nombre de una película.
Elegir si desea:
Reservar → resta 1 butaca (si hay disponibles).
Cancelar → suma 1 butaca (libera un lugar).
Si no hay butacas para reservar o la película no existe, mostrar mensaje de error.
Salir:
Terminar la ejecución del programa.
'''
#agrega comentarios explicando cada parte del codigo
Peliculas = []
Butacas = []
#Bucle principal del menú
while True:
    #Mostrar opciones del menú
    print("\nMenu del cine:")
    print("1. Agregar película")
    print("2. Consultar butacas disponibles")
    print("3. Ver cartelera completa")
    print("4. Listar películas sin butacas")
    print("5. Reservar / Cancelar butacas")
    print("6. Salir")
    opcion = input("Seleccione una opción (1-6): ")
    #Procesar la opción seleccionada con un if y seguidos de elif
    if opcion == '1':
        pelicula = input("Ingrese el nombre de la película: ")
        if pelicula in Peliculas:
            print("La película ya está en la cartelera.")
            continue
        cantidad = int(input("Ingrese la cantidad inicial de butacas: "))
        if cantidad < 0:
            print("La cantidad de butacas debe ser un número entero mayor o igual a 0.")
            continue
        #una vez continuada la validacion, se agrega la pelicula y la cantidad de butacas a las listas
        Peliculas.append(pelicula)
        Butacas.append(cantidad)
        print(f"Película '{pelicula}' con {cantidad} butacas agregada.")
        #se agrega un mensaje de confirmacion de que la pelicula fue agregada 
        #y se vuelve al menu principal
        #opcion 2 en donde nos permite consultar las butacas disponibles de una pelicula y mostrarla en pantalla
    elif opcion == '2':
        pelicula = input("Ingrese el nombre de la película: ")
        if pelicula in Peliculas:
            index = Peliculas.index(pelicula)
            print(f"La película '{pelicula}' tiene {Butacas[index]} butacas disponibles.")
        else:
            print("La película no existe en la cartelera.")
    elif opcion == '3':
        #La pelicula y la cantidad de butacas se muestran en pantalla
        print("\nCartelera completa:")
        for i in range(len(Peliculas)):
            print("Nombre de la película y butacas disponibles:")
            print(f"{Peliculas[i]}: | {Butacas[i]} ")
    elif opcion == '4':
        print("\nPeliculas sin butacas:")
        sin_butacas = False
        for i in range(len(Peliculas)):
            if Butacas[i] == 0:
                print(Peliculas[i])
                sin_butacas = True
        if not sin_butacas:
            print("No hay películas sin butacas disponibles.")
            #opcion 5 en donde nos permite reservar o cancelar una butaca de una pelicula
    elif opcion == '5':
        pelicula = input("Ingrese el nombre de la película: ")
        if pelicula in Peliculas:
            index = Peliculas.index(pelicula)
            accion = input("¿Desea reservar (r) o cancelar (c) una butaca? (r/c): ").lower()
            if accion == 'r':
                if Butacas[index] > 0:
                    Butacas[index] -= 1
                    print(f"Butaca reservada para '{pelicula}'. Quedan {Butacas[index]} butacas.")
                else:
                    print("No hay butacas disponibles para reservar.")
            elif accion == 'c':
                Butacas[index] += 1
                print(f"Butaca cancelada para '{pelicula}'. Ahora hay {Butacas[index]} butacas disponibles.")
            else:
                print("Acción no válida. Por favor, ingrese 'r' para reservar o 'c' para cancelar.")
        else:
            print("La película no existe en la cartelera.")
    elif opcion == '6':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

'''
3. Consigna:
Un estacionamiento administra sus cocheras numeradas y si están libres u ocupadas.
Usar dos listas paralelas:
cocheras[] → números de cochera.
estados[] → 0 = libre, 1 = ocupada.
Menú:
Agregar cochera.
Consultar estado de una cochera.
Ver estado general.
Listar libres.
Ocupar / Liberar cochera.
Salir.
Consigna:
'''

cocheras = []  # lista para los números de cochera
estados = []   # lista para los estados: 0 = libre, 1 = ocupada

while True:
    print("\nMenú del estacionamiento:")
    print("1. Agregar cochera")
    print("2. Consultar estado de una cochera")
    print("3. Ver estado general")
    print("4. Listar cocheras libres")
    print("5. Ocupar / Liberar cochera")
    print("6. Salir")
    opcion = input("Seleccione una opción (1-6): ")

    # Opción 1: Agregar una nueva cochera
    if opcion == '1':
        numero = int(input("Ingrese el número de la cochera: "))
        if numero in cocheras:
            print("La cochera ya existe.")
            continue
        cocheras.append(numero)
        estados.append(0)
        print(f"Cochera {numero} agregada y está libre.")
        # (Nota: este print de abajo parece un mensaje de error que quedó de más)
        print("Por favor, ingrese un número válido para la cochera.")
    
    # Opción 2: Consultar el estado (libre/ocupada) de una cochera puntual
    elif opcion == '2':
        try:
            numero = int(input("Ingrese el número de la cochera a consultar: "))
            if numero in cocheras:
                index = cocheras.index(numero)
                estado = "Libre" if estados[index] == 0 else "Ocupada"
                print(f"La cochera {numero} está {estado}.")
            else:
                print("La cochera no existe.")
        except ValueError:
            # Si el usuario no escribe un número válido, muestra este mensaje
            print("Por favor, ingrese un número válido para la cochera.")
    
    # Opción 3: Ver el estado de todas las cocheras registradas
    elif opcion == '3':
        print("\nEstado general de las cocheras:")
        for i in range(len(cocheras)):
            estado = "Libre" if estados[i] == 0 else "Ocupada"
            print(f"Cochera {cocheras[i]}: {estado}")
    
    # Opción 4: Listar solamente las cocheras que están libres
    elif opcion == '4':
        print("\nCocheras libres:")
        libres = False
        for i in range(len(cocheras)):
            if estados[i] == 0:
                print(f"Cochera {cocheras[i]}")
                libres = True
        if not libres:
            print("No hay cocheras libres.")
    
    # Opción 5: Cambiar el estado de una cochera (ocupar o liberar)
    elif opcion == '5':
        numero = int(input("Ingrese el número de la cochera a ocupar/liberar: "))
        if numero in cocheras:
            index = cocheras.index(numero)
            accion = input("¿Desea ocupar (o) o liberar (l) la cochera? (o/l): ").lower()
            if accion == 'o':
                if estados[index] == 0:
                    estados[index] = 1
                    print(f"Cochera {numero} ahora está ocupada.")
                else:
                    print("La cochera ya está ocupada.")
            elif accion == 'l':
                if estados[index] == 1:
                    estados[index] = 0
                    print(f"Cochera {numero} ahora está libre.")
                else:
                    print("La cochera ya está libre.")
            else:
                print("Acción no válida. Por favor, ingrese 'o' para ocupar o 'l' para liberar.")
        else:
            print("La cochera no existe.")
        # (Nota: este print también parece estar fuera de lugar)
        print("Por favor, ingrese un número válido para la cochera.")

    # Opción 6: Salir del programa
    elif opcion == '6':
        print("Saliendo... ¡Gracias por usar el sistema!")
        break  # corta el bucle while y termina el programa

    # Si el usuario escribe algo distinto a 1-6
    else:
        print("Opción inválida. Por favor, elija un número del 1 al 6.")

'''
5. Consigna:
Una concesionaria necesita un programa en Python para gestionar los autos disponibles para la venta.
Debe usar dos listas paralelas:
autos[] → nombres o modelos de autos.
unidades[] → cantidad de unidades disponibles de cada modelo.
Cada auto en autos[i] corresponde a las unidades en unidades[i].
El programa debe utilizar un menú con bucle while que permita al usuario elegir diferentes opciones hasta salir.
Opciones del menú:
Agregar auto:
El usuario ingresa el modelo y la cantidad inicial de unidades.
Validar que el modelo no esté vacío ni repetido.
Las unidades deben ser un número entero mayor o igual a 0.
Consultar unidades de un modelo:
El usuario ingresa el modelo de auto.
Mostrar cuántas unidades quedan.
Si no existe, mostrar un mensaje de error.
Ver inventario completo:
Mostrar todos los modelos y la cantidad de unidades disponibles.
Listar autos sin stock:
Mostrar únicamente los modelos con unidades = 0.
Vender / Reponer unidades:
El usuario elige un modelo.
Puede:
Vender → resta 1 unidad (si hay disponibles).
Reponer → suma 1 unidad.
Si no hay stock suficiente o el modelo no existe, mostrar error.
Salir:
Terminar el programa.
'''

autos = []
unidades = []

while True:
    print("\nMenú de la concesionaria:")
    print("1. Agregar auto")
    print("2. Consultar unidades de un modelo")
    print("3. Ver inventario completo")
    print("4. Listar autos sin stock")
    print("5. Vender / Reponer unidades")
    print("6. Salir")
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == '1':
        modelo = input("Ingrese el modelo del auto: ")
        if modelo in autos:
            print("El modelo ya está en el inventario.")
            continue
        try:
            cantidad = int(input("Ingrese la cantidad inicial de unidades: "))
            if cantidad < 0:
                print("La cantidad debe ser un número entero mayor o igual a 0.")
                continue
            autos.append(modelo)
            unidades.append(cantidad)
            print(f"Modelo '{modelo}' con {cantidad} unidades agregado.")
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")

    elif opcion == '2':
        modelo = input("Ingrese el modelo del auto: ")
        if modelo in autos:
            index = autos.index(modelo)
            print(f"El modelo '{modelo}' tiene {unidades[index]} unidades disponibles.")
        else:
            print("El modelo no existe en el inventario.")

    elif opcion == '3':
        print("\nInventario completo:")
        for i in range(len(autos)):
            print(f"{autos[i]}: {unidades[i]} unidades")

    elif opcion == '4':
        print("\nAutos sin stock:")
        sin_stock = False
        for i in range(len(autos)):
            if unidades[i] == 0:
                print(autos[i])
                sin_stock = True
        if not sin_stock:
            print("No hay autos sin stock.")

    elif opcion == '5':
        modelo = input("Ingrese el modelo del auto: ")
        if modelo in autos:
            index = autos.index(modelo)
            accion = input("¿Desea vender (v) o reponer (r) una unidad? (v/r): ").lower()
            if accion == 'v':
                if unidades[index] > 0:
                    unidades[index] -= 1
                    print(f"Unidad vendida de '{modelo}'. Quedan {unidades[index]} unidades.")
                else:
                    print("No hay unidades disponibles para vender.")
            elif accion == 'r':
                unidades[index] += 1
                print(f"Unidad repuesta de '{modelo}'. Ahora hay {unidades[index]} unidades disponibles.")
            else:
                print("Acción no válida. Por favor, ingrese 'v' para vender o 'r' para reponer.")
        else:
            print("El modelo no existe en el inventario.")
    elif opcion == '6':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

