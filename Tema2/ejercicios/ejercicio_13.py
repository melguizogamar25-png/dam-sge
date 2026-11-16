abecedario = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "ñ",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

resultado = []

for i in range(len(abecedario)):
    posicion_humana = i + 1
    if posicion_humana % 3 != 0:
        resultado.append(abecedario[i])

print("Abecedario resultante:", resultado)