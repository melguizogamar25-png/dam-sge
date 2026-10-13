#Piedra, papel

person_1 = 0
person_2 = 0

print('Bienvenidos')
print('Juego Piedra, Papel o Tijera')

person_1 = int (input('Jugador 1 elija: 1 - piedra | 2 - papel | 3 - tijeras'))
person_2 = int (input('Jugador 1 elija: 1 - piedra | 2 - papel | 3 - tijeras'))

match person_1:
    case 1:
        match person_2:
            case 1:
                print('Empate')
            case 2: 
                print('Gana jugador 2')
            case 3:
                print('Gana jugador 1')
    case 2:
        match person_2:
            case 1:
                print('Gana jugador 1')  
            case 2:
                print('Empate')
            case 3:
                print('Gana jugador 2')
    case 3:
        match person_2:
            case 1:
                print('Gana jugador 2')
            case 2:
                print('Gana jugador 1')
            case 3:
                print('Empate')
    case _:
        print('Opción incorrecta') 
    
