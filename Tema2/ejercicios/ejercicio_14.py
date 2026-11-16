palabra = input("Introduce una palabra: ").lower()

if palabra == palabra[::-1]:
    print(f"La palabra '{palabra}' ES un palíndromo.")
else:
    print(f"La palabra '{palabra}' NO es un palíndromo.")