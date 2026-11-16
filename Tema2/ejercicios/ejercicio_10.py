n = int(input("¿Cuántas palabras va a introducir?: "))
palabras = []
for _ in range(n):
    palabras.append(input("Escriba una palabra: "))

print("La lista creada es:", palabras)

sin_repetidos = []
for p in palabras:
    if p not in sin_repetidos:
        sin_repetidos.append(p)

print("La lista sin elementos repetidos es:", sin_repetidos)