#Escribe un programa que cuente cuántas líneas NO vacías contiene un fichero 'entrada.txt' que
#tenga varias líneas de prueba.

contador = 0

f = open('Tema3/MelguizoGarcíaMarta_EjerciciosFicheros/ejercicio01/entrada.txt')

for linea in f:
    if linea.strip():
        contador += 1

f.close()

print(f"El fichero tiene {contador} líneas no vacías.")


