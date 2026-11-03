#Hasta la pag 165
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
print(tienda[0:3]) #Coge el indice del 0 al 2, el ulktimo nunca lo acepta

#Invertir una lista
print(tienda[::-1]) #Es la lista original pero invertida (Conservas la lista)
print(tienda.reverse()) #Modificas la lista original

#Añadir al final de la lista
tienda.append('Atún')
print(tienda)

#Añadir a cualquier posición de una lista
tienda.insert(1, 'Jamón')
print(tienda)

#Repetir elementos
print(tienda * 3)

#Combinar listas
frutas = ['Naranja', 'Manzana', 'Piña']
print(tienda + frutas) #Aqui estamos conservando la lista original
print(tienda.extend(frutas))#Estamois modificando la lista original

#Modificar una lista
tienda[0] = 'Jugo'
print(tienda)

#Modificar con troceado
tienda[1:4] = ['Atún', 'Pasta']
print(tienda)

#Borrar elemento
del tienda[3] #Se borra por el indice
tienda.remove('Sal') #Se borra por su valor
producto = tienda.pop() #Se copge el indice -1
producto = tienda.pop(2)
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
