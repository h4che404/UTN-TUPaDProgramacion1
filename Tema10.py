'''
Caso 10 – Hotel – Habitaciones y estado (0=libre / 1=ocupada)
Enunciado / Descripción
Un hotel desea un sistema para controlar el estado de sus habitaciones (libre u ocupada). Se pide construir un menú que utilice listas paralelas: una lista habitaciones[] para almacenar los números de las habitaciones (e.g., 101, 102, 201) y otra lista estados[] para almacenar el estado de cada habitación, donde 0 representa "libre" (desocupada) y 1 representa "ocupada". Ambas listas deben compartir el índice, de manera que el estado en estados[i] corresponda a la habitación en habitaciones[i]. El programa debe usar un bucle while para presentar un menú al usuario, permitiéndole realizar diferentes operaciones hasta que elija la opción "Salir".
Ejemplo:
•	habitaciones[] = [101, 102, 201]
•	estados[] = [0, 1, 0]
En este ejemplo:
•	La habitación 101 está libre (0).
•	La habitación 102 está ocupada (1).
•	La habitación 201 está libre (0).
Desafío: Implementar el sistema de gestión de habitaciones y estados utilizando listas paralelas y un menú interactivo.
Menú:
1.	Ingresar números de habitación: (Registrar las habitaciones del hotel)
o	Permite al usuario ingresar los números de las habitaciones del hotel.
o	Ejemplo: El usuario ingresa "103", "104", "202".
2.	Ingresar estados (0/1) paralelos: (Definir el estado inicial de cada habitación)
o	Permite al usuario ingresar el estado inicial de cada habitación, utilizando 0 para "libre" y 1 para "ocupada". Debe corresponder al orden de las habitaciones ingresadas previamente.
o	Ejemplo: Si las habitaciones son "103", "104" y "202", el usuario podría ingresar "0" para 103, "1" para 104 y "0" para 202.
3.	Mostrar estado general: (Mostrar el estado de todas las habitaciones)
o	Muestra una lista de todas las habitaciones y su estado correspondiente (libre u ocupada).
o	Ejemplo de salida:
	"Habitación 101: Libre"
	"Habitación 102: Ocupada"
	"Habitación 201: Libre"
	"Habitación 103: Libre"
	"Habitación 104: Ocupada"
	"Habitación 202: Libre"
4.	Consultar estado de una habitación: (Verificar el estado de una habitación específica)
o	Permite al usuario ingresar el número de una habitación y ver su estado actual (libre u ocupada).
o	Ejemplo: El usuario ingresa "102" y el programa muestra "Habitación 102: Ocupada".
5.	Listar ocupadas o libres (según lo que se pida): (Mostrar una lista de habitaciones según su estado)
o	Permite al usuario elegir si quiere ver la lista de habitaciones ocupadas o la lista de habitaciones libres.
6.	Agregar habitación: (Añadir una nueva habitación al sistema)
o	Permite al usuario agregar una nueva habitación al sistema, asignándole un estado inicial (libre u ocupada).
7.	Ver libres: (Mostrar solo las habitaciones libres)
o	Muestra una lista reducida que solo incluye las habitaciones que están libres (estado = 0).
8.	Cambiar estado: (Cambiar el estado de una habitación)
o	Permite al usuario cambiar el estado de una habitación (de libre a ocupada o de ocupada a libre). Debe solicitar el número de habitación y el nuevo estado deseado.
9.	Ver todas: (Mostrar todas las habitaciones y su estado)
o	Muestra una lista completa de todas las habitaciones y su estado correspondiente, similar a la opción 3.
10.	Salir: (Terminar el programa)
o	Termina la ejecución del programa.
'''

habitaciones = []
estados = [0, 1]


while True:
    print("\n--- Menú ---")
    print("1. Ingresar números de habitación")
    print("2. Ingresar estados (0/1) paralelos")
    print("3. Mostrar estado general")
    print("4. Consultar estado de una habitación")
    print("5. Listar ocupadas o libres (según lo que se pida)")
    print("6. Agregar habitación")
    print("7. Ver libres")
    print("8. Cambiar estado")
    print("9. Ver todas")
    print("10. Salir")

    opcion = int(input("Seleccione una opción (1-10): "))
    if opcion == 1:
        num_habitacion = input("Ingrese el número de la habitación (o 'fin' para terminar): ")
        while num_habitacion.lower() != 'fin':
            if num_habitacion.isdigit():
                habitaciones.append(int(num_habitacion))
                num_habitacion = input("Ingrese el número de la habitación (o 'fin' para terminar): ")
            else:
                print("Por favor, ingrese un número válido.")
                num_habitacion = input("Ingrese el número de la habitación (o 'fin' para terminar): ")
    elif opcion == 2:
        for i in range(len(habitaciones)):
            estado = input(f'Ingrese el estado de la habitacion {habitaciones[i]} (0=libre, 1=ocupada): ')
            while estado not in ['0', '1']:
                print("Estado inválido. Ingrese 0 para libre o 1 para ocupada.")
                estado = input(f'Ingrese el estado de la habitacion {habitaciones[i]} (0=libre, 1=ocupada): ')
            estados.append(int(estado))
    elif opcion == 3:
        for i in range(len(habitaciones)):
            if estados[i] == 0:
                estado_str = 'Libre' 
            else:
                estado_str = 'Ocupada'
            print(f'Habitacion Nro {habitaciones[i]} --> {estado_str} ')
    elif opcion == 4:
        num_habitacion = int(input('Ingrese el numero de la habitacion: '))
        est = habitaciones.index(num_habitacion)
        if estados[i] == 0:
                estado_str = 'Libre' 
        else:
                estado_str = 'Ocupada'
        print(f'Habitacion Nro {habitaciones[est]} --> {estado_str}')
    elif opcion == 5: 
        print('1. Libres')
        print('2. Ocupadas')
        sub_opcion = int(input('Seleccione una opción (1-2): '))
        if sub_opcion == 1:
            print('Habitaciones Libres:')
            for i in range(len(habitaciones)):
                if estados[i] == 0:
                    print(f'Habitacion Nro {habitaciones[i]} --> Libre')
        elif sub_opcion == 2:
            print('Habitaciones Ocupadas:')
            for i in range(len(habitaciones)):
                if estados[i] == 1:
                    print(f'Habitacion Nro {habitaciones[i]} --> Ocupada')
        else:
            print('Opción inválida.')
    elif opcion == 6:
        agg = int(input('Ingrese el numero de la habitacion a agregar: '))
        habitaciones.append(agg)
        estado = input(f'Ingrese el estado de la habitacion {agg} (0=libre, 1=ocupada): ')
        while estado not in ['0', '1']:
            print("Estado inválido. Ingrese 0 para libre o 1 para ocupada.")
            estado = input(f'Ingrese el estado de la habitacion {agg} (0=libre, 1=ocupada): ')
        estados.append(int(estado))
    elif opcion == 7:
        print('Habitaciones Libres:')
        for i in range(len(habitaciones)):
            if estados[i] == 0:
                print(f'Habitacion Nro {habitaciones[i]} --> Libre')
    elif opcion == 8:
        num_habitacion = int(input('Ingrese el numero de la habitacion a cambiar estado: '))
        if num_habitacion in habitaciones:
            est = habitaciones.index(num_habitacion)
            nuevo_estado = input(f'Ingrese el nuevo estado para la habitacion {num_habitacion} (0=libre, 1=ocupada): ')
            while nuevo_estado not in ['0', '1']:
                print("Estado inválido. Ingrese 0 para libre o 1 para ocupada.")
                nuevo_estado = input(f'Ingrese el nuevo estado para la habitacion {num_habitacion} (0=libre, 1=ocupada): ')
            estados[est] = int(nuevo_estado)
            print(f'El estado de la habitacion {num_habitacion} ha sido actualizado.')
        else:
            print('La habitacion no existe.')
    elif opcion == 9:
        for i in range(len(habitaciones)):
            if estados[i] == 0:
                estado_str = 'Libre' 
            else:
                estado_str = 'Ocupada'
            print(f'Habitacion Nro {habitaciones[i]} --> {estado_str} ')
    elif opcion == 10:
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 10.")
