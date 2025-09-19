'''
a) Creación de listas 
Crea una lista con los nombres de 5 compañeros de clase.
Muestra en pantalla el primer y el último elemento de la lista.
'''

lista_companeros = ["juan", "juancito", "NAHUEL", "joako", "agus"]
print(lista_companeros[0])
print(lista_companeros[-1])

'''
b) Acceso y modificación
Crea una lista con 5 números enteros.
Reemplaza el tercer elemento por el valor 99.
Muestra la lista modificada.
'''

lista_nume = [1,2,3,4,5]
lista_nume[2] = 99
print(lista_nume)

'''
c) Slicing (rebanado)
Con la lista [10, 20, 30, 40, 50, 60, 70]:
Muestra los primeros 3 elementos.
Muestra los últimos 2 elementos.
Muestra los elementos del índice 2 al 4 inclusive.
'''

numeros = [10,20,30,40,50,60,70]
print(numeros[0:3])
print(numeros[-2:])
print(numeros[2:5])


'''
d) Métodos de listas
Crea una lista de frutas: ["manzana", "banana", "pera"].
Agrega "uva" a la lista.
Pide al usuario que agregue otra fruta y añádela a la lista.
Elimina "banana" de la lista.
Muestra la lista final.
'''

frutas = ["manzana", "banana", "pera"]
frutas.append("uva")
nueva_fruta = input("Ingresa otra fruta: ")
frutas.append(nueva_fruta)
frutas.remove("banana")
print(frutas)

'''
e) Listas y bucles
Calcula la suma de los elementos de la lista [3, 6, 9, 12, 15] usando un bucle for.
'''

numeros = [3,6,9,12,15]
suma = 0
for numero in numeros:
    suma += numero
print(suma)

'''
f) Listas anidadas (matrices)
Listas anidadas (matrices)
       Declara una lista anidada (matriz) de 2 filas y 3 columnas con números           enteros.
       Imprime el valor de la posición [1][2].
      Imprime también el valor de las posiciones [0][0] y [0][2].
'''

listas = [[1, 2, 3],[4, 5, 6]]
print(listas[1][2])
print(listas[0][2], listas[0][0])