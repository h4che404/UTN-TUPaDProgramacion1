numeros = []
for i in range(10):
            num = int(input("ingrese un nuemro"))
            numeros.append(num)
        suma_ultimos_cinco = sum(numeros[-5:])
        print(f"La suma de los últimos 5 números es: {suma_ultimos_cinco}")
            