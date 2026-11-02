import random

min_lim = float(input("Introduce el límite inferior de temperatura: "))
max_lim = float(input("Introduce el límite superior de temperatura: "))

temperaturas = []
for _ in range(7):
    temp = random.uniform(min_lim, max_lim)
    temperaturas.append(round(temp, 2))

print("\n--- INFORME ---")
print("Temperaturas registradas de la semana:", temperaturas)


media = sum(temperaturas) / len(temperaturas)
print(f"Temperatura media de la semana: {media:.2f}°C")

max_temp = max(temperaturas)
min_temp = min(temperaturas)

dia_max = temperaturas.index(max_temp) + 1
dia_min = temperaturas.index(min_temp) + 1

print(f"Temperatura máxima: {max_temp}°C (ocurrió el Día {dia_max})")
print(f"Temperatura mínima: {min_temp}°C (ocurrió el Día {dia_min})")

temperaturas_ordenadas = sorted(temperaturas, reverse=True)
print("Temperaturas ordenadas de mayor a menor:", temperaturas_ordenadas)

superiores_media = [t for t in temperaturas if t > media]
num_dias_superiores = len(superiores_media)

print(f"Número de días por encima de la media: {num_dias_superiores}")
print("Lista de temperaturas superiores a la media:", superiores_media)