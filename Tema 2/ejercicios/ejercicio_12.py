n = int(input("¿Cuántas palabras va a introducir?: "))
palabras = []
for _ in range(n):
    palabras.append(input("Escriba una palabra: "))

palabras.sort()

print("La lista ordenada alfabéticamente es:", palabras)