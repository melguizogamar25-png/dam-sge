import random  # Importamos el módulo 'random' para poder generar números aleatorios

temperaturas = []  # Lista vacía para almacenar las 7 temperaturas de la semana

while True:  # Bucle principal del menú
    print("\n--- ESTACIÓN METEOROLÓGICA DE NICO ---")  # Título
    print("1. Generar temperaturas de la semana (7 días)")  # Opción 1
    print("2. Mostrar informe meteorológico completo")  # Opción 2
    print("0. Salir")  # Salir
    op = input("Opción: ")  # Leemos la opción

    match op:  # Evaluamos la elección
        case "1":  # Generar temperaturas
            temperaturas.clear()  # Limpiamos datos de semanas anteriores
            t_min = float(input("Límite mínimo de temperatura (°C): "))  # Leemos el límite inferior
            t_max = float(input("Límite máximo de temperatura (°C): "))  # Leemos el límite superior
            for _ in range(7):  # Repetimos 7 veces (una por cada día de la semana)
                temp = round(random.uniform(t_min, t_max), 2)  # Generamos un decimal aleatorio entre t_min y t_max redondeado a 1 decimal
                temperaturas.append(temp)  # Guardamos la temperatura en la lista
            print("Temperaturas generadas correctamente.")  # Confirmamos

        case "2":  # Mostrar informe
            if not temperaturas:  # Verificamos si ya se han generado temperaturas
                print("Primero debes generar las temperaturas.")  # Avisamos si está vacía
            else:  # Si hay datos
                print("\n1. Temperaturas registradas:")  # Encabezado apartado 1
                suma = 0  # Acumulador para calcular la media
                max_t = temperaturas[0]  # Inicializamos la temperatura máxima con la del día 1
                dia_max = 1  # Guardamos que el día de la máxima es el 1
                min_t = temperaturas[0]  # Inicializamos la temperatura mínima con la del día 1
                dia_min = 1  # Guardamos que el día de la mínima es el 1

                for i in range(len(temperaturas)):  # Recorremos los 7 días por su índice (0 a 6)
                    print(f"   Día {i+1}: {temperaturas[i]} °C")  # Imprimimos el día (i+1) y su temperatura
                    suma += temperaturas[i]  # Sumamos la temperatura al acumulador
                    if temperaturas[i] > max_t:  # Si encontramos una temperatura mayor que 'max_t'
                        max_t = temperaturas[i]  # Actualizamos el valor máximo
                        dia_max = i + 1  # Guardamos qué día ocurrió (i+1)
                    if temperaturas[i] < min_t:  # Si encontramos una temperatura menor que 'min_t'
                        min_t = temperaturas[i]  # Actualizamos el valor mínimo
                        dia_min = i + 1  # Guardamos qué día ocurrió (i+1)

                media = suma / len(temperaturas)  # Calculamos la temperatura media semanal
                print(f"\n2. Temperatura media: {media:.2f} °C")  # Mostramos la media con 2 decimales
                print(f"3. Máxima: {max_t} °C (Día {dia_max}) | Mínima: {min_t} °C (Día {dia_min})")  # Mostramos máxima, mínima y sus días

                ordenadas = temperaturas.copy()  # Hacemos una copia de la lista para no perder el orden original de los días
                ordenadas.sort(reverse=True)  # Ordenamos la copia de mayor a menor (reverse=True)
                print(f"4. Ordenadas de mayor a menor: {ordenadas}")  # Mostramos la lista ordenada

                superiores = []  # Creamos una lista nueva para guardar las temperaturas por encima de la media
                for t in temperaturas:  # Recorremos cada temperatura
                    if t > media:  # Si supera la media calculada
                        superiores.append(t)  # La añadimos a la nueva lista

                print(f"5. Días por encima de la media: {len(superiores)}")  # La longitud de la nueva lista nos dice cuántos días fueron
                print(f"6. Lista de temperaturas superiores a la media: {superiores}")  # Mostramos la nueva lista

        case "0":  # Salir
            break  # Terminamos el bucle