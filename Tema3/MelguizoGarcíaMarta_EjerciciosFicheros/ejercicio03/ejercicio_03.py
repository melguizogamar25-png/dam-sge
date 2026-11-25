f_origen = open('Tema3/MelguizoGarcíaMarta_EjerciciosFicheros/ejercicio03/origen.txt', 'r')
contenido = f_origen.read()
f_origen.close()

f_copia = open('Tema3/MelguizoGarcíaMarta_EjerciciosFicheros/ejercicio03/copia.txt', 'w')
f_copia.write(contenido)
f_copia.close()