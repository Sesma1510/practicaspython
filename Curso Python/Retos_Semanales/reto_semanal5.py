while True:
    añoInicial = input('Introduce el año actual ')
    try:
        añoInicial = int(añoInicial)
        break
    except ValueError:
        print('Dato incorrecto el valor debe ser numerico')

while True:
    añoFinal = input('Introduce otro año para calcular: ')
    try:
        añoFinal = int(añoFinal)
        break
    except ValueError:
        print('Dato incorrecto el valor debe ser numerico')

if añoFinal == añoInicial:
    print('Haz introducido el mismo año, trata con diferentes')
else:
    años = añoFinal - añoInicial
    print(f'Desde el año {añoInicial} hasta el año {añoFinal} han pasado {años} años') 
