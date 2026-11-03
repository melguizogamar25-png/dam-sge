n_conductores = int(input("¿Cuántos conductores tiene la empresa?: "))

nombres = []
kms = []
total_kms = []

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for i in range(n_conductores):
    nombre = input(f"\nNombre del conductor {i + 1}: ")
    nombres.append(nombre)
    
    kms_conductor = []
    print(f"Introduce los kilómetros recorridos por {nombre}:")
    for dia in dias_semana:
        km = float(input(f"  - {dia}: "))
        kms_conductor.append(km)
    
    kms.append(kms_conductor)


for kms_conductor in kms:
    total_kms.append(sum(kms_conductor))

print("\n" + "=" * 45)
print("     RESUMEN DE KILÓMETROS POR CONDUCTOR     ")
print("=" * 45)

for i in range(n_conductores):
    print(f"Conductor: {nombres[i]:<15} | Total Kms: {total_kms[i]:.2f} km")