notas = []
while True:
    entrada = input("Introduce una nota (0 a 10) o 'fin' para terminar: ")
    if entrada.lower() == "fin":
        break

    nota = float(entrada)
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota no válida. Debe estar entre 0 y 10.")

if len(notas) > 0:
    print("\n--- BOLETÍN DE CALIFICACIONES ---")
    for i, n in enumerate(notas, start=1):
        print(f"Nota {i}: {n:.2f}")

    media = sum(notas) / len(notas)
    mas_alta = max(notas)
    mas_baja = min(notas)

    suspensos = 0
    for n in notas:
        if n < 5:
            suspensos += 1

    print("-" * 33)
    print(f"Nota media: {media:.2f}")
    print(f"Nota más alta: {mas_alta:.2f}")
    print(f"Nota más baja: {mas_baja:.2f}")
    print(f"Número de suspensos: {suspensos}")
else:
    print("No se introdujeron notas.")