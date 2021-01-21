USU = 'root'
PASS = 'toor'
i = 3
while i > 0:
    nombre = str(input('Introduzca el nombre de usuario: '))
    contraseña =str(input('Introduzca la contraseña: '))
    i = i - 1
    if nombre == USU and contraseña == PASS:
        print('Bienvenido')
        break
    else:
        print(f'Acceso fallido, le quedan: {i} intentos.')
        if i == 0:
            print('Has agotado todos tus intentos')
