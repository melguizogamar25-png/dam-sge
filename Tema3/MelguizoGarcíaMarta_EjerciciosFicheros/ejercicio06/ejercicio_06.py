import random

ruta = 'Tema3/MelguizoGarcíaMarta_EjerciciosFicheros/ejercicio06/fichero.txt'

f = open(ruta, 'r')
contenido = f.read()
f.close()

palabras = contenido.split()
lineas = contenido.splitlines()

# 1. La palabra de mayor longitud
mas_larga = max(palabras, key=len)
print("La palabra más larga es:", mas_larga)

# 2. Las veces que aparece una palabra
buscar = input("Introduce la palabra a buscar: ").lower()
palabras_minus = contenido.lower().split()
print(f"La palabra '{buscar}' aparece {palabras_minus.count(buscar)} veces.")

# 3. Leer una línea aleatoria del fichero
print("Línea aleatoria:", random.choice(lineas))

# 4. Funcionalidad extra 1: Contar el total de palabras
print("Total de palabras en el fichero:", len(palabras))

# 5. Funcionalidad extra 2: Mostrar el contenido en mayúsculas
print("\nContenido en mayúsculas:")
print(contenido.upper())