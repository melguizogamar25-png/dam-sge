#Calculadora con un match case
#No parar hasta que el usuario escriba un 0

while True:
    print("Bienvenidos al programa")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Salir")
    op = int(input("Seleccione: "))
    num_1 = float(input("Diga el primer número que quiere operar: "))
    num_2 = float(input("Diga el segundo número que quiere operar: "))

    match op:
        case 1:
            resul = num_1 + num_2
            print("El resultado es: ", resul)
        case 2:
            resul = num_1 - num_2
            print("El resultado es: ", resul)
        case 3:
            resul = num_1 * num_2
            print("El resultado es: ", resul)
        case 4: 
            resul = num_1 // num_2
            print("El resultado es: ", resul)
        case 0:
            print("Hasta Luego")


    