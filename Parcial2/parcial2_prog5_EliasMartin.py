import csv
import os

CSV_FILE = "catalogo.csv"


# ----------------------------
# Utilidades (VALIDACIONES)
# ----------------------------

def normalizar_titulo(t: str) -> str:
    """
    Devuelve el título normalizado para comparación.
    Requisitos:
    - Quitar espacios sobrantes intermedios y extremos.
    - Pasar a minúsculas.
    : implementar y devolver el string normalizado.
    """
    t = t.strip()
    t = ' '.join(t.split())
    t = t.lower()
    return t 


def titulo_valido(t: str) -> bool:
    """
    Un título es válido si, tras normalizar, no queda vacío.
    implementar y devolver True/False.
    """

    
    if normalizar_titulo(t) == "":
        return True
    else:  
        return False 


def pedir_titulo(msg: str) -> str:
    """
    Pide un título por input hasta que sea válido según las reglas del enunciado.
    Requisitos:
    - No vacío.
    - Comparación insensible a mayúsculas y con espacios normalizados.
    - Debe devolver el título ya normalizado para mostrar/guardar prolijo.
    implementar bucle de pedido y validación.
    """

    titulo = input(msg).strip()
    if titulo_valido(titulo):
        return normalizar_titulo(titulo)
    return ""


def pedir_entero_no_negativo(msg: str) -> int:
    """
    Pide un entero >= 0 (usar validaciones simples como str.isdigit()).
    Debe volver a pedir si el valor no es válido.
    implementar bucle de pedido y validación; devolver int.
    """
    while True:
        valor = input(msg).strip()
        if valor.isdigit():
            return int(valor)
        else:
            print("Entrada inválida. Ingrese un número entero no negativo.")


# ----------------------------
# Persistencia CSV
# ----------------------------

def cargar_catalogo_desde_csv() -> list[dict]:
    """
    Carga el catálogo desde CSV si existe.
    Formato: encabezado TITULO,CANTIDAD
    Requisitos mínimos:
    - Si no existe, devolver lista vacía.
    - Saltar filas inválidas.
    - Convertir CANTIDAD a int cuando corresponda.
    implementar lectura real con csv.DictReader.
    """
    catalogo: list[dict] = []
    if not os.path.isfile(CSV_FILE):
        return catalogo
    else:
        with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                titulo = fila['TITULO'].strip()
                cantidad = int(fila['CANTIDAD'])
                if cantidad < 0:
                    continue
                catalogo.append({'TITULO': titulo, 'CANTIDAD': cantidad})
        return catalogo


def guardar_catalogo_a_csv(catalogo: list[dict]) -> None:
    """
    Guarda el catálogo al CSV (sobrescribe).
    Columnas: TITULO,CANTIDAD (con encabezado)
    Requisitos:
    - Escribir siempre encabezado.
    - Asegurar que CANTIDAD sea entero no negativo.
    implementar escritura real con csv.DictWriter.
    """

    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as archivo_csv:
        encabezado = ['TITULO', 'CANTIDAD']
        escritor = csv.DictWriter(archivo_csv, fieldnames=encabezado)

        escritor.writeheader()  # escribe TITULO,CANTIDAD

        for libro in catalogo:
            titulo = libro['TITULO'].strip()
            cantidad = int(libro['CANTIDAD'])

            # Validación: cantidad no negativa
            if cantidad < 0:
                cantidad = 0

            escritor.writerow({'TITULO': titulo, 'CANTIDAD': cantidad})
catalogo = cargar_catalogo_desde_csv()
catalogo.append({'TITULO': 'Nuevo Libro', 'CANTIDAD': 3})
guardar_catalogo_a_csv(catalogo)

# ----------------------------
# Búsquedas y reglas de negocio
# ----------------------------

def buscar_indice_por_titulo(catalogo: list[dict], titulo_busqueda: str) -> int:
    """
    Devuelve el índice del libro cuyo título coincide (comparación normalizada).
    Si no existe, devuelve -1.
    implementar recorrido y comparación con normalización.
    """
    titulo_busqueda_normalizado = normalizar_titulo(titulo_busqueda)
    for indice, libro in enumerate(catalogo):
        titulo_libro_normalizado = normalizar_titulo(libro['TITULO'])
        if titulo_libro_normalizado == titulo_busqueda_normalizado:
            return indice
    return -1



def existe_titulo(catalogo: list[dict], titulo: str) -> bool:
    """
    True si el título ya existe en el catálogo (comparación normalizada).
    implementar usando buscar_indice_por_titulo.
    """
    indice = buscar_indice_por_titulo(catalogo, titulo)
    if indice != -1:
        return True
    else:
        return False 


# ----------------------------
# Operaciones (CRUD / reportes)
# ----------------------------

def ingresar_titulos_multiples(catalogo: list[dict]) -> list[dict]:
    """
    1) Ingresar títulos (múltiples):
       - Pedir cuántos libros cargar.
       - Por cada uno: TITULO (no vacío, no duplicado) y CANTIDAD (>=0).
       - Guardar automáticamente tras cambios.
    Debe devolver el catálogo actualizado.
    """
    # pedir cantidad de registros a ingresar
    while True:
        cant_raw = input("¿Cuántos libros querés cargar? ")
        n = int(cant_raw)
        if n < 0:
            print("Debe ser un número entero >= 0.")
            continue
        else:
            break

    for i in range(1, n + 1):
        print(f"\nLibro #{i}")
        # título (no vacío, no duplicado)
        while True:
            titulo = input("  TITULO: ").strip()
            if not titulo:
                print("  El título no puede estar vacío.")
                continue
            if existe_titulo(catalogo, titulo):
                print("  Ya existe un libro con ese título (no se permiten duplicados).")
                continue
            break

        # cantidad (entero >= 0)
        while True:
            cant_raw = input("  CANTIDAD (>=0): ").strip()
            cantidad = int(cant_raw)
            if cantidad < 0:
                print("  Debe ser >= 0.")
                continue
            else:
                print("  Ingresá un entero válido.")
            break

        # agregar y guardar automáticamente
        catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
        guardar_catalogo_a_csv(catalogo)
        print("  ✔ Guardado.")

    return catalogo


def ingresar_ejemplares(catalogo: list[dict]) -> list[dict]:
    """
    2) Ingresar ejemplares a un título existente (sumar cantidad).
    Requisitos:
    - Verificar existencia del título.
    - Sumar cantidad (>=0).
    - Guardar automáticamente tras cambios.
    Debe devolver el catálogo actualizado.
    implementar.
    """
    print("→ Ingresar ejemplares: PENDIENTE DE IMPLEMENTAR")
    if not catalogo:
        print("Catálogo vacío.")
        return catalogo
    titulo = normalizar_titulo(input("Título al que querés sumar ejemplares: "))
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx is None:
        print("No existe ese título.")
        return catalogo
    while True:
        try:
            cantidad = int(input("Cantidad a sumar (>=0): ").strip())
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Ingresá un entero válido.")
    catalogo[idx]["CANTIDAD"] += cantidad
    guardar_catalogo_a_csv(catalogo)
    print("Actualizado y guardado.")
    return catalogo
    return catalogo 


def mostrar_catalogo(catalogo: list[dict]) -> None:
    """
    3) Mostrar catálogo completo (título + stock).
    Requisitos:
    - Formato simple, un libro por línea.
    - Indicar si el catálogo está vacío.
     implementar.
    """
    print("→ Mostrar catálogo: PENDIENTE DE IMPLEMENTAR")
    if not catalogo:
        print("El catálogo está vacío.")
        return
    for libro in catalogo:
        print(f"Título: {libro['TITULO']}, Cantidad: {libro['CANTIDAD']}")


def consultar_disponibilidad(catalogo: list[dict]) -> None:
    """
    4) Consultar disponibilidad de un título (mostrar cuántos ejemplares hay).
    Requisitos:
    - Verificar existencia del título.
    - Mostrar cantidad disponible.
    implementar.
    """
    print("→ Consultar disponibilidad: PENDIENTE DE IMPLEMENTAR")
    titulo = normalizar_titulo(input("Ingrese el título a consultar: "))
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print("No existe ese título en el catálogo.")
        return
    cantidad = catalogo[idx]['CANTIDAD']
    print(f"El título '{catalogo[idx]['TITULO']}' tiene {cantidad} ejemplares disponibles.")


def listar_agotados(catalogo: list[dict]) -> None:
    """
    5) Listar sólo títulos con CANTIDAD == 0.
    Requisitos:
    - Mostrar lista o indicar que no hay agotados.
    implementar.
    """
    print("→ Listar agotados: PENDIENTE DE IMPLEMENTAR")
    agotados = [libro for libro in catalogo if libro['CANTIDAD'] == 0]
    if not agotados:
        print("No hay títulos agotados.")
        return
    print("Títulos agotados:")
    for libro in agotados:
        print(f"- {libro['TITULO']}")



def agregar_titulo(catalogo: list[dict]) -> list[dict]:
    """
    6) Agregar título individual (validar duplicados) con cantidad inicial.
    Requisitos:
    - TITULO válido y único.
    - CANTIDAD inicial >= 0.
    - Guardar automáticamente tras cambios.
    Debe devolver el catálogo actualizado.
    implementar.
    """
    print("→ Agregar título: PENDIENTE DE IMPLEMENTAR")
    while True:
        titulo = input("Ingrese el título a agregar: ").strip()
        if not titulo:
            print("El título no puede estar vacío.")
            continue
        if existe_titulo(catalogo, titulo):
            print("Ya existe un libro con ese título (no se permiten duplicados).")
            continue
        break
    while True:
        cantidad = int(input("Ingrese la cantidad inicial (>=0): ").strip())
        if cantidad < 0:
            print("La cantidad debe ser >= 0.")
            continue
        else:
            print("Ingresá un entero válido.")
            break
    catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    guardar_catalogo_a_csv(catalogo)
    print("Título agregado y guardado.")
    return catalogo


def actualizar_ejemplares_prestamo_devolucion(catalogo: list[dict]) -> list[dict]:
    """
    7) Actualizar ejemplares:
       - Préstamo: restar 1 sólo si CANTIDAD > 0.
       - Devolución: sumar 1.
       - Guardar automáticamente tras cambios.
    Debe devolver el catálogo actualizado.
    """
    if not catalogo:
        print("El catálogo está vacío.")
        return catalogo

    titulo = input("Título del libro a actualizar: ").strip()
    
    # Buscar el libro en el catálogo
    indice = None
    for i, libro in enumerate(catalogo):
        if libro['TITULO'].strip().lower() == titulo.lower():
            indice = i
            break

    if indice is None:
        print("No se encontró ese título en el catálogo.")
        return catalogo

    # Elegir operación
    print("\n¿Qué acción desea realizar?")
    print("1) Préstamo (restar 1)")
    print("2) Devolución (sumar 1)")
    opcion = input("Ingrese opción (1/2): ").strip()

    if opcion == "1":  # PRÉSTAMO
        if catalogo[indice]['CANTIDAD'] > 0:
            catalogo[indice]['CANTIDAD'] -= 1
            print("✔ Préstamo registrado.")
        else:
            print("No hay ejemplares disponibles para prestar.")

    elif opcion == "2":  # DEVOLUCIÓN
        catalogo[indice]['CANTIDAD'] += 1
        print("✔ Devolución registrada.")

    else:
        print("Opción inválida. No se realizaron cambios.")
        return catalogo

    # Guardar cambios automáticamente
    guardar_catalogo_a_csv(catalogo)
    print("📁 Cambios guardados en catalogo.csv.")

    return catalogo


# ----------------------------
# Menú e interacción (sin globales)
# ----------------------------

def mostrar_menu() -> None:
    print("""
================= MENU =================
1) Ingresar títulos (múltiples)
2) Ingresar ejemplares a un título existente
3) Mostrar catálogo
4) Consultar disponibilidad de un título
5) Listar libros agotados (cantidad = 0)
6) Agregar un único título
7) Registrar préstamo / devolución
8) Salir
========================================
""")


def main() -> None:
    print("📚 Iniciando sistema de Biblioteca…")
    catalogo: list[dict] = cargar_catalogo_desde_csv()
    if len(catalogo) == 0:
        print("ℹ️ Catálogo vacío o CSV no encontrado.")
    else:
        print(f"✅ Catálogo cargado. {len(catalogo)} título(s).")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            catalogo = ingresar_titulos_multiples(catalogo)
        elif opcion == "2":
            catalogo = ingresar_ejemplares(catalogo)
        elif opcion == "3":
            mostrar_catalogo(catalogo)
        elif opcion == "4":
            consultar_disponibilidad(catalogo)
        elif opcion == "5":
            listar_agotados(catalogo)
        elif opcion == "6":
            catalogo = agregar_titulo(catalogo)
        elif opcion == "7":
            catalogo = actualizar_ejemplares_prestamo_devolucion(catalogo)
        elif opcion == "8":
            print("👋 Saliendo. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
