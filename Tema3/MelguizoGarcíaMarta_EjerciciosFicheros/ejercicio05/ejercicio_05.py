f_datos = open('Tema3/MelguizoGarcíaMarta_EjerciciosFicheros/ejercicio05/datos.txt', 'r')
lineas = f_datos.readlines()
f_datos.close()

lineas.reverse()

f_invertido = open('Tema3/MelguizoGarcíaMarta_EjerciciosFicheros/ejercicio05/invertido.txt', 'w')
for linea in lineas:
    # Nos aseguramos de que si la última línea no tenía salto de línea, no se pegue a la siguiente
    if not linea.endswith('\n'):
        linea += '\n'
    f_invertido.write(linea)

f_invertido.close()