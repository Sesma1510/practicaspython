# Calculadora de IMC (Indice de Masa Corporal)

personas = int(input('Introduzca el numero de personas que van a calcular su IMC: '))

while personas > 0:
    while True:
        nombre = input('Introduce tu nombre: ')
        try:
            nombre = int(nombre)
            print('INVALIDO--> Porfavor introduce tu nombre solo con letras: ')
        except ValueError:
            break
    while True:
        apellido_paterno = input('Introduce tu apellido paterno: ')
        try:
            apellido_paterno = int(apellido_paterno)
            print('INVALIDO--> Porfavor introduce tu apellido paterno solo con letras: ')
        except ValueError:
            break
    while True:
        apellido_materno = input('Introduce tu apellido materno: ')
        try:
            apellido_materno = int(apellido_materno)
            print('INVALIDO--> Porfavor introduce tu apellido materno solo con letras: ')
        except ValueError:       
            break
    while True:
        edad = input('Introduce tu edad: ')
        try:
            edad = int(edad)
            break
        except ValueError:
            print('INVALIDO--> Porfavor introduce tu edad con numeros: ')       
    while True:
        peso = input('Introduce tu peso en kilogramos: ')
        try:
            peso = int(peso)
            break
        except ValueError:
            print('INVALIDO--> Porfavor introduce tu peso en numeros enteros: ')
    while True:
        estatura = input('Introduce tu estatura en metros "(ejem: 1.78 metros)": ')
        try:
            estatura = float(estatura)
            break
        except ValueError:
            print('INVALIDO--> Porfavor introduce tu estatura en este formato "(ejemplo: 1.78 metros)": ')
    IMC = int(peso) / float(estatura) ** 2

    if(edad < 18):
        print(f'{nombre.title()} {apellido_paterno.title()} {apellido_materno.title()}'', usted es menor de edad')
    else:
        print(f'{nombre.title()} {apellido_paterno.title()} {apellido_materno.title()}'', usted es mayor de edad')
    
    print(f'Su IMC es: {IMC:.2f} \nUsted tiene')
    

    if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Peso Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("Obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("Obesidad media")
    elif IMC >= 40.00:
        print ("Obesidad morbida")

    personas = personas - 1