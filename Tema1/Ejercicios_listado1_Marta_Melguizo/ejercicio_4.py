#De dos números, saber cuál es el mayor.

num1 = float(input('Introduce el primer número: '))
num2 = float(input('Introduce el segundo número: '))

if num1 > num2:
    print('El mayor es: ', num1)
elif num2 > num1: 
    print('El mayor es: ', num2)
else:
    print('Los números son iguales.')
