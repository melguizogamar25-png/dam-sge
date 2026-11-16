n1 = int(input("¿Cuántas palabras tiene la primera lista?: "))
lista1 = []
for _ in range(n1):
    lista1.append(input("Escriba una palabra para la primera lista: "))

n2 = int(input("¿Cuántas palabras tiene la segunda lista?: "))
lista2 = []
for _ in range(n2):
    lista2.append(input("Escriba una palabra para la segunda lista: "))

print("Primera lista:", lista1)
print("Segunda lista:", lista2)

for palabra in lista2:
    while palabra in lista1:
        lista1.remove(palabra)

print("La primera lista queda ahora:", lista1)