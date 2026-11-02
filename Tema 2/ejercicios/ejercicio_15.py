cadena = input("Introduce una palabra o frase: ").lower()

letras = []
es_isograma = True

for caracter in cadena:
    if caracter.isalpha():
        if caracter in letras:
            es_isograma = False
            break
        letras.append(caracter)

if es_isograma:
    print(f"'{cadena}' ES un isograma.")
else:
    print(f"'{cadena}' NO es un isograma.")