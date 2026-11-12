print('-- BIENVENIDOS --')

numeros = set()
cantidad = int(input('¿Cuántos números desea introducir?'))

for posicion in range(cantidad):
    numero = int(input(f'Introduzca el número {posicion + 1}'))
    numeros.add(numero)

opcion = int (1)

while opcion != 0:
    print('\n Conjunto actual:', numeros)
    