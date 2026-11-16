#5.1.1 Creando listas
listas_vacias = []
listas_palabras = ['Python', 'JavaScript', 'C++']
listas_numericas = [2, 3, 6, 7, 9]

#5.1.2 Conversión
#Conversion de una cadena de texto
print(list('Python'))

#Conversion de una lista con rangos
print(list(range(10)))

#Conversion a una lista vacía
print(list())

#5.1.3 Operaciones con listas
#Obtener un elemento
tienda = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']

print(tienda[1]) #Si ponemos un indice que no esta en la lista nos da error
#Trocear una lista
print(tienda[0:3]) #Coge el indice del 0 al 2, el ultimo nunca lo acepta

#Invertir una lista
print(tienda[::-1]) #Es la lista original pero invertida (Conservas la lista)
print(tienda.reverse()) #Modificas la lista original

#Añadir al final de la lista
tienda.append('Atún')
print(tienda)

#Añadir a cualquier posición de una lista
    #en este tipo de inserciones no obtendremos un
    #error si especificamos índices fuera de los límites de la lista.
tienda.insert(1, 'Jamón')
print(tienda)

#Repetir elementos
print(tienda * 3)

#Combinar listas
frutas = ['Naranja', 'Manzana', 'Piña']
print(tienda + frutas) #Aqui estamos conservando la lista original
print(tienda.extend(frutas))#Estamos modificando la lista original

#Modificar una lista
tienda[0] = 'Jugo'
print(tienda)

#Modificar con troceado
tienda[1:4] = ['Atún', 'Pasta']
print(tienda)

#Borrar elemento
del tienda[3] #Se borra por el indice
tienda.remove('Sal') #Se borra por su valor
producto = tienda.pop() #Se coge el indice -1
producto = tienda.pop(2)#Nos devuelve el elemento borrado
print(producto)
print(tienda)
tienda[1:4] = [] #Mediante troceados
print(tienda)

#Borrado completo de la lista
tienda.clear() 
tienda = [] #reinicias la lista a vacío (Nueva zona de memoria)

#Encontrar un elemento
print(tienda.index('Huevos'))

#Pertenencia de un elemento
print('Aceite' in tienda) #te devuelve un booleano

#Número de ocurrencias
sheldon_greeting = [ 'Penny', 'Penny', 'Penny' ]
print(sheldon_greeting.count('Howard'))
print(sheldon_greeting.count('Penny'))

#Convertir lista a cadena de texto
    #unimos todos sus elementos mediante algún separador
print(','.join(tienda))
print('|'.join(tienda))

#Ordenar una lista
print(sorted(tienda)) #Conservando la lista orginal
print(tienda.sort()) #Modificando la lista original
print(sorted(tienda, reverse=True)) #Ambos métodos admiten un parámetro «booleano» reverse para indicar si queremos que la ordenación se haga en sentido inverso:

#Longitud de una lista
print(len(tienda))

#Iterar sobre una lista
for producto in tienda:
    print(producto)

#Iterar usando enumeración
for i, producto in enumerate(tienda):
    print(i, producto)

#Iterar sobre multiples listas
comida = ['Agua', 'Aceite', 'Arroz']
details = ['mineral natural', 'de oliva virgen', 'basmati']
for producto, details in zip(comida, details):
    print(comida, details)

#Lista explicita con la combinación
print(list(zip(comida, details)))

#5.1.4 Cuidado con las copias
    #Se cambian las dos listas, tanto la original como la copia
original_list = [4,3,7,1]
copy_list = original_list
original_list[0] = 15
print(original_list)
print(copy_list)

    #Se copia y si se cambia la original no se cambia la copia y viceversa
copy_list = original_list.copy()
original_list[0] = 15
print(original_list)
print(copy_list)

#5.1.5 Veracidad múltiple 
word = 'python'
if len(word) > 4 and word.startswith('p') and word.count('y') >= 1:
    print('Cool word!')
else:
    print('No thanks')

#veracidad multiple usando all
word = 'python'
enough_length = len(word) > 4 
right_beginning = word.startswith( 'p' )
min_ys = word.count( 'y' ) >= 1
is_cool_word = all([enough_length, right_beginning, min_ys])
if is_cool_word:
    print( 'Cool word!' )
else:
    print('No thanks')

#veracidad multiple usando any
word = 'yeah'
enough_length = len(word) > 4 
min_ys = word.count( 'y' ) >= 1 
is_fine_word = any([enough_length, right_beginning, min_ys])
if is_fine_word:
    print('Fine word!')
else:
    print('No thanks')

#5.1.6 Listas por compresión
values = 32,45,11,87,20,48
int_values = [int(value) for value in values.split(',')]
print(int_values)

#5.1.8 Funciones matemáticas
#Suma de todos los valores
data = [5,3,2,8,9,1]
print(sum(data))
#Minimo de todos los valores
print(min(data))
#Máximo de todos los valores
print(max(data))
