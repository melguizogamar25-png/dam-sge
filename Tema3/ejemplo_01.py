#Como leer en un fichero
f = open('Tema3/archivo.txt')
f2 = open('Tema3/files/archivo2.txt')

archivo = f.read() #Archivo entero
archivo2 = f2.readlines() #Por lineas devolviendo una lista

print(archivo)
print(archivo2)


f.seek(0) #Esto hace que podamos volver al principio del fichero
for linea in f:#Lectura linea a linea
    print(linea)