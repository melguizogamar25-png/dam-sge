n1 = int(input("¿Cuántas palabras tiene la primera lista?: "))
lista1 = []
for _ in range(n1):
    lista1.append(input("Primera lista - Palabra: "))

n2 = int(input("¿Cuántas palabras tiene la segunda lista?: "))
lista2 = []
for _ in range(n2):
    lista2.append(input("Segunda lista - Palabra: "))

set1 = set(lista1)
set2 = set(lista2)

en_ambas = list(set1 & set2)

solo_primera = list(set1 - set2)

solo_segunda = list(set2 - set1)

todas = list(set1 | set2)

print("\nResultados (sin repeticiones):")
print("Palabras que aparecen en las dos listas:", en_ambas)
print("Palabras en la primera pero no en la segunda:", solo_primera)
print("Palabras en la segunda pero no en la primera:", solo_segunda)
print("Todas las palabras que aparecen en ambas listas:", todas)