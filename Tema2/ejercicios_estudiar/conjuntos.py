# set([...]) convierte una lista en un conjunto: elimina automáticamente duplicados
# y almacena los elementos sin orden fijo (tabla hash) para búsquedas instantáneas.
ciberseguridad = set(["ana", "carlos", "beatriz", "ana", "david", "elena"])
ia = set(["carlos", "elena", "fernando", "gabriela", "fernando", "hugo"])

while True:
    print("\n" + "=" * 50)
    print("    CONTROL DE INSCRIPCIONES A TALLERES")
    print("=" * 50)
    print("1. Inscribir alumno en un taller")
    print("2. Dar de baja a un alumno")
    print("3. Mostrar inscritos únicos por taller")
    print("4. Informe de cruces (Unión, Intersección, Diferencias)")
    print("5. Comprobar grupo VIP (Subconjunto / Disjunto)")
    print("0. Salir")

    opcion = input("\nElige una opción: ").strip()

    # --- OPCIÓN 1: INSERCIÓN SIN DUPLICADOS CON .add() ---
    if opcion == "1":
        nombre = input("Nombre del alumno: ").lower().strip()
        taller = input("¿En qué taller inscribir? (C = Ciberseguridad / I = IA / A = Ambos): ").upper().strip()
        if taller == "C":
            # .add(x) mete el elemento en el conjunto. Si ya estaba dentro, Python lo ignora sin dar error.
            ciberseguridad.add(nombre)
            print(f"'{nombre}' añadido a Ciberseguridad (si ya estaba, no se duplica).")
        elif taller == "I":
            ia.add(nombre)
            print(f"'{nombre}' añadido a IA.")
        elif taller == "A":
            ciberseguridad.add(nombre)
            ia.add(nombre)
            print(f"'{nombre}' añadido a ambos talleres.")
        else:
            print("Taller no válido.")

    # --- OPCIÓN 2: BORRADO SEGURO CON .discard() ---
    elif opcion == "2":
        nombre = input("Nombre del alumno a dar de baja: ").lower().strip()
        taller = input("¿De qué taller dar de baja? (C = Ciberseguridad / I = IA): ").upper().strip()
        if taller == "C":
            if nombre in ciberseguridad:
                # .discard(x) elimina 'x' si existe; a diferencia de .remove(x), NUNCA lanza KeyError si falta.
                ciberseguridad.discard(nombre)
                print(f"'{nombre}' eliminado de Ciberseguridad.")
            else:
                print(f"'{nombre}' no estaba en Ciberseguridad.")
        elif taller == "I":
            if nombre in ia:
                ia.discard(nombre)
                print(f"'{nombre}' eliminado de IA.")
            else:
                print(f"'{nombre}' no estaba en IA.")

    # --- OPCIÓN 3: ORDENACIÓN DE UN CONJUNTO PARA MOSTRARLO ---
    elif opcion == "3":
        # Como los sets NO tienen orden ni método .sort(), usamos sorted(conjunto)
        # que devuelve una LISTA ordenada alfabéticamente para imprimirla limpia.
        print(f"\nCiberseguridad ({len(ciberseguridad)} únicos):", sorted(ciberseguridad))
        print(f"Inteligencia Artificial ({len(ia)} únicos):", sorted(ia))

    # --- OPCIÓN 4: OPERACIONES MATEMÁTICAS DE CONJUNTOS ---
    elif opcion == "4":
        # UNIÓN (|): todos los elementos que están en ciberseguridad O en ia (sin repetir)
        todos = ciberseguridad | ia
        # INTERSECCIÓN (&): solo los elementos que están en ciberseguridad Y en ia a la vez
        ambos = ciberseguridad & ia
        # DIFERENCIA (-): elementos que están en el primer conjunto pero NO en el segundo
        solo_ciber = ciberseguridad - ia
        solo_ia = ia - ciberseguridad
        # DIFERENCIA SIMÉTRICA (^): elementos que están en uno de los dos, pero NO en ambos
        solo_uno = ciberseguridad ^ ia

        print("\n--- INFORME DE CRUCES DE ASISTENCIA ---")
        print(f"• Total alumnos únicos (Unión):            {len(todos)} -> {sorted(todos)}")
        print(f"• Van a AMBOS talleres (Intersección):     {len(ambos)} -> {sorted(ambos)}")
        print(f"• Van SOLO a Ciberseguridad (Diferencia):  {len(solo_ciber)} -> {sorted(solo_ciber)}")
        print(f"• Van SOLO a IA (Diferencia):              {len(solo_ia)} -> {sorted(solo_ia)}")
        print(f"• Van SOLO a uno de los dos (Dif. Sim.):   {len(solo_uno)} -> {sorted(solo_uno)}")

    # --- OPCIÓN 5: SET COMPREHENSION Y RELACIONES LÓGICAS ---
    elif opcion == "5":
        entrada = input("Introduce nombres VIP separados por comas: ").lower()
        # SET COMPREHENSION: {expresion for item in iterable if condicion}
        # Trocea el texto por comas (.split(",")), limpia espacios (.strip()) y filtra vacíos
        grupo_vip = {nombre.strip() for nombre in entrada.split(",") if nombre.strip()}
        todos_inscritos = ciberseguridad | ia

        print(f"\nGrupo VIP analizado: {grupo_vip}")
        # .issubset(otro) devuelve True si TODOS los elementos de grupo_vip están dentro de todos_inscritos
        if grupo_vip.issubset(todos_inscritos):
            print("-> Todos los miembros del grupo VIP están inscritos en algún taller.")
        # .isdisjoint(otro) devuelve True si grupo_vip y todos_inscritos NO tienen ni un elemento en común
        elif grupo_vip.isdisjoint(todos_inscritos):
            print("-> Ningún miembro del grupo VIP está inscrito todavía.")
        else:
            # Restamos conjuntos para saber exactamente qué alumnos VIP faltan por apuntarse
            faltan = grupo_vip - todos_inscritos
            print(f"-> Solo algunos están inscritos. Faltan por apuntarse: {faltan}")

    elif opcion == "0":
        print("Cerrando gestor de talleres...")
        break
    else:
        print("Opción incorrecta.")