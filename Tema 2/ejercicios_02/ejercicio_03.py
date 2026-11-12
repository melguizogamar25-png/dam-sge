print('-- BIENVENIDOS --')

import random

estudiantes = {
    '12345678A': round(random.uniform(1, 10), 2),
    '87654321B': round(random.uniform(1, 10), 2),
    '11223344C': round(random.uniform(1, 10), 2)
}

continuar = True

while continuar:
    print('\n MENÚ EXPEDIENTES ESTUDIANTES ')
    print('1 - Mostrar los datos')
    print('2 - Modificar la nota')
    print('3 - Añadir un nuevo estudiante')
    print('4 - Filtrar la nota de corte')
    print('0 - Salir')
    opcion = int(input('Elige un a opción: '))

    match opcion:
        case 1: 
            print('\n DATOS DE LOS ESTUDIANTES')
            for dni, nota in estudiantes.items():
                print(f'DNI: {dni} | NOTA: {nota}')

        case 2: 
            dni = input('Introduce el Dni del estudiante a modificar: ')
            if dni in estudiantes:
                nueva_nota = float(input('Introduce la nueva nota: '))
                estudiantes[dni] = nueva_nota
                print(f'Nota actualizada correctamente para {dni}')
            else:
                print('EL Dni introducido no existe')

        case 3:
            dni = input('Introduce')
