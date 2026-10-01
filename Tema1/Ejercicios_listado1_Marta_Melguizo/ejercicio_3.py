#Mostrar el precio final (con IVA) de un producto con un valor de 100 euros, suponiendo que el IVA es el 21%.

iva = float(input('Introduce el IVA: '))
producto = float(input('Introduce el precio del producto: '))

precio_final = producto + (producto * iva/100)

print('Precio sin IVA:', producto, '€')
print('Precio final con IVA:', precio_final, '€')


