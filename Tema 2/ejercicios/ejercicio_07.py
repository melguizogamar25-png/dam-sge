n = int(input("¿Cuántas palabras va a introducir?: "))
palabras = []
for _ in range(n):
    palabras.append(input("Escriba una palabra: "))

print("La lista creada es:", palabras)
eliminar = input("Palabra a eliminar: ")

while eliminar in palabras:
    palabras.remove(eliminar)

print("La lista es ahora:", palabras)