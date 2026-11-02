numeros = [12, -5, 8, -1, 0, -3, 15]

for i in range(len(numeros)):
    if numeros[i] < 0:
        numeros[i] = 0

print("Lista con negativos reemplazados:", numeros)