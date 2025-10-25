#Crear un archivo llamado “notas.txt” que contenga tres líneas con el nombre de un alumno y su nota, 
# separados por una coma.
print("punto 1")
with open('notas.txt', 'w') as file:
    file.write("Juan,9\n")
    file.write('Nahuel,10\n')
    file.write("Agustin,9\n")
#Abrir el archivo en modo lectura y mostrar su contenido línea por línea, eliminando los saltos de línea.
with open('notas.txt', 'r') as file:
    for line in file:
        print(line.strip())
#Leer el archivo y mostrar los datos con el siguiente formato:
#Alumno: Sofía | Nota: 9
with open('notas.txt', 'r') as file:
    for line in file:
        nombre, nota= line.strip().split(',')
        print(f'Alumno: {nombre} | Nota: {nota}')
#Abrir el archivo en modo 'a' y permitir agregar más alumnos con sus notas desde teclado.
#El usuario puede ingresar varios hasta escribir “n”.
with open('notas.txt', 'a') as file:
    while True:
        nombre= input("Ingrese el nombre del alumno (o 'n' para terminar): ")
        if nombre.lower() == 'n':
            break
        nota= input("Ingrese la nota del alumno: ")
        file.write(f"{nombre},{nota}\n")
#Reescribir el archivo desde cero con una nueva lista de tres alumnos distintos.
#Mostrar un mensaje que indique que el contenido anterior fue reemplazado
with open('notas.txt', 'w') as file:
    file.write("Lucia,9\n")
    file.write("Sofia,10\n")
    file.write("Abril,5\n")
    print("Contenido anterior reemplazado.")
print("-------------------------------------------")
#Crear un archivo llamado heladeria.csv con tres sabores de ejemplo.
#Agregar un nuevo sabor
#Pedir al usuario que ingrese:
#El nombre del sabor, El precio, Si está disponible ("si" o "no")
#Luego abrir el archivo en modo 'a' (agregar) y escribir la nueva línea sin borrar el contenido anterior.
#Confirmar la actualización
print("punto 2")
with open("heladeria.csv", "w") as file:
    file.write("Chocolate,1200,si\n")
    file.write("Vainilla,800,si\n")
    file.write("Dulce de Leche,1000,no\n")
with open("heladeria.csv", "r") as file:
        for line in file:
            sabor, precio, disponible = line.strip().split(',')
            print(f"Sabor: {sabor} | Precio: ${precio} | Disponible: {disponible}")
            nuevo_sabor = input("Ingrese el nuevo sabor: ")
            nuevo_precio = input("Ingrese el precio: ")
            nuevo_disponible = input("Esta disponible? (si/no): ")
with open("heladeria.csv", "a") as file:
                file.write(f"{nuevo_sabor},{nuevo_precio},{nuevo_disponible}\n")
                print("Sabor agregado.")
print("-------------------------------------------")
#Crear un archivo llamado cine.csv con tres películas.
#	Mostrar el contenido del archivo
#	Leer el archivo completo y mostrar su contenido tal cual está (sin procesar línea por línea todavía).
#Agregar una nueva película-Pedir al usuario los datos y agregarlos sin borrar el contenido anterior
#Mostrar confirmación final
# abrir el archivo y mostrar su contenido actualizado
print("punto 3")
with open('cine.csv', 'w') as file:
    file.write("El Transportador,Accion\n")
    file.write("Bocchi the Rock!RE:,Animacion\n")
    file.write("Dragon Ball Z: La galaxia está en peligro,Animacion\n")
with open('cine.csv', 'r') as file:
        contenido = file.read()
        print("Contenido del archivo cine.csv:")
        print(contenido)
        nuevo_titulo = input("Ingrese el nuevo título de la película: ")
        nuevo_genero = input("Ingrese el género de la película: ")
with open('cine.csv', 'a') as file:
            file.write(f"{nuevo_titulo},{nuevo_genero}\n")
            print("Película agregada.")
with open('cine.csv', 'r') as file:
        print("Contenido actualizado del archivo cine.csv:")
        for line in file:
            print(line.strip())
print("-------------------------------------------")
#•	Crear un archivo llamado pacientes.csv con los siguientes datos:
#nombre,edad,turno
#•	Abrir el archivo en modo lectura y mostrar el contenido
#•	Permitir al usuario agregar un nuevo paciente, pidiendo:
#Nombre
#Edad
#Si tiene turno (“si” / “no”)
#Luego escribir esa línea al final del archivo.
#Reabrir el archivo y mostrar el contenido actualizado.
print("punto 4")
with open('pacientes.csv', 'w') as file:
    file.write("nombre,edad,turno\n")
    file.write("George,76,si\n")
    file.write("Luis,45,no\n")
    file.write("Marta,28,si\n")
with open('pacientes.csv', 'r') as file:
        print("Contenido del archivo pacientes.csv:")
        for line in file:
            print(line.strip())
        nuevo_nombre = input("Ingrese el nombre del paciente: ")
        nueva_edad = input("Ingrese la edad del paciente: ")
        nuevo_turno = input("Tiene turno? (si/no): ")
with open('pacientes.csv', 'a') as file:
     file.write(f"{nuevo_nombre},{nueva_edad},{nuevo_turno}\n")
     print("Paciente agregado.")
with open('pacientes.csv', 'r') as file:
     print("Contenido actualizado del archivo pacientes.csv:")
     for line in file:
        print(line.strip())
print("-------------------------------------------")
#Crear un archivo llamado excursiones.csv con el siguiente contenido:
#destino,precio,disponible
#Abrir el archivo en modo lectura y mostrar los destinos.
#Agregar una nueva excursión.
#Pedir al usuario:
#El nombre del destino
#El precio
#Si está disponible (“si” o “no”)
#Luego abrir el archivo en modo 'a' y escribir la nueva línea sin borrar el contenido anterior.
#Reabrir el archivo y mostrar su contenido actualizado.
print("punto 5")
with open('excursiones.csv', 'w') as file:
    file.write("destino,precio,disponible\n")
    file.write("Cataratas del Iguazu,5000,si\n")
    file.write("Bariloche,7000,no\n")
    file.write("Mendoza,6000,si\n")
with open('excursiones.csv', 'r') as file:
    print("Contenido del archivo excursiones.csv:")
    for line in file:
        print(line.strip())
    nuevo_destino = input("Ingrese el nombre del nuevo destino: ")
    nuevo_precio = input("Ingrese el precio: ")
    nuevo_disponible = input("Está disponible? (si/no): ")
with open('excursiones.csv', 'a') as file:
    file.write(f"{nuevo_destino},{nuevo_precio},{nuevo_disponible}\n")
    print("Nueva excursión agregada.")
with open('excursiones.csv', 'r') as file:
    print("Contenido actualizado del archivo excursiones.csv:")
    for line in file:
        print(line.strip())
print("-------------------------------------------")
