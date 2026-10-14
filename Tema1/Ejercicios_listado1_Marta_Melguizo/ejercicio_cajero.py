# Haga un programa de la interfaz de un cajero automático. Tendrá las opciones, ver saldo,
#retirar dinero, comprar entradas e ingresar dinero. En cada opción se pedirán los datos
#necesarios y se realizarán las operaciones adecuadas. El coste de las entradas se debe restar al
#saldo de dicha cuenta. La cuenta será creada por nosotros con un saldo inicial concreto.

op = 0
salir = True
saldo = 500.95
entradas = 25.0
retirar = 0.0
ingresar = 0.0
total = 0.0

print('Bienvenido al cajero')

while salir:
    print('1 - Ver saldo')
    print('2 - Retirar dinero')
    print('3 - Comprar entradas')
    print('4 - Ingresar dinero')
    print('0 - Para Salir')
    op = int(input(''))

    match op:
        case 1:
            print('Este es tu saldo actual: ', saldo)
        case 2:
            retirar = float(input('¿Cuánto dinero desea retirar? \n'))
            saldo -= retirar
            print('Se ha retirado el dinero correctamente')
        case 3:
            print('Las entradas que desea comprar cuesta: ', entradas)
            num_entradas = int(input('¿Cuántas entradas desea comprar? \n'))
            total = num_entradas * entradas
            print('Las entradas han costado: ', total)
            saldo -= total
        case 4:
            ingresar = float(input('¿Cuánto dinero desea ingresar? \n'))
            saldo += ingresar
            print('Se ha ingresado el dinero correctamente')
        case 0:
            print('Hasta luego, vuelva pronto')
            salir = False
        case _:
            print('Datos incorrectos')
        

        

     
            