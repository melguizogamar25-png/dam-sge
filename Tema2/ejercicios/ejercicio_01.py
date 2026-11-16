numeros = []

while True:
    print("\n--- MENÚ EJERCICIO 1 ---")
    print("1. Introducir números en la lista")
    print("2. Reemplazar negativos por 0 y mostrar")
    print("0. Salir")
    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            numeros.clear()
            n = int(input("¿Cuántos números deseas introducir?: "))
            for i in range(n):
                num = float(input(f"Introduce el número {i+1}: "))
                numeros.append(num)
        case "2":
            if not numeros:
                print("La lista está vacía. Introduce datos primero.")
            else:
                print(f"Lista original: {numeros}")
                for i in range(len(numeros)):
                    if numeros[i] < 0:
                        numeros[i] = 0
                print(f"Lista modificada: {numeros}")
        case "0":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida.")