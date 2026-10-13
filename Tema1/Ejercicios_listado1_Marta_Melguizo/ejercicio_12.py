import random 
numero_secreto = random.randint(0,10)
intentos = 0

while intentos < 3:
    numero = int(input("Adivina el número entre 0 y 10: "))
    intentos += 1
    if numero == numero_secreto:
        print("Has acertado")
        intentos = 3
    else:
        print("No has acertado")

if numero != numero_secreto:
    print("El número era: ", numero_secreto)
    