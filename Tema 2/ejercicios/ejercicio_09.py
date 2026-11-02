n = int(input("¿Cuántas palabras va a introducir?: "))
original = []
for _ in range(n):
    original.append(input("Escriba una palabra: "))

inversa = original[::-1]  

print("Lista original:", original)
print("Lista invertida:", inversa)