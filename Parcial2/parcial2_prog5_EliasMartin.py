import csv
import os

CSV_FILE = "catalogo.csv"
CSV_HEADERS = ["NOMBRE", "CANTIDAD"]

# ----------------------------
# Utilidades (VALIDACIONES)
# ----------------------------


def normalizar_titulo(t: str) -> str:
    
    t = t.strip()
    t = ' '.join(t.split())
    t = t.lower()
    return t 

def normalizar_texto(texto):
    """Devuelve el texto sin espacios extras y en minúsculas."""
    if texto is None:
        return ""
    # Mapa de acentos a caracteres sin acento
    mapa_acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N', 'ü': 'u', 'Ü': 'U'   
    }
    for acentuada, sin_acentuar in mapa_acentos.items():
        texto = texto.replace(acentuada, sin_acentuar)
        
    return str(texto).strip().lower()

def parse_int_flexible(valor):
    #Convierte el valor en entero.
    #Elimina separadores (., ) y devuelve 0 si no es válido.
    if valor is None:
        return 0
    s = str(valor).strip()
    # Manejo de cadena vacía
    if s == "":
        return 0
    # Eliminación de separadores comunes y verificación de dígitos
    s = s.replace(" ", "").replace(",", "").replace(".", "")
    if s.lstrip("-").isdigit():
        return int(s)
    return 0

def input_int(mensaje, permitir_vacio=False, valor_defecto=None):
    """Pide un número entero y valida"""
    while True:
        entrada = input(mensaje).strip()
        if entrada == "" and permitir_vacio:
            return valor_defecto
        entrada_limpia = entrada.replace(" ", "").replace(",", "").replace(".", "")
        if entrada_limpia.lstrip("-").isdigit():
            return parse_int_flexible(entrada_limpia)
        print("Error: ingrese un número entero válido.")

def input_str_solo_letras(mensaje):
    while True:
        entrada = input(mensaje).strip()
        entrada = normalizar_texto(entrada).strip()
        if not entrada:
            print("Error: La entrada no puede estar vacía. Inténtelo de nuevo.")
            continue
        if entrada.isalpha():
            return entrada
        print("Error: Ingrese solo letras (caracteres alfabéticos).")

def titulo_valido(t: str) -> bool:
    if normalizar_titulo(t) == "":
        return True
    else:  
        return False 


def pedir_titulo(msg: str) -> str:
    titulo = input(msg).strip()
    if titulo_valido(titulo):
        return normalizar_titulo(titulo)
    return ""


def pedir_entero_no_negativo(msg: str) -> int:
    while True:
        valor = input(msg).strip()
        if valor.isdigit():
            return int(valor)
        else:
            print("Entrada inválida. Ingrese un número entero no negativo.")


# ----------------------------
# Persistencia CSV
# ----------------------------

def archivo_existe(ruta):
    """Devuelve True si el archivo existe y es accesible."""
    return os.path.isfile(ruta)

def crear_csv_ejemplo(ruta):
    """Crea un CSV de ejemplo si no existe."""
    # Datos de ejemplo 
    muestra = [
        {"TITULO": "Cien años de soledad", "CANTIDAD": 5},
        {"TITULO": "Don Quijote de la Mancha", "CANTIDAD": 2},
        {"TITULO": "La sombra del viento", "CANTIDAD": 0},
    ]
    # Guardar CSV de ejemplo
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
        writer.writeheader()
        for fila in muestra:
            writer.writerow(fila)
            


def cargar_catalogo_desde_csv(ruta) -> list[dict]:
    catalogo: list[dict] = []
    if not os.path.isfile(CSV_FILE):
        return catalogo
    else:
        with open(ruta, mode='r', newline='', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                titulo = fila['TITULO'].strip()
                cantidad = int(fila['CANTIDAD'])
                if cantidad < 0:
                    continue
                catalogo.append({'TITULO': titulo, 'CANTIDAD': cantidad})
        return catalogo




# ----------------------------
# Búsquedas y reglas de negocio
# ----------------------------

def buscar_indice_por_titulo(catalogo: list[dict], titulo_busqueda: str):
    return [p for p in catalogo if normalizar_texto(titulo_busqueda) in normalizar_texto(p["TITULO"])]



def existe_titulo(catalogo: list[dict], titulo: str) -> bool:
    indice = buscar_indice_por_titulo(catalogo, titulo)
    if indice != -1:
        return True
    else:
        return False 


# ----------------------------
# Operaciones (CRUD / reportes)
# ----------------------------

def ingresar_titulos_multiples(catalogo: list[dict]) -> list[dict]:
    # pedir cantidad de registros a ingresar
    while True:
        cant_raw = input_int("¿Cuántos libros querés cargar? ")
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
            titulo = input_str_solo_letras("  TITULO: ").strip()
            if not titulo:
                print("  El título no puede estar vacío.")
                continue
            if existe_titulo(catalogo, titulo):
                print("  Ya existe un libro con ese título (no se permiten duplicados).")
                continue
            break
        # cantidad (entero >= 0)
        while True:
            cant_raw = input_int("  CANTIDAD (>=0): ")
            cantidad = int(cant_raw)
            if cantidad < 0:
                print("  Debe ser >= 0.")
                continue
            else:
                print("  Ingresá un entero válido.")
            break

        # agregar y guardar automáticamente
        catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
        print("  ✔ Guardado.")

    return catalogo



def ingresar_ejemplares(catalogo: list[dict]) -> list[dict]:
    if not catalogo:
        print("Catálogo vacío.")
        return catalogo
    titulo = normalizar_titulo(input_str_solo_letras("Título al que querés sumar ejemplares: "))
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx is None:
        print("No existe ese título.")
        return catalogo
    while True:
            cantidad = int(input("Cantidad a sumar (>=0): ").strip())
            for libro in idx:
                print(f"{libro.__len__}Título: {libro['TITULO']}, Cantidad: {libro['CANTIDAD']}")
            indice = input("Ingrese el índice del libro a actualizar: ").strip()
            if not indice.isdigit() or int(indice) < 0 or int(indice) >= len(catalogo):
                print("Índice inválido. Intente nuevamente.")
                continue
            idx = int(indice)
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            break
    
    catalogo[idx]["CANTIDAD"] += cantidad
    print("Actualizado y guardado.")
    return catalogo


def mostrar_catalogo(catalogo: list[dict]) -> None:
    if not catalogo:
        print("El catálogo está vacío.")
        return
    for libro in catalogo:
        print(f"Título: {libro['TITULO']}, Cantidad: {libro['CANTIDAD']}")


def consultar_disponibilidad(catalogo: list[dict]) -> None:
    titulo = normalizar_titulo(input("Ingrese el título a consultar: "))
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print("No existe ese título en el catálogo.")
        return
    cantidad = catalogo[idx]['CANTIDAD']
    print(f"El título '{catalogo[idx]['TITULO']}' tiene {cantidad} ejemplares disponibles.")


def listar_agotados(catalogo: list[dict]) -> None:
    agotados = [libro for libro in catalogo if libro['CANTIDAD'] == 0]
    if not agotados:
        print("No hay títulos agotados.")
        return
    print("Títulos agotados:")
    for libro in agotados:
        print(f"- {libro['TITULO']}")



def agregar_titulo(catalogo: list[dict]) -> list[dict]:
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
    print("Título agregado y guardado.")
    return catalogo


def actualizar_ejemplares_prestamo_devolucion(catalogo: list[dict]) -> list[dict]:

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
    if not archivo_existe(CSV_FILE):
        print("No se encontró el archivo base, se creará uno de ejemplo.")
        crear_csv_ejemplo(CSV_FILE)
    catalogo: list[dict] = cargar_catalogo_desde_csv(CSV_FILE)
    print(f"\n{len(catalogo)} países cargados correctamente.\n")

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
