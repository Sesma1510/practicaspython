contador = 3

while contador > 0 :   
    contraseña = input('Cree una contraseña: ')
    if contraseña[0].isnumeric() :
        contraseñaRepetida = input('Repita la contraseña: ')

        if contraseña == contraseñaRepetida :
            contador = 0
            break
        else :
            print(f'Las contraseñas no coinciden')
            contador = contador - 1
            if contador == 0 :
                print('Excedio el numero de intentos, el programa se cerrara')
                break
    else:
        print('La contraseña tiene que empezar con un numero')
        contador = contador - 1
        if contador == 0 :
                print('Excedio el numero de intentos, el programa se cerrara')
                break


