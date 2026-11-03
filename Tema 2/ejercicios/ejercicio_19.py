precios = []
print("--- INGRESO DE PRECIOS DE ARTÍCULOS ---")
for i in range(5):
    precio = float(input(f"Precio del Artículo {i + 1}: "))
    precios.append(precio)

cantidades = []
print("\n--- INGRESO DE CANTIDADES VENDIDAS ---")
for i in range(4):
    print(f"\nSucursal {i + 1}:")
    ventas_sucursal = []
    for j in range(5):
        cant = int(input(f"  Cantidad vendida del Artículo {j + 1}: "))
        ventas_sucursal.append(cant)
    cantidades.append(ventas_sucursal)

print("\n" + "=" * 50)
print(" -- INFORME DE VENTAS -- ")
print("=" * 50)

print("\n1. Cantidades totales vendidas por artículo:")
cantidades_totales_articulos = []
for j in range(5):
    total_articulo = 0
    for i in range(4):
        total_articulo += cantidades[i][j]
    cantidades_totales_articulos.append(total_articulo)
    print(f"   - Artículo {j + 1}: {total_articulo} unidades")

total_articulos_suc2 = sum(cantidades[1])
print(f"\n2. Total de artículos vendidos en la Sucursal 2: {total_articulos_suc2} unidades")

art3_suc1 = cantidades[0][2]
print(f"\n3. Cantidad vendida del Artículo 3 en la Sucursal 1: {art3_suc1} unidades")

recaudacion_sucursales = []
recaudacion_total_empresa = 0

print("\n4. Recaudación total por sucursal:")
for i in range(4):
    recaudacion_suc = 0
    for j in range(5):
        recaudacion_suc += cantidades[i][j] * precios[j]
    recaudacion_sucursales.append(recaudacion_suc)
    recaudacion_total_empresa += recaudacion_suc
    print(f"   - Sucursal {i + 1}: {recaudacion_suc:.2f} €")

print(f"\n5. Recaudación total de la empresa: {recaudacion_total_empresa:.2f} €")

max_recaudacion = max(recaudacion_sucursales)
sucursal_mayor = recaudacion_sucursales.index(max_recaudacion) + 1

print(f"\n6. Sucursal de mayor recaudación: Sucursal {sucursal_mayor} (con {max_recaudacion:.2f} €)")