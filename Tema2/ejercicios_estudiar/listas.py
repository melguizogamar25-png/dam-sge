entrenamientos = [5.5, 10.2, 8.0, 12.5, 5.5, 12.5, 7.0, 15.0, 9.5]

salir = True
porcentaje = 100
mes = 30

while salir:
    print("\n-- MENÚ --")
    print("1 - Agregar un nuevo entrenamiento")
    print("2 - Corregir un entrenamiento")
    print("3 - Eliminar un entrenamiento")
    print("4 - Mostrar todos los entrenamientos")
    print("5 - Buscar el récord máximo")
    print("6 - Sumar una distancia extra")
    print("7 - Calcular estadísticas totales")
    print("8 - Ordenar la lista de mayor a menor")
    print("9 - Dividir la lista en dos")
    print("10 - Salir")
    opcion = input("Seleccione una opción del menú: ").strip()

    match opcion:
        case "1":
            nuevo_entrenamiento = float(input("Kilometraje del nuevo entrenamiento: "))
            entrenamientos.append(nuevo_entrenamiento)
            print("Entrenamiento añadido.")

        case "2":
            dia = int(input(f"Número de entrenamiento a modificar (1-{len(entrenamientos)}): ")) - 1
            if 0 <= dia < len(entrenamientos):
                accion = int(input("¿Poner a cero (0) o introducir una nueva distancia (1)?: "))
                if accion == 0:
                    entrenamientos[dia] = 0.0
                    print("Entrenamiento puesto a 0.0 km.")
                else:
                    nuevo_km = float(input("Nuevos kilómetros: "))
                    entrenamientos[dia] = nuevo_km
                    print("Distancia actualizada.")
            else:
                print("Día no válido.")

        case "3":
            op = int(input("Eliminar por su posición (0) o por el valor (1): "))
            if op == 0:
                dia = int(input(f"Día a eliminar (1 a {len(entrenamientos)}): ")) - 1
                if 0 <= dia < len(entrenamientos):
                    eliminado = entrenamientos.pop(dia)
                    print(f"Eliminado: {eliminado} km")
                else:
                    print("Día no válido.")
            elif op == 1:
                valor = float(input("Introduce los kilómetros exactos a borrar: "))
                if valor in entrenamientos:
                    entrenamientos.remove(valor)
                    print(f"Se ha borrado {valor} km")
                else:
                    print("No existe ese valor en la lista.")
            else:
                print("Opción no válida.")

        case "4":
            if not entrenamientos:
                print("No hay entrenamientos registrados.")
            else:
                print("\n--- HISTORIAL DE SALIDAS ---")
                for i, km in enumerate(entrenamientos, start=1):
                    print(f"Día {i:02d}: {km:6.2f} km")

        case "5":
            if entrenamientos:
                record = max(entrenamientos)
                veces = entrenamientos.count(record)
                primer_dia = entrenamientos.index(record) + 1
                print(f"Tu récord es de {record} km.")
                print(f"Lo has conseguido {veces} vez/veces, la primera fue el día {primer_dia}.")
            else:
                print("La lista está vacía.")

        case "6":
            dia = int(input(f"¿A qué día quieres sumarle km extra (1 - {len(entrenamientos)})?: ")) - 1
            if 0 <= dia < len(entrenamientos):
                extra = float(input("Kilómetros extra a sumar: "))
                entrenamientos[dia] += extra
                print(f"Nuevo total del día {dia + 1}: {entrenamientos[dia]:.2f} km")
            else:
                print("Día no válido.")

        case "7":
            if entrenamientos:
                total_km = sum(entrenamientos)
                media_km = total_km / len(entrenamientos)
                porcentaje_mes = (len(entrenamientos) / mes) * porcentaje
                print(f"Total acumulado: {total_km:.2f} km")
                print(f"Media por entrenamiento: {media_km:.2f} km")
                print(f"Has entrenado el {porcentaje_mes:.1f}% de los días del mes (sobre {mes} días).")
            else:
                print("No hay datos para calcular estadísticas.")

        case "8":
            entrenamientos.sort(reverse=True)
            print("Lista ordenada de mayor a menor:", entrenamientos)

        case "9":
            if len(entrenamientos) < 3:
                print("Necesitas al menos 3 entrenamientos.")
            else:
                ordenada = sorted(entrenamientos)
                tres_peores = ordenada[:3]
                restantes = ordenada[3:]
                print("Los 3 peores entrenamientos:", tres_peores)
                print("El resto de entrenamientos:", restantes)

        case "10":
            print("Saliendo, muchas gracias.")
            salir = False

        case _:
            print("Opción incorrecta, elige un número del 1 al 10.")
    


## EXPLICADO PASO A PASO ##

# Creamos la estructura principal: una lista mutable y ordenada de números decimales (float)
entrenamientos = [5.5, 10.2, 8.0, 12.5, 5.5, 12.5, 7.0, 15.0, 9.5]

# Iniciamos un bucle infinito que mantendrá el menú activo hasta ejecutar 'break'
while True:
    # Imprimimos la cabecera y las opciones del menú por pantalla
    print("\n" + "=" * 45)
    print("      GESTOR DE ENTRENAMIENTOS RUNNING")
    print("=" * 45)
    print("1. Agregar entrenamiento (al final o en posición)")
    print("2. Modificar o poner a 0.0 un entrenamiento")
    print("3. Eliminar entrenamiento (por posición o valor)")
    print("4. Mostrar todos los entrenamientos")
    print("5. Buscar récord máximo y cuántas veces se logró")
    print("6. Sumar kilómetros extra a un día concreto")
    print("7. Estadísticas (total, media y % días al mes)")
    print("8. Ordenar de mayor a menor y ver inversa")
    print("9. Dividir en dos listas (3 peores vs restantes)")
    print("0. Salir")

    # Leemos la opción como texto (str) y .strip() elimina espacios accidentales al inicio/final
    opcion = input("\nElige una opción: ").strip()

    # --- OPCIÓN 1: AÑADIR O INSERTAR ---
    if opcion == "1":
        # Convertimos el texto leído a decimal (float) para permitir medios kilómetros
        km = float(input("Introduce los kilómetros recorridos: "))
        # Preguntamos dónde guardarlo y pasamos la respuesta a mayúsculas con .upper()
        modo = input("¿Añadir al final (F) o insertar en una posición (P)?: ").upper()
        if modo == "P":
            # Restamos 1 porque el usuario cuenta desde 1, pero Python indexa desde 0
            pos = int(input(f"¿En qué día (1 a {len(entrenamientos) + 1})?: ")) - 1
            # Comprobamos que la posición esté dentro de los límites válidos (incluyendo el final)
            if 0 <= pos <= len(entrenamientos):
                # .insert(indice, valor) mete el dato en 'pos' y desplaza el resto a la derecha
                entrenamientos.insert(pos, km)
                print("Entrenamiento insertado correctamente.")
            else:
                print("Posición fuera de rango.")
        else:
            # .append(valor) añade el nuevo elemento al final de la lista en tiempo O(1)
            entrenamientos.append(km)
            print("Entrenamiento añadido al final.")

    # --- OPCIÓN 2: MODIFICAR POR ÍNDICE ---
    elif opcion == "2":
        # Pedimos el número de día y restamos 1 para obtener su índice real en la lista
        dia = int(input(f"Número de entrenamiento a modificar (1 a {len(entrenamientos)}): ")) - 1
        # Validamos que el índice exista (debe ser estrictamente menor que len)
        if 0 <= dia < len(entrenamientos):
            accion = input("¿Poner a cero (0) o introducir nueva distancia (N)?: ").upper()
            if accion == "0":
                # Sobrescribimos directamente la posición 'dia' con 0.0 (mutabilidad)
                entrenamientos[dia] = 0.0
                print(f"Día {dia + 1} puesto a 0.0 km.")
            else:
                nuevo_km = float(input("Nuevos kilómetros: "))
                # Reasignamos el nuevo valor en la posición exacta
                entrenamientos[dia] = nuevo_km
                print("Distancia actualizada.")
        else:
            print("Día no válido.")

    # --- OPCIÓN 3: ELIMINAR POR ÍNDICE O POR VALOR ---
    elif opcion == "3":
        tipo = input("¿Borrar por número de día (D) o por valor de km (V)?: ").upper()
        if tipo == "D":
            dia = int(input(f"Día a eliminar (1 a {len(entrenamientos)}): ")) - 1
            if 0 <= dia < len(entrenamientos):
                # .pop(indice) borra el elemento de esa posición Y nos lo devuelve para mostrarlo
                eliminado = entrenamientos.pop(dia)
                print(f"Eliminado el entrenamiento de {eliminado} km.")
            else:
                print("Día no válido.")
        elif tipo == "V":
            valor = float(input("Introduce los km exactos a borrar: "))
            # Comprobamos antes con 'in' si existe, porque .remove() lanza ValueError si no está
            if valor in entrenamientos:
                # .remove(valor) busca y borra solo la PRIMERA aparición de ese número
                entrenamientos.remove(valor)
                print(f"Se ha eliminado la primera aparición de {valor} km.")
            else:
                print("No existe ningún entrenamiento con esa distancia.")

    # --- OPCIÓN 4: RECORRER Y MOSTRAR ---
    elif opcion == "4":
        # En Python, una lista vacía [] se evalúa como False; 'not entrenamientos' es True si está vacía
        if not entrenamientos:
            print("No hay entrenamientos registrados.")
        else:
            print("\n--- HISTORIAL DE SALIDAS ---")
            # enumerate(..., start=1) genera parejas (contador_desde_1, elemento_de_la_lista)
            for i, km in enumerate(entrenamientos, start=1):
                # :02d rellena con un cero a la izquierda (01, 02); :6.2f reserva 6 espacios y 2 decimales
                print(f"Día {i:02d}: {km:6.2f} km")

    # --- OPCIÓN 5: MÁXIMO, CONTEO E ÍNDICE ---
    elif opcion == "5":
        if entrenamientos:
            # max() recorre la lista y devuelve el valor numérico más alto
            record = max(entrenamientos)
            # .count(valor) cuenta cuántas veces aparece exactamente 'record' en la lista
            veces = entrenamientos.count(record)
            # .index(valor) devuelve el índice de la primera vez que aparece; sumamos 1 para el día humano
            primer_dia = entrenamientos.index(record) + 1
            print(f"Tu récord es de {record} km.")
            print(f"Lo has conseguido {veces} vez/veces (la primera fue el día {primer_dia}).")
        else:
            print("La lista está vacía.")

    # --- OPCIÓN 6: ACTUALIZACIÓN ACUMULATIVA ---
    elif opcion == "6":
        dia = int(input(f"¿A qué día quieres sumarle km extra (1 a {len(entrenamientos)})?: ")) - 1
        if 0 <= dia < len(entrenamientos):
            extra = float(input("Kilómetros extra a sumar: "))
            # += lee el valor actual de entrenamientos[dia], le suma 'extra' y guarda el resultado
            entrenamientos[dia] += extra
            print(f"Nuevo total del día {dia + 1}: {entrenamientos[dia]:.2f} km.")
        else:
            print("Día no válido.")

    # --- OPCIÓN 7: OPERACIONES MATEMÁTICAS GLOBALES ---
    elif opcion == "7":
        if entrenamientos:
            # sum() suma todos los elementos numéricos de la lista
            total_km = sum(entrenamientos)
            # len() devuelve la cantidad total de elementos en la lista
            media_km = total_km / len(entrenamientos)
            porcentaje_mes = (len(entrenamientos) / 30) * 100
            print(f"Total acumulado: {total_km:.2f} km")
            print(f"Media por entrenamiento: {media_km:.2f} km")
            print(f"Has entrenado el {porcentaje_mes:.1f}% de los días del mes (sobre 30 días).")
        else:
            print("No hay datos para calcular estadísticas.")

    # --- OPCIÓN 8: ORDENACIÓN IN-PLACE Y SLICING INVERSO ---
    elif opcion == "8":
        # .sort(reverse=True) ordena la lista ORIGINAL de mayor a menor (no devuelve nada, modifica la lista)
        entrenamientos.sort(reverse=True)
        print("Lista ordenada de mayor a menor:", entrenamientos)
        # [::-1] es un slicing con paso -1: crea una COPIA invertida sin tocar la original
        print("Vista invertida (menor a mayor) sin modificar:", entrenamientos[::-1])

    # --- OPCIÓN 9: ORDENACIÓN NO DESTRUCTIVA Y SLICING ---
    elif opcion == "9":
        if len(entrenamientos) >= 3:
            # sorted() crea una NUEVA lista ordenada de menor a mayor, dejando 'entrenamientos' intacta
            ordenada = sorted(entrenamientos)
            # [:3] extrae desde el índice 0 hasta el 2 (los 3 primeros elementos)
            tres_peores = ordenada[:3]
            # [3:] extrae desde el índice 3 hasta el final de la lista
            restantes = ordenada[3:]
            print("Los 3 peores entrenamientos:", tres_peores)
            print("El resto de entrenamientos:", restantes)
        else:
            print("Necesitas al menos 3 entrenamientos para dividir la lista.")

    # --- OPCIÓN 0: SALIDA ---
    elif opcion == "0":
        print("¡Buen entrenamiento! Saliendo...")
        break  # Sale inmediatamente del bucle while True
    else:
        print("Opción incorrecta.")


        
 
