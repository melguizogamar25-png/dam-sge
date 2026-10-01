#Akinator

vuela = input('¿Puede volar?: ').lower() == 'si'
humano = input('¿Es humano?: ').lower() == 'si'
mascara = input('¿Tiene máscara?: ').lower() == 'si'

if vuela and humano and mascara:
    personaje = 'Ironman'
elif vuela and humano and not mascara:
    personaje = 'Captain Marvel'
elif vuela and not humano and mascara:
    personaje = 'Ronan the Accuser'
elif vuela and not humano and not mascara:
    personaje = 'Vision'
elif not vuela and humano and mascara:
    personaje = 'Spiderman'
elif not vuela and humano and not mascara:
    personaje = 'Hulk'
elif not vuela and not humano and mascara:
    personaje = 'Black Bolt'
else:
    personaje = 'Thanos'
print('Tu personaje es: ', personaje)