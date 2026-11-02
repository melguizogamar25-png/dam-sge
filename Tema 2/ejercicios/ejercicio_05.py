n = int(input("¿Cuántas palabras va a introducir?: "))
palabras = []
for _ in range(n):
    palabras.append(input("Escriba una palabra: "))

print("La lista creada es:", palabras)
buscar = input("Recuento. Diga la palabra a buscar: ")
cantidad = palabras.count(buscar)

print(f"La palabra '{buscar}' aparece {cantidad} vez/veces en la lista.")