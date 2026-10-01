#La sentencia if
temperatura = 40

if temperatura > 35: #Esto serian los parentesis en java
    print('Aviso por alta temperatura')
else:
    print('Parametros normales')

#Asignación condicional
    #Aunque la tradicional vale debemos de hacer este ejemplo
fire_risk = 'LOW' if temperatura < 30 else 'HIGH'

#Booleanos en condiciones
is_cold = True
if is_cold: #No hace falta poner == true ya que is_cold es True 
    print('Coge chaqueta')
else:
    print('Usa camiseta')

    #Si fuera con valor falso
cold = False
if not cold: #Equivalente a if cold == False
    print('Usa camiseta')
else:
    print('Coge chaqueta')

#Akinator con superheroes

