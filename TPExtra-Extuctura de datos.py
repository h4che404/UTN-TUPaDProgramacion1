"""
PUNTO 1 - Manejo de notas.txt
Crear un archivo llamado “notas.txt” con tres líneas con el nombre de un alumno y su nota, separados por una coma.
Luego mostrar su contenido, formatearlo, permitir agregar más alumnos, y reescribir el archivo desde cero.
"""

def crear_notas():
    with open("notas.txt", "w") as archivo:
        archivo.write("Sofia,9\n")
        archivo.write("Marcos,7\n")
        archivo.write("Ana,10\n")
    print("Archivo 'notas.txt' creado correctamente.")

def leer_notas():
    try:
        with open("notas.txt", "r") as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("El archivo 'notas.txt' no existe. Créelo primero.")

def mostrar_notas_formato():
    try:
        with open("notas.txt", "r") as archivo:
            for linea in archivo:
                nombre, nota = linea.strip().split(",")
                print(f"Alumno: {nombre} | Nota: {nota}")
    except FileNotFoundError:
        print("El archivo 'notas.txt' no existe. Créelo primero.")

def agregar_notas():
    try:
        with open("notas.txt", "a") as archivo:
            while True:
                nombre = input("Ingrese nombre del alumno (o 'n' para salir): ")
                if nombre.lower() == "n":
                    break
                nota = input("Ingrese la nota: ")
                archivo.write(f"{nombre},{nota}\n")
        print("Alumnos agregados correctamente.")
    except FileNotFoundError:
        print("El archivo 'notas.txt' no existe. Créelo primero.")

def reescribir_notas():
    with open("notas.txt", "w") as archivo:
        archivo.write("Lucas,8\n")
        archivo.write("Micaela,10\n")
        archivo.write("Tomas,6\n")
    print("El contenido anterior fue reemplazado.")



"""
PUNTO 2 - Heladería
Crear el archivo heladeria.csv, mostrar su contenido, y permitir agregar sabores.
"""

def crear_heladeria():
    with open("heladeria.csv", "w") as archivo:
        archivo.write("Chocolate,1200,si\n")
        archivo.write("Vainilla,1100,si\n")
        archivo.write("Frutilla,1150,no\n")
    print("Archivo 'heladeria.csv' creado correctamente.")

def mostrar_heladeria():
    try:
        with open("heladeria.csv", "r") as archivo:
            for linea in archivo:
                sabor, precio, disponible = linea.strip().split(",")
                print(f"Sabor: {sabor} | Precio: ${precio} | Disponible: {disponible}")
    except FileNotFoundError:
        print("El archivo 'heladeria.csv' no existe. Créelo primero.")

def agregar_sabor():
    with open("heladeria.csv", "a") as archivo:
        sabor = input("Ingrese el sabor: ")
        precio = input("Ingrese el precio: ")
        disponible = input("¿Está disponible? (si/no): ")
        archivo.write(f"{sabor},{precio},{disponible}\n")
    print("Nuevo sabor agregado correctamente.")



"""
PUNTO 3 - Cine
Crear un archivo cine.csv con tres películas, mostrar el contenido, agregar una nueva película y mostrar el archivo actualizado.
"""

def crear_cine():
    with open("cine.csv", "w") as archivo:
        archivo.write("Matrix,1500,18:00\n")
        archivo.write("Avatar,1800,20:30\n")
        archivo.write("Toy Story,1300,16:00\n")
    print("Archivo 'cine.csv' creado correctamente.")

def mostrar_cine():
    try:
        with open("cine.csv", "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo 'cine.csv' no existe. Créelo primero.")

def agregar_pelicula():
    with open("cine.csv", "a") as archivo:
        nombre = input("Ingrese nombre de la película: ")
        precio = input("Ingrese precio: ")
        horario = input("Ingrese horario: ")
        archivo.write(f"{nombre},{precio},{horario}\n")
    print("Película agregada correctamente.")
    mostrar_cine()



"""
PUNTO 4 - Pacientes
Crear un archivo pacientes.csv, mostrar su contenido, y permitir agregar nuevos pacientes.
"""

def crear_pacientes():
    with open("pacientes.csv", "w") as archivo:
        archivo.write("Juan,30,si\n")
        archivo.write("María,45,no\n")
        archivo.write("Pedro,27,si\n")
    print("Archivo 'pacientes.csv' creado correctamente.")

def mostrar_pacientes():
    try:
        with open("pacientes.csv", "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo 'pacientes.csv' no existe. Créelo primero.")

def agregar_paciente():
    with open("pacientes.csv", "a") as archivo:
        nombre = input("Ingrese nombre del paciente: ")
        edad = input("Ingrese edad: ")
        turno = input("¿Tiene turno? (si/no): ")
        archivo.write(f"{nombre},{edad},{turno}\n")
    print("Paciente agregado correctamente.")
    mostrar_pacientes()



"""
PUNTO 5 - Excursiones
Crear un archivo excursiones.csv, mostrar sus destinos y permitir agregar una nueva excursión.
"""

def crear_excursiones():
    with open("excursiones.csv", "w") as archivo:
        archivo.write("Bariloche,250000,si\n")
        archivo.write("Iguazu,200000,no\n")
        archivo.write("Mendoza,180000,si\n")
    print("Archivo 'excursiones.csv' creado correctamente.")

def mostrar_excursiones():
    try:
        with open("excursiones.csv", "r") as archivo:
            for linea in archivo:
                destino, precio, disponible = linea.strip().split(",")
                print(f"Destino: {destino} | Precio: ${precio} | Disponible: {disponible}")
    except FileNotFoundError:
        print("El archivo 'excursiones.csv' no existe. Créelo primero.")

def agregar_excursion():
    with open("excursiones.csv", "a") as archivo:
        destino = input("Ingrese el destino: ")
        precio = input("Ingrese el precio: ")
        disponible = input("¿Está disponible? (si/no): ")
        archivo.write(f"{destino},{precio},{disponible}\n")
    print("Excursión agregada correctamente.")
    mostrar_excursiones()



while True:
    print("\n------------------------------")
    print("        MENÚ PRINCIPAL        ")
    print("------------------------------")
    print("1. Punto 1 - Notas")
    print("2. Punto 2 - Heladería")
    print("3. Punto 3 - Cine")
    print("4. Punto 4 - Pacientes")
    print("5. Punto 5 - Excursiones")
    print("6. Salir")
    print("------------------------------")

    opcion = input("Seleccione una opción: ")


    if opcion == "1":
        while True:
            print("\n--- PUNTO 1: NOTAS ---")
            print("1. Crear archivo")
            print("2. Leer archivo")
            print("3. Mostrar con formato")
            print("4. Agregar alumnos")
            print("5. Reescribir archivo")
            print("6. Volver al menú principal")
            sub = input("Opción: ")
            if sub == "1":
                crear_notas()
            elif sub == "2":
                leer_notas()
            elif sub == "3":
                mostrar_notas_formato()
            elif sub == "4":
                agregar_notas()
            elif sub == "5":
                reescribir_notas()
            elif sub == "6":
                break
            else:
                print("Opción inválida.")


    elif opcion == "2":
        while True:
            print("\n--- PUNTO 2: HELADERÍA ---")
            print("1. Crear archivo")
            print("2. Mostrar contenido")
            print("3. Agregar sabor")
            print("4. Volver al menú principal")
            sub = input("Opción: ")
            if sub == "1":
                crear_heladeria()
            elif sub == "2":
                mostrar_heladeria()
            elif sub == "3":
                agregar_sabor()
            elif sub == "4":
                break
            else:
                print("Opción inválida.")


    elif opcion == "3":
        while True:
            print("\n--- PUNTO 3: CINE ---")
            print("1. Crear archivo")
            print("2. Mostrar contenido")
            print("3. Agregar película")
            print("4. Volver al menú principal")
            sub = input("Opción: ")
            if sub == "1":
                crear_cine()
            elif sub == "2":
                mostrar_cine()
            elif sub == "3":
                agregar_pelicula()
            elif sub == "4":
                break
            else:
                print("Opción inválida.")


    elif opcion == "4":
        while True:
            print("\n--- PUNTO 4: PACIENTES ---")
            print("1. Crear archivo")
            print("2. Mostrar contenido")
            print("3. Agregar paciente")
            print("4. Volver al menú principal")
            sub = input("Opción: ")
            if sub == "1":
                crear_pacientes()
            elif sub == "2":
                mostrar_pacientes()
            elif sub == "3":
                agregar_paciente()
            elif sub == "4":
                break
            else:
                print("Opción inválida.")


    elif opcion == "5":
        while True:
            print("\n--- PUNTO 5: EXCURSIONES ---")
            print("1. Crear archivo")
            print("2. Mostrar destinos")
            print("3. Agregar excursión")
            print("4. Volver al menú principal")
            sub = input("Opción: ")
            if sub == "1":
                crear_excursiones()
            elif sub == "2":
                mostrar_excursiones()
            elif sub == "3":
                agregar_excursion()
            elif sub == "4":
                break
            else:
                print("Opción inválida.")

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida, intente nuevamente.")
