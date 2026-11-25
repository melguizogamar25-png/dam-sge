ruta = 'Tema3/MelguizoGarcíaMarta_EjerciciosFicheros/ejercicio07/clientes.txt'
f = open(ruta, 'a')

continuar = "s"
while continuar.lower() == "s":
    nombre = input("Nombre: ")
    apellido1 = input("Apellido1: ")
    apellido2 = input("Apellido2: ")
    edad = input("Edad: ")

    f.write(f"Nombre:\t\t{nombre}\n")
    f.write(f"Apellido1:\t{apellido1}\n")
    f.write(f"Apellido2:\t{apellido2}\n")
    f.write(f"Edad:\t\t{edad}\n")

    continuar = input("¿Quieres añadir otro cliente? (s/n): ")

f.close()

# Mostramos el contenido final como en la captura
f = open(ruta, 'r')
print("\nEl contenido del fichero clientes.txt es:")
print(f.read())
f.close()