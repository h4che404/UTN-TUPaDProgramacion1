import csv
import os

CSV_FILE = "catalogo.csv"
CSV_HEADERS = ["TITULO", "CANTIDAD", "PRESTADOS"]

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
    guardar_catalogo_a_csv(ruta, muestra)
            


def cargar_catalogo_desde_csv(ruta) -> list[dict]:
    catalogo: list[dict] = []
    if not os.path.isfile(ruta): # Usar 'ruta' en lugar de CSV_FILE
        return catalogo
    else:
        with open(ruta, mode='r', newline='', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                # Asegura la existencia de la clave, si falta en un archivo viejo, usa 0
                prestados = parse_int_flexible(fila.get('PRESTADOS', 0)) 
                
                titulo = fila.get('TITULO', '').strip()
                cantidad = parse_int_flexible(fila.get('CANTIDAD', 0))
                
                # Validación básica
                if cantidad < 0 or titulo == "":
                    continue
                
                catalogo.append({
                    'TITULO': titulo, 
                    'CANTIDAD': cantidad, 
                    'PRESTADOS': prestados
                })
        return catalogo

def guardar_catalogo_a_csv(ruta: str, catalogo: list[dict]):
    # Validar que haya datos para guardar (opcional, pero buena práctica)
    if not catalogo:
        print("No hay datos en el catálogo para guardar. El archivo se guardará vacío.")
    
    # Abrir el archivo en modo 'w' (write/escritura) para SOBREESCRIBIR
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        # Usamos DictWriter y los encabezados globales
        writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
        
        # Escribir los encabezados (siempre se escriben primero)
        writer.writeheader()
        
        # Escribir todas las filas del catálogo
        for libro in catalogo:
            writer.writerow(libro)
            


# ----------------------------
# Búsquedas y reglas de negocio
# ----------------------------

def buscar_indice_por_titulo(catalogo: list[dict], titulo_busqueda: str) -> list[dict]:
    coincidencias = []
    termino_normalizado = normalizar_texto(titulo_busqueda)
    
    # Recorrido explícito para evitar comprensión de lista/lambda
    for libro in catalogo:
        titulo_normalizado = normalizar_texto(libro["TITULO"])
        
        # Lógica de búsqueda parcial: ¿Está el término dentro del título?
        if termino_normalizado in titulo_normalizado:
            coincidencias.append(libro)
            
    return coincidencias



def existe_titulo(catalogo: list[dict], titulo: str) -> bool:
    # Si la lista devuelta por la búsqueda tiene elementos, el título existe.
    coincidencias = buscar_indice_por_titulo(catalogo, titulo)
    return len(coincidencias) > 0


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
        guardar_catalogo_a_csv(CSV_FILE, catalogo)
        print("  ✔ Guardado.")

    return catalogo



def ingresar_ejemplares(catalogo: list[dict]) -> list[dict]:
    if not catalogo:
        print("Catálogo vacío.")
        return catalogo
    
    # 1. Pedir el título de forma parcial
    titulo_busqueda = input_str_solo_letras("Título (o parte del título) al que querés sumar ejemplares: ").strip()
    
    # 2. Obtener todas las coincidencias
    coincidencias = buscar_indice_por_titulo(catalogo, titulo_busqueda)
    
    if not coincidencias:
        print("No se encontró ningún título con esa coincidencia.")
        return catalogo
        
    print("\nCoincidencias encontradas:")
    # 3. Mostrar y permitir al usuario elegir
    for i, libro in enumerate(coincidencias):
        print(f"[{i}] Título: {libro['TITULO']}, Cantidad: {libro['CANTIDAD']}")

    while True:
        idx_coincidencia = input_int("Ingrese el número del libro que desea actualizar: ")
        if 0 <= idx_coincidencia < len(coincidencias):
            libro_seleccionado = coincidencias[idx_coincidencia]
            idx_catalogo = catalogo.index(libro_seleccionado)
            break
        else:
            print("Número fuera del rango de coincidencias.")
    while True:
        cantidad = input_int("Cantidad a sumar (>=0): ") 
        if cantidad is not None and cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue
        break 
    catalogo[idx_catalogo]["CANTIDAD"] += cantidad
    print(f"Actualizado: {catalogo[idx_catalogo]['TITULO']} ahora tiene {catalogo[idx_catalogo]['CANTIDAD']} ejemplares.")
    
    guardar_catalogo_a_csv(CSV_FILE, catalogo)
    return catalogo

def mostrar_catalogo(catalogo: list[dict]) -> None:
    if not catalogo:
        print("El catálogo está vacío.")
        return

    # Definir el ancho de las columnas
    ANCHO_TITULO = 40
    ANCHO_CANT = 10
    ANCHO_PREST = 10
    ANCHO_TOTAL = ANCHO_TITULO + ANCHO_CANT + ANCHO_PREST + 8 # +8 para los separadores y espacios

    # Imprimir encabezados de la tabla
    print("=" * ANCHO_TOTAL)
    print(f"{'TITULO':<{ANCHO_TITULO}} | {'DISPONIBLE':>{ANCHO_CANT}} | {'PRESTADOS':>{ANCHO_PREST}}")
    print("=" * ANCHO_TOTAL)

    # Imprimir cada libro
    for libro in catalogo:
        # Asegurarse de manejar los casos donde el libro pueda tener un título muy largo
        titulo_cortado = libro['TITULO'][:ANCHO_TITULO]
        
        # Uso de < (alineación izquierda) y > (alineación derecha)
        print(
            f"{titulo_cortado:<{ANCHO_TITULO}} | "
            f"{libro['CANTIDAD']:>{ANCHO_CANT}} | "
            f"{libro.get('PRESTADOS', 0):>{ANCHO_PREST}}" # Se usa .get para seguridad si falta la clave
        )
        
    print("=" * ANCHO_TOTAL)


def consultar_disponibilidad(catalogo: list[dict]) -> None:
    if not catalogo:
        print("El catálogo está vacío.")
        return

    # 1. Pedir la entrada de búsqueda y obtener coincidencias
    titulo_busqueda = input("Ingrese el título (o parte del título) a consultar: ").strip()
    coincidencias = buscar_indice_por_titulo(catalogo, titulo_busqueda)
    
    if not coincidencias:
        print("No se encontró ningún título que coincida con la búsqueda.")
        return

    # 2. Mostrar y permitir al usuario seleccionar una coincidencia
    print("\nCoincidencias encontradas:")
    for i, libro in enumerate(coincidencias):
        print(f"[{i}] Título: {libro['TITULO']}, Cantidad: {libro['CANTIDAD']}")

    while True:
            # Pide al usuario el índice de la lista de coincidencias
            idx_coincidencia = input("Ingrese el número del libro para consultar su disponibilidad: ").strip()
            
            if not idx_coincidencia.isdigit():
                print("Error: Ingrese un número válido.")
                continue
                
            idx_coincidencia = int(idx_coincidencia)

            if 0 <= idx_coincidencia < len(coincidencias):
                libro_seleccionado = coincidencias[idx_coincidencia]
                break
            else:
                print("Número fuera del rango de coincidencias. Intente de nuevo.")
            print("Entrada inválida. Ingrese un número.")
            
    # 3. Mostrar la disponibilidad del libro seleccionado
    cantidad = libro_seleccionado['CANTIDAD']
    titulo = libro_seleccionado['TITULO']
    
    print(f"\nEl título '{titulo}' tiene {cantidad} ejemplares disponibles.")


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
        titulo = input_str_solo_letras("Ingrese el título a agregar: ").strip()
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
    guardar_catalogo_a_csv(CSV_FILE, catalogo)
    print("Título agregado y guardado.")
    return catalogo


def actualizar_ejemplares_prestamo_devolucion(catalogo: list[dict]) -> list[dict]:

    if not catalogo:
        print("El catálogo está vacío.")
        return catalogo

    # 1. Búsqueda Parcial y Selección
    titulo_busqueda = input("Título (o parte del título) del libro a actualizar: ").strip()
    coincidencias = buscar_indice_por_titulo(catalogo, titulo_busqueda)
    
    if not coincidencias:
        print("No se encontró ningún título que coincida con la búsqueda.")
        return catalogo
        
    print("\nCoincidencias encontradas:")
    for i, libro in enumerate(coincidencias):
        print(f"[{i}] {libro['TITULO']} | Disp: {libro['CANTIDAD']} | Prestados: {libro['PRESTADOS']}")

    # Lógica para seleccionar el libro específico
    idx_catalogo = -1
    while True:
            idx_coincidencia = input("Ingrese el NÚMERO del libro para registrar la acción: ").strip()
            
            if not idx_coincidencia.isdigit():
                print("Error: Ingrese un número válido.")
                continue
                
            idx_coincidencia = int(idx_coincidencia)

            if 0 <= idx_coincidencia < len(coincidencias):
                libro_seleccionado = coincidencias[idx_coincidencia]
                idx_catalogo = catalogo.index(libro_seleccionado)
                break
            else:
                print("Número fuera del rango de coincidencias. Intente de nuevo.")
            print("Entrada inválida. Ingrese un número.")
            
    if idx_catalogo == -1: # Nunca debería pasar, pero como seguridad
        return catalogo 

    # Referencia directa al libro en el catálogo principal
    libro_a_actualizar = catalogo[idx_catalogo]

    # 2. Elegir Operación
    print("\n¿Qué acción desea realizar?")
    print("1) Préstamo (restar 1 a Disponible, sumar 1 a Prestados)")
    print("2) Devolución (sumar 1 a Disponible, restar 1 a Prestados)")
    opcion = input("Ingrese opción (1/2): ").strip()

    if opcion == "1":  # PRÉSTAMO
        if libro_a_actualizar['CANTIDAD'] > 0:
            libro_a_actualizar['CANTIDAD'] -= 1
            libro_a_actualizar['PRESTADOS'] += 1
            print(f"✔ Préstamo registrado para '{libro_a_actualizar['TITULO']}'.")
        else:
            print("No hay ejemplares disponibles para prestar.")

    elif opcion == "2":  # DEVOLUCIÓN
        if libro_a_actualizar['PRESTADOS'] > 0:
            libro_a_actualizar['CANTIDAD'] += 1
            libro_a_actualizar['PRESTADOS'] -= 1
            print(f"✔ Devolución registrada para '{libro_a_actualizar['TITULO']}'.")
        else:
            print("No hay ejemplares registrados como prestados para este título.")
    else:
        print("Opción inválida. No se realizaron cambios.")
    guardar_catalogo_a_csv(CSV_FILE, catalogo)
    return catalogo
    
def eliminar_titulo(catalogo: list[dict]) -> list[dict]:
    if not catalogo:
        print("El catálogo está vacío. No hay títulos para eliminar.")
        return catalogo

    # 1. Búsqueda Parcial
    # (Asumo que 'input_str_solo_letras' es una de tus funciones de validación)
    titulo_busqueda = input_str_solo_letras("Ingrese el título (o parte) a eliminar: ").strip()
    coincidencias = buscar_indice_por_titulo(catalogo, titulo_busqueda)

    if not coincidencias:
        print("⚠️ El título no existe en el catálogo.")
        return catalogo

    # 2. Manejar múltiples coincidencias
    print("\nCoincidencias encontradas:")
    for i, libro in enumerate(coincidencias):
        print(f"[{i}] {libro['TITULO']} (Disp: {libro['CANTIDAD']})")

    idx_seleccionado = -1

    # 3. Si hay más de uno, preguntar. Si solo hay uno, seleccionarlo.
    if len(coincidencias) > 1:
        while True:
            # Usar input_int para validar la entrada numérica
            idx_seleccionado = input_int("Se encontraron varias coincidencias. Ingrese el NÚMERO del libro que desea eliminar: ")
            
            if 0 <= idx_seleccionado < len(coincidencias):
                break
            else:
                print("Número fuera del rango de coincidencias. Intente de nuevo.")
    else:
        # Solo hay una coincidencia, la seleccionamos automáticamente
        idx_seleccionado = 0 

    # 4. Obtener el diccionario del libro a eliminar
    libro_a_eliminar = coincidencias[idx_seleccionado]

    # 5. Eliminar el libro usando list.remove()
    # .remove() busca el objeto (el diccionario) en la lista y lo borra.
    catalogo.remove(libro_a_eliminar) 
    
    # Llama a la función de guardado
    guardar_catalogo_a_csv(CSV_FILE, catalogo) 
    
    print(f"Se eliminó el título '{libro_a_eliminar['TITULO']}' del catálogo y del CSV.")
    return catalogo

# ----------------------------
# Menú e interacción (sin globales)
# ----------------------------

def mostrar_menu() -> None:
    print("""
================= MENÚ BIBLIOTECA =================
1 - Ingresar títulos (múltiples)
2 - Ingresar ejemplares
3 - Mostrar catálogo
4 - Consultar disponibilidad
5 - Listar agotados
6 - Agregar título
7 - Actualizar ejemplares (Préstamo/Devolución)
8 - Eliminar título
9 - Salir
====================================================
""")


def main() -> None:
    print("📚 Iniciando sistema de Biblioteca…")
    if not archivo_existe(CSV_FILE):
        print("No se encontró el archivo base, se creará uno de ejemplo.")
        crear_csv_ejemplo(CSV_FILE)
    catalogo: list[dict] = cargar_catalogo_desde_csv(CSV_FILE)
    print(f"\n{len(catalogo)} libros cargados correctamente.\n")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1":
                catalogo = ingresar_titulos_multiples(catalogo)
            case "2":
                catalogo = ingresar_ejemplares(catalogo)
            case "3":
                mostrar_catalogo(catalogo)
            case "4":
                consultar_disponibilidad(catalogo)
            case "5":
                listar_agotados(catalogo)
            case "6":
                catalogo = agregar_titulo(catalogo)
            case "7":
                catalogo = actualizar_ejemplares_prestamo_devolucion(catalogo)
            case "8":
                catalogo = eliminar_titulo(catalogo)
            case "9":
                print("👋 Saliendo. ¡Hasta luego!")
                break
            case _:
                print("⚠️ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
