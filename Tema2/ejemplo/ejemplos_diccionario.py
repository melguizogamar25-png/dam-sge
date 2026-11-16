#Se queda con el orden en el que se insertan las claves
#Son mutables
#Las claves deben de ser únicas

# 5.3.1 Creando diccionarios
vacio = {} #Diccionario vacío
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'

}
print(rae)

# 5.3.2 Conversión
#Diccionario a partir de una lista de cadenas de texto
print(dict(['a1', 'b2']))
#Diccionario a partir de una tupla de cadenas de texto
print(dict(('a1', 'b2')))
#Diccionario a partir de una lista de listas 
print(dict([['a', 1], ['b', 2]]))

#Diccionario vacío
dict()

#Creación con dict
person = dict(
    name = 'Marta',
    surname = 'Melguizo',
    job = 'Programadora'
)
print(person)

# 5.3.3 Operaciones con diccionarios
#Obtener un elemento
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'

}
print(rae['anarcoide']) #Para obtener un solo elemento necesitas escribir la clave entre corchetes
#Para obetenr un elemento tambien podemos utilizar get
print(rae.get('bifronte'))
#Si no existe elemento que estamos qqueriendo obtener vamos a ponerle el mensje
#Que queremos que pong para que no ponga none
print(rae.get('programacion', 'No disponible'))

#Añadir o modificar un elemento
rae['enjuiciar'] = 'SOmeter una cuestión a examen, discusión y juicio'
print(rae)


