n = int(input("¿Cuántas palabras va a introducir?: "))
palabras = []

for _ in range(n):
    p = input("Escriba una palabra: ")
    palabras.append(p)

print("La lista creada es:", palabras)