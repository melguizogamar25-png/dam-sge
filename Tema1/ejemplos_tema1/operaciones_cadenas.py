#Combinar cadenas
cadena1 = 'Hola'
cadena2 = 'Mundo'
print(cadena1 + ' ' + cadena2)

#Repetir cadenas (pagina 85)
risa = 'PUAJ'
print (risa * 4) #Podemos repetir las cadenas multiplicandolo

#Obtener un caracter
saludo = 'Hola Mundo'
print(saludo [3]) #Es como un indice en los arrays de java
print(saludo [-2]) #tambien esta en negativo empezaria en el -1 desde el final hasta el principio

#Trocear una cadena
troce = 'Agua pasada no lleva molino'
print(troce[:])
print(troce[12:])
print(troce[:11])
print(troce[5:11])
print(troce[5:11:2])

#Longitud de una cadena
long = 'Necesito saber cual es la longitud de esta cadena'
print(len(long))

#Pertenencia de un elemento
text = 'Mas vale malo conocido que bueno por conocer'
print('malo' in text)
print('feo' in text)

#Dividir una cadena
div = 'No hay mal que por bien no venga'
print(div.split())

#Limpiar cadenas
limpiar = '\n\t \n 48374983274832 \n\n\t \t \n'
print(limpiar.strip()) #Puedes tambien borrar la parte de la izquierda, de la derecha y un caracter special como \n

#realizar busquedas
busq = '''Quizás porque mi niñez, Sigue jugando en tu playa'''
print(busq.startswith('Quizás'))

#Reemplazar elementos
reem = 'Quien mal anda mal acaba'
print(reem.replace('mal', 'bien')) #Sustituye la primera cadena por la segunda, si no encuentra la primera cadena no hace nada

#Mayusculas y minusculas
mayus = 'Esto es un ejemplo de mayusculas'
print(mayus.capitalize()) #Pone la primera letra en mayuscula
print(mayus.title()) #Pone la primera letra de cada palabra en mayuscula
print(mayus.upper()) #Pone todas las letras en mayuscula
print(mayus.lower()) #Pone todas las letras en minuscula
print(mayus.swapcase()) #Cambia las mayusculas por minusculas y viceversa   

#Identificando caracteres (Boleanos)
ident = 'R2D2'
print(ident.isalnum()) #Comprueba si todos los caracteres son letras o números
print(ident.isnumeric()) #Comprueba si todos los caracteres son números
print(ident.isalpha()) #Comprueba si todos los caracteres son letras
print(ident.islower()) #Comprueba si todos los caracteres son minusculas
print(ident.isupper()) #Comprueba si todos los caracteres son mayusculas


#EJERCICIO INTERPOLACIÓN
name = 'Marta'
edad = 19
nota_media = 4.5
colegio = 'Salesianos San Pedro'
mascota = 'Gato'
estudios = ['Grado Medio', 'Grado Superior']
emocion = ('contenta', 'ilusionada', 'motivada')

print(f'''Hola me llamo {name} y tengo {edad} años,\n
estudio en {colegio} y temgo una nota media de {nota_media}.\n
Los estudios realizados que tengo son {estudios[0]}, {estudios[1]} y me encuentro\n
{emocion[0]}, {emocion[1]}, {emocion[2]} por empezar este curso.''')
