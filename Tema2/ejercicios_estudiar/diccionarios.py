# Creamos un diccionario con llaves {}. Estructura: {clave_única: valor}
comandos = {
    "ls": "Lista los archivos y directorios de la ruta actual.",
    "cd": "Cambia el directorio de trabajo actual.",
    "grep": "Busca patrones de texto dentro de archivos.",
    "chmod": "Cambia los permisos de lectura, escritura y ejecución.",
    "mkdir": "Crea un nuevo directorio o carpeta."
}

while True:
    print("\n" + "=" * 48)
    print("      GLOSARIO INTERACTIVO DE COMANDOS")
    print("=" * 48)
    print("1. Agregar un nuevo comando")
    print("2. Imprimir glosario completo")
    print("3. Buscar comando (sin error si no existe)")
    print("4. Modificar definición de un comando")
    print("5. Añadir 2 comandos favoritos y fusionar")
    print("6. Borrar un comando (por nombre o el último)")
    print("7. Ordenar el diccionario alfabéticamente")
    print("8. Generar ficha de autoevaluación (fromkeys)")
    print("0. Salir")

    opcion = input("\nElige una opción: ").strip()

    # --- OPCIÓN 1: INSERCIÓN SEGURA CON .setdefault() ---
    if opcion == "1":
        cmd = input("Nombre del comando: ").lower().strip()
        # El operador 'in' comprueba si 'cmd' existe entre las CLAVES del diccionario (búsqueda O(1))
        if cmd in comandos:
            print(f"El comando '{cmd}' ya existe. Usa la opción 4 para modificarlo.")
        else:
            desc = input("Significado / uso del comando: ").strip()
            # .setdefault(clave, valor) inserta la pareja SOLO si la clave no existía previamente
            comandos.setdefault(cmd, desc)
            print(f"Comando '{cmd}' añadido con éxito.")

    # --- OPCIÓN 2: RECORRIDO DE CLAVE Y VALOR CON .items() ---
    elif opcion == "2":
        if not comandos:
            print("El diccionario está vacío.")
        else:
            print("\n--- LISTADO DE COMANDOS ---")
            # .items() devuelve una vista de tuplas (clave, valor) que desempaquetamos en 'cmd' y 'desc'
            for cmd, desc in comandos.items():
                print(f"• {cmd:<10} ---> {desc}")

    # --- OPCIÓN 3: BÚSQUEDA SIN EXCEPCIONES CON .get() ---
    elif opcion == "3":
        buscar = input("¿Qué comando quieres consultar?: ").lower().strip()
        # Si usáramos comandos[buscar] y no existiera, saltaría KeyError.
        # .get(clave, valor_por_defecto) devuelve el valor si existe, o el texto de aviso si no existe.
        resultado = comandos.get(buscar, "AVISO: Ese comando aún no está registrado en el glosario.")
        print(f"\n[{buscar}]: {resultado}")

    # --- OPCIÓN 4: ACTUALIZACIÓN DE VALOR POR CLAVE ---
    elif opcion == "4":
        cmd = input("¿Qué comando quieres modificar?: ").lower().strip()
        if cmd in comandos:
            # Accedemos directamente por clave entre corchetes para leer y sobrescribir el valor
            print(f"Definición actual: {comandos[cmd]}")
            nueva_desc = input("Nueva definición: ").strip()
            comandos[cmd] = nueva_desc
            print("Definición actualizada.")
        else:
            print("No se puede modificar porque el comando no existe.")

    # --- OPCIÓN 5: FUSIÓN DE DICCIONARIOS (|= o .update()) ---
    elif opcion == "5":
        print("Introduce tus 2 comandos favoritos:")
        favoritos = {}  # Creamos un diccionario auxiliar vacío
        # range(1, 3) genera los números 1 y 2 (el límite superior 3 no se incluye)
        for i in range(1, 3):
            c = input(f"  Comando favorito {i}: ").lower().strip()
            d = input(f"  Definición de '{c}': ").strip()
            favoritos[c] = d  # Guardamos cada par en el diccionario temporal
        # El operador |= (Python 3.9+) fusiona 'favoritos' dentro de 'comandos' in-place.
        # Si alguna clave ya existía, actualiza su valor; si no existía, la añade.
        comandos |= favoritos
        print("¡Tus comandos favoritos se han fusionado con el glosario principal!")

    # --- OPCIÓN 6: ELIMINACIÓN CON .pop() Y .popitem() ---
    elif opcion == "6":
        modo = input("¿Borrar por nombre (N) o eliminar el último añadido (U)?: ").upper().strip()
        if modo == "N":
            cmd = input("Nombre del comando a eliminar: ").lower().strip()
            # .pop(clave, None) borra la clave y devuelve su definición.
            # Poner None como segundo argumento evita que lance KeyError si la clave no existe.
            borrado = comandos.pop(cmd, None)
            if borrado is not None:
                print(f"Eliminado '{cmd}' (Decía: '{borrado}').")
            else:
                print("Ese comando no estaba en el diccionario.")
        elif modo == "U":
            if comandos:
                # .popitem() elimina y devuelve como tupla (clave, valor) el ÚLTIMO elemento insertado
                cmd_eliminado, desc_eliminada = comandos.popitem()
                print(f"Se ha eliminado el último registro: '{cmd_eliminado}' -> {desc_eliminada}")
            else:
                print("El diccionario ya está vacío.")

    # --- OPCIÓN 7: ORDENACIÓN POR CLAVE ---
    elif opcion == "7":
        # comandos.items() saca parejas (clave, valor).
        # sorted() las ordena alfabéticamente fijándose en el primer elemento de cada tupla (la clave).
        # dict() vuelve a convertir esa lista de tuplas ordenadas en un diccionario.
        comandos = dict(sorted(comandos.items()))
        print("Diccionario ordenado alfabéticamente:")
        for cmd, desc in comandos.items():
            print(f"  {cmd}: {desc}")

    # --- OPCIÓN 8: CREACIÓN MASIVA CON dict.fromkeys() ---
    elif opcion == "8":
        # dict.fromkeys(claves, valor_inicial) crea un diccionario nuevo tomando todas las claves
        # de comandos.keys() y asignándoles a TODAS el mismo valor por defecto.
        ficha_estudio = dict.fromkeys(comandos.keys(), "Pendiente de repasar")
        print("\n--- FICHA DE AUTOEVALUACIÓN GENERADA ---")
        for cmd, estado in ficha_estudio.items():
            print(f"[ ] {cmd:<10} -> {estado}")

    elif opcion == "0":
        print("¡Hasta la próxima sesión de terminal!")
        break
    else:
        print("Opción no reconocida.")