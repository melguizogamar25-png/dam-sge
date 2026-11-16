recaudaciones = []


#Agregar
cantidad = float(input("Cantidad recaudada: "))
recaudaciones.append(cantidad)
print(f"Añadida como dia {len(recaudaciones)}")

#Poner a cero un
dia = int(input(f"Que dia? (1-{len(recaudaciones)})"))
if 1 <= dia <= len(recaudaciones):
    recaudaciones[dia -1] = 0.0
    print(f"Día {dia} puesto a cero")

#Imprimir toda la lista

#Dia que mas he ganado 
if len(recaudaciones) == 0:
    print("No hay")
else:
    mayor = recaudaciones[0]
    for r in recaudaciones:
        if r > mayor:
            mayor = r
    veces = recaudaciones.count(mayor)

#Caso 5
dia = int(input(f"Que dia? (1-{len(recaudaciones)})"))
if 1 <= dia <= len(recaudaciones):
    extra = float(input("Cantidad extra: "))
    recaudaciones[dia -1] += extra
    print(f"Dia {dia} ahora:")
else:
    print("No existe")


#Para ordenar la lista un sort y para mayor a menor reverse= True


#Media
if len(recaudaciones) == 0:
    print("NO")
else:
    total = 0
    for r in recaudaciones:
        total += r
    media = total/len(recaudaciones)
    #Imprimir la media a dos decimales

#case 9
porcentaje = len(recaudaciones) /  30 * 100
if porcentaje > 100:
    porcentaje = 100

#case 10
if len(recaudaciones) < 5:
    print("Falta al menos 5")
else:
    ordenada = sorted(recaudaciones)
    menos = ordenada[:5]
    restantes = ordenada[5:]
    print(f"5 menores {menos}")
    