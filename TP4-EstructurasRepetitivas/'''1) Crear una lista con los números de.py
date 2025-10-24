'''1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range.'''
lista = [x for x in range(1, 101) if x % 4 == 0]
print(lista)
print("-------")
'''2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!'''

lista = ["automóviles", "motos", "bicicletas", "electricidad", "juegos"]
print(lista(-2))
print("-------")

