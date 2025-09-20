#TPlistas
"""
a) Creación de listas
Crea una lista con los nombres de 5 compañeros de clase.
Muestra en pantalla el primer y el último elemento de la lista.
"""
lista_nombre =["Nahuel","Agustin","Juan Cruz", "Joaco","David"]
print("primer compañero", lista_nombre[0])
print("quinto compañero", lista_nombre[-1])
"""
b) Acceso y modificación
Crea una lista con 5 números enteros.
Reemplaza el tercer elemento por el valor 99.
Muestra la lista modificada.
"""
lista = [10, 20, 30, 40, 50]
lista[2] = 99
print(lista[0:])
"""
c) Slicing (rebanado)
Con la lista [10, 20, 30, 40, 50, 60, 70]:
Muestra los primeros 3 elementos.
Muestra los últimos 2 elementos.
Muestra los elementos del índice 2 al 4 inclusive.
"""
lista = [10, 20, 30, 40, 50, 60, 70 ]
print(lista[0:2])
print(lista[5:])
print(lista[2:4])
"""
d) Métodos de listas
Crea una lista de frutas: ["manzana", "banana", "pera"].
Agrega "uva" a la lista.
Pide al usuario que agregue otra fruta y añádela a la lista.
Elimina "banana" de la lista.
Muestra la lista final.
"""

frutas=["manzana", "banana", "pera"]
frutas.append("uva")
new_fruta=input(print("ingrese otra fruta:"))
frutas.append(new_fruta)
frutas.remove("banana")
print("La lista quedo asi:", frutas)

"""
e) Listas y bucles
Calcula la suma de los elementos de la lista [3, 6, 9, 12, 15] usando un bucle for.
"""
numeros=[3, 6, 9, 12, 15]
suma=0
for n in numeros:
    suma += n

print("la suma entre todos los numeros quedo: ", suma)


"""
f) Listas anidadas (matrices)
Listas anidadas (matrices)
        Declara una lista anidada (matriz) de 2 filas y 3 columnas con números enteros.
        Imprime el valor de la posición [1][2].
        Imprime también el valor de las posiciones [0][0] y [0][2].
"""

matriz = [[1, 2, 3], [4, 5, 6]]

print("Valor en [1][2]:", matriz[1][2])
print("Valor en [0][0]:", matriz[0][0])
print("Valor en [0][2]:", matriz[0][2])
