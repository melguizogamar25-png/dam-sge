# 5.2.1 Crear una tupla
vacia = ()
tupla_numerica = (412, 526) #Se puede poner números en neghativo
three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')

print(vacia)
print(tupla_numerica)
print(three_wise_men)

#Tuplas de un elemento
#Esto se utiliza para las tuplas de un solo elemento
one_item = ('Papá Noel')
print(type(one_item)) #Se ha creado una variable de tipo string
one_item_tuple = ('Papá Noel', )
print(type(one_item_tuple)) #Al ponerle una coima al final lo que se consigue es que se cree una tupla

#Tuplas sin paréntesis
one_item = 'Papá Noel',
three_wise_men = 'Melchor' , 'Gaspar' , 'Baltasar'
tenerife_geoloc = 28.46824, -16.25462

# 5.2.2 Modificar una tupla
three_wise_men = 'Melchor' , 'Gaspar' , 'Baltasar'
#No se puede modificar una tupla porque es una estructura de datos inmutable
#Cuando creamos la tupla con un valor, no se puede modificar
three_wise_men[0] = 'Tom Hanks'
print(three_wise_men)

# 5.2.3 Conversión
#Este tipo de conversión solo se puede hacer con datos iterables
#Como por ejemplo listas, diccionarios, pero no se puede hacer con un número
shopping = ['Agua', 'Aceite', 'Arroz']
print(tuple(shopping))#Si utilizas la función tuple sin argumentos () se crea una tupla vacía

# 5.2.4 Operaciones con tuplas
mi_tupla = (3, 1, 4, 1, 5)
#Todos estos metodos dan error porque:
print(mi_tupla.reverse()) #Modificarias las posiciones del objeto original
print(mi_tupla.append(9)) #Cambiaria el tamaño y contenido de la tupla
print(mi_tupla.extend([9, 2])) #Cambiaria el tamaño y contenido de la tupla 
print(mi_tupla.remove(4)) #No puedes eliminar porque estarias cambiando el tamaño y contenido de la tupla
print(mi_tupla.clear()) #Dejarias la tupla vacía 
print(mi_tupla.sort()) #Cambiaria las posiciones del objeto original 

#Los siguientes metodos si funcionan porque devuelven nuevos elementos no cambia el original
#sorted()
numeros = (5, 2, 8, 1, 4)
resultado_ordenado = sorted(numeros)
print(resultado_ordenado)  #es una lista
print(numeros) #la tupla original no cambia
# Si necesitas que el resultado vuelva a ser una tupla:
tupla_ordenada = tuple(sorted(numeros))
print(tupla_ordenada)
#reversed()
letras = ('a', 'b', 'c', 'd')
resultado_invertido = tuple(reversed(letras)) # Aplicamos reversed() y convertimos a tupla
print(resultado_invertido)
print(letras) #la tupla original no cambia

# 5.2.5 Desempaquetado de tuplas
three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')
king1, king2, king3 = three_wise_men
print(king1) #Saldría Melchor
#Sale Melchor porque el primer valor de la tupla se asocia al primer valor escrito abajo

#Esta funcion devuelve el cociente y el resto de una division
cociente, resto = divmod(7, 3) #Divide 7 enrre 3
print(cociente) #Muestra el cociente que es 2
print(resto) #Muestra el resto que es 1

#Intercambio de valores
value1 = 40
value2 = 20
value1, value2 = value2, value1
print(value1) #Este valor ahora vale 20
print(value2)

#Desempquetado extendido
#Extrae elementos individuales y agrupa el resto
ranking = ('G', 'A', 'R', 'Y', 'W')
head, *body, tail = ranking
print(head) #Coge el primer elemento de la tupla
print(body) #Con el * le dice que tome todo lo que quede en medio y lo guarde en una lista (Siempe devuelve una lista)
#Solo puede tener un * por cada operacion
print(tail) #Coge el ultimo elementode la tupla
first, *rest = ranking
print(first) #Coge el primero
print(rest) #Coge los elementos que queden sin contar el primero

#Desempaquetando genérico
#Es extensible a cualquier tipo de datos que sea iterable
#Sobre cadenas de texto
oxygen = '02'
first, last = oxygen
print(first, last) #La variable first enseña un 0 y last un 2 separados por comas
#Sobre listas
writer1, writer2, writer3 = ['Hola', 'Adios', 'Haasta luego']
print(writer1, writer2, writer3)

# 5.2.6 ¿Tuplas por comprension?
myrange = (number for number in range(1, 6))
print(myrange)