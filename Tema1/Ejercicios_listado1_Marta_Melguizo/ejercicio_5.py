#Crea una variable numérica y si está entre 0 y 10, mostrar un mensaje indicándolo.

num = float(input('Introduce un número: '))

if num >= 0 and num <= 10:
    print('Este número está entre 0 y 10.')
else:
    print('Este número no está entre 0 y 10.')