#Crea un programa que añada la fecha y hora actuales al final de un fichero.

from datetime import datetime

ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

f = open('Tema3/MelguizoGarcíaMarta_EjerciciosFicheros/ejercicio02/registro.txt', 'a')
f.write(ahora + "\n")
f.close()