n = int(input("¿Cuántas palabras va a introducir?: "))
palabras = []
for _ in range(n):
    palabras.append(input("Escriba una palabra: "))

print("La lista creada es:", palabras)
buscar = input("Sustituir la palabra: ")
reemplazo = input("por la palabra: ")

for i in range(len(palabras)):
    if palabras[i] == buscar:
        palabras[i] = reemplazo

print("La lista es ahora:", palabras)