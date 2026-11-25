f_texto = open('Tema3/MelguizoGarcíaMarta_EjerciciosFicheros/ejercicio04/texto.txt', 'r')
f_numerado = open('Tema3/MelguizoGarcíaMarta_EjerciciosFicheros/ejercicio04/numerado.txt', 'w')

numero = 1
for linea in f_texto:
    f_numerado.write(f"{numero}. {linea}")
    numero += 1

f_texto.close()
f_numerado.close()