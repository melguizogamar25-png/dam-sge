lista = ["Python", "Java", "C++", "JavaScript"]

opcion = ""
while opcion != "7":
    print("\n--- MENÚ FUNCIONALIDADES DE LISTAS ---")
    print("1. Buscar un elemento (Read)")
    print("2. Insertar al final (Create)")
    print("3. Insertar en una posición concreta (Create)")
    print("4. Borrar elemento por valor (Delete)")
    print("5. Borrar elemento por índice/extracción (Delete)")
    print("6. Mostrar lista actual")
    print("7. Salir y pasar al ejercicio práctico")

    opcion = input("Elige una opción (1-7): ")

    if opcion == "1":
        elem = input("Elemento a buscar: ")
        if elem in lista:
            idx = lista.index(elem)
            print(f"El elemento '{elem}' existe en la posición {idx}.")
        else:
            print(f"El elemento '{elem}' no está en la lista.")

    elif opcion == "2":
        elem = input("Elemento a añadir al final: ")
        lista.append(elem)
        print(f"'{elem}' añadido correctamente.")

    elif opcion == "3":
        elem = input("Elemento a insertar: ")
        pos = int(input("Posición (índice): "))
        lista.insert(pos, elem)
        print(f"'{elem}' insertado en la posición {pos}.")

    elif opcion == "4":
        elem = input("Elemento a borrar: ")
        if elem in lista:
            lista.remove(elem)
            print(f"'{elem}' ha sido eliminado.")
        else:
            print(f"'{elem}' no se encuentra en la lista.")

    elif opcion == "5":
        pos = int(input("Índice a extraer/borrar: "))
        if 0 <= pos < len(lista):
            extraido = lista.pop(pos)
            print(f"Elemento '{extraido}' extraído y borrado.")
        else:
            print("Índice fuera de rango.")

    elif opcion == "6":
        print("Lista actual:", lista)

    elif opcion == "7":
        print("Saliendo del menú explicativo...\n")

    else:
        print("Opción inválida. Intenta de nuevo.")

# ENUNCIADO REAL:
# Un supermercado gestiona su lista de la compra de reposición urgente.
# El encargado desea eliminar un producto agotado de la lista. Para evitar
# errores al borrar, primero debe comprobar si el producto existe mediante
# la búsqueda y, si está en la lista, proceder a su borrado por valor.

print("--- SUPERMERCADO ---")
inventario_urgente = ["Leche", "Pan", "Huevos", "Aceite", "Manzanas"]
print("Inventario actual:", inventario_urgente)

producto_a_borrar = input(
    "Ingrese el producto que desea eliminar del inventario: "
)

if producto_a_borrar in inventario_urgente:
    inventario_urgente.remove(producto_a_borrar)
    print(
        f"El producto '{producto_a_borrar}' ha sido encontrado y eliminado."
    )
else:
    print(
        f"El producto '{producto_a_borrar}' no se encuentra en la lista de reposición."
    )

print("Inventario actualizado:", inventario_urgente)