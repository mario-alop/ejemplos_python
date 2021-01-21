usuarios={ "iperurena": {
          "nombre": "Iñaki",
                  "apellido": "Perurena",
                  "password": "123123"
          },
          "fmuguruza": {
               "nombre": "Fermín",
                  "apellido": "Muguruza",
                  "password": "654321"
          },
          "aolaizola": {
               "nombre": "Aimar",
                  "apellido": "Olaizola",
                  "password": "123456"
} }

i = 3
while i > 0:
    nombre = str(input('Introduzca el nombre de usuario: '))
    contraseña =str(input('Introduzca la contraseña: '))
    i = i -1
    for key, value in usuarios.items():
        if nombre == key and contraseña == value['password']:
            print('Bienvenido')
            print(value['nombre'], value['apellido'])
    if i != 0:
        print(f'Acceso fallido, le quedan: {i} intentos.')   
    if i == 0:
        print('Has agotado todos tus intentos')
        break
            
            
        
            
            
