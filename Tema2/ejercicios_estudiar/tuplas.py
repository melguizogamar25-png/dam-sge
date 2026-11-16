# Creamos una lista mutable que contiene TUPLAS inmutables.
# Cada tupla representa un registro fijo: (codigo_vuelo, destino, hora, pasajeros)
vuelos = [
    ("IB3412", "Madrid", "08:30", 145),
    ("VY2010", "Barcelona", "10:15", 172),
    ("FR8821", "Londres", "10:15", 189),
    ("UX4055", "Madrid", "14:00", 110),
    ("LH1123", "Frankfurt", "18:45", 160)
]

while True:
    print("\n" + "=" * 45)
    print("       PANEL DE CONTROL DE VUELOS")
    print("=" * 45)
    print("1. Mostrar parrilla completa de vuelos")
    print("2. Registrar nuevo vuelo")
    print("3. Buscar vuelos por destino")
    print("4. Vuelo con más y menos pasajeros (desempaquetado *)")
    print("5. Estadísticas de franja horaria (.count e .index)")
    print("6. Reprogramar hora de un vuelo (reconstrucción de tupla)")
    print("0. Salir")

    opcion = input("\nSelecciona una opción: ").strip()

    # --- OPCIÓN 1: DESEMPAQUETADO EN BUCLES ---
    if opcion == "1":
        # Formateamos cabeceras alineadas: <10 izquierda, >10 derecha
        print(f"\n{'CÓDIGO':<10} {'DESTINO':<15} {'HORA':<8} {'PASAJEROS':>10}")
        print("-" * 46)
        # En cada iteración, Python "desempaqueta" los 4 elementos de la tupla en 4 variables sueltas
        for codigo, destino, hora, pasajeros in vuelos:
            print(f"{codigo:<10} {destino:<15} {hora:<8} {pasajeros:>10}")

    # --- OPCIÓN 2: EMPAQUETADO DE TUPLA ---
    elif opcion == "2":
        cod = input("Código de vuelo (ej. IB1234): ").upper().strip()
        dest = input("Ciudad de destino: ").strip().capitalize()
        hora = input("Hora de salida (HH:MM): ").strip()
        pax = int(input("Número de pasajeros: "))
        # Los paréntesis () crean una nueva tupla inmutable con los 4 datos
        nuevo_vuelo = (cod, dest, hora, pax)
        # Añadimos la tupla completa a la lista 'vuelos'
        vuelos.append(nuevo_vuelo)
        print(f"Vuelo {nuevo_vuelo} registrado correctamente.")

    # --- OPCIÓN 3: FILTRADO DESEMPAQUETANDO ---
    elif opcion == "3":
        buscar_dest = input("Introduce el destino a buscar: ").strip().capitalize()
        encontrados = False  # Bandera booleana para saber si hallamos al menos uno
        for codigo, destino, hora, pasajeros in vuelos:
            if destino == buscar_dest:
                print(f" -> Vuelo {codigo} sale a las {hora} con {pasajeros} pasajeros.")
                encontrados = True
        if not encontrados:
            print(f"No hay vuelos programados hacia {buscar_dest}.")

    # --- OPCIÓN 4: ORDENACIÓN CON LAMBDA Y DESEMPAQUETADO CON ASTERISCO (*) ---
    elif opcion == "4":
        if len(vuelos) >= 2:
            # sorted() ordena las tuplas. key=lambda v: v[3] indica que ordene fijándose en el índice 3 (pasajeros)
            ordenados = sorted(vuelos, key=lambda v: v[3])
            # Desempaquetado extendido: 'menor' toma el 1º, 'mayor' el último, e 'intermedios' recoge el resto en una lista
            menor, *intermedios, mayor = ordenados
            # Accedemos a los campos de cada tupla por índice: [0] es código, [1] es destino, [3] es pasajeros
            print(f"Vuelo con MENOS pasajeros: {menor[0]} a {menor[1]} ({menor[3]} pax)")
            print(f"Vuelo con MÁS pasajeros:   {mayor[0]} a {mayor[1]} ({mayor[3]} pax)")
            print(f"Hay {len(intermedios)} vuelos en ocupación intermedia.")
        else:
            print("Hacen falta al menos 2 vuelos.")

    # --- OPCIÓN 5: MÉTODOS PROPIOS DE TUPLA (.count e .index) ---
    elif opcion == "5":
        # Expresión generadora dentro de tuple(): extrae el índice [2] (hora) de cada vuelo y forma una tupla pura
        tupla_horas = tuple(v[2] for v in vuelos)
        hora_consulta = input("Introduce hora a consultar (HH:MM): ").strip()
        # .count(x) cuenta cuántas veces aparece esa hora en la tupla
        cantidad = tupla_horas.count(hora_consulta)
        if cantidad > 0:
            # .index(x) devuelve la posición del primer vuelo que tiene esa hora
            primera_pos = tupla_horas.index(hora_consulta)
            print(f"Salen {cantidad} vuelo(s) a las {hora_consulta}.")
            # Usamos 'primera_pos' para indexar la lista original 'vuelos' y sacar código [0] y destino [1]
            print(f"El primero en parrilla es el {vuelos[primera_pos][0]} destino {vuelos[primera_pos][1]}.")
        else:
            print(f"No hay ningún vuelo a las {hora_consulta}.")

    # --- OPCIÓN 6: CÓMO "MODIFICAR" UN DATO INMUTABLE ---
    elif opcion == "6":
        cod_buscar = input("Introduce el código del vuelo a reprogramar: ").upper().strip()
        actualizado = False
        # Usamos enumerate() porque necesitamos el índice 'i' de la lista para poder sustituir la tupla entera
        for i, vuelo in enumerate(vuelos):
            # Desempaquetamos la tupla actual en 4 variables
            codigo, destino, hora_antigua, pasajeros = vuelo
            if codigo == cod_buscar:
                nueva_hora = input(f"Hora actual: {hora_antigua}. Introduce nueva hora (HH:MM): ").strip()
                # NO podemos hacer vuelo[2] = nueva_hora (daría TypeError).
                # En su lugar, creamos una TUPLA NUEVA y sobrescribimos la posición 'i' de la lista
                vuelos[i] = (codigo, destino, nueva_hora, pasajeros)
                print(f"Vuelo actualizado: {vuelos[i]}")
                actualizado = True
                break  # Cortamos el bucle porque los códigos de vuelo son únicos
        if not actualizado:
            print("Código de vuelo no encontrado.")

    elif opcion == "0":
        print("Cerrando torre de control...")
        break
    else:
        print("Opción no válida.")