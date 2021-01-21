agenda = {}
# comentario
salir = False

while not salir:

    # Pedimos los datos
    nombre = input("Introduce un nombre: ")
    telefono = int(input("Introduce un telefono: "))
    edad = int(input('Introduzca edad: '))

    # Comprobamos si esta dentro del diccionario
    if nombre not in agenda:
        # Añadimos el contacto
        agenda[nombre] = telefono, edad
        print('Añadido el contacto')
    else:
        print('El nombre esta repetido')

    # Indicamos si queremos salir
    respuesta = input("¿Quieres salir? (S/N)")

    if respuesta == "S":
        salir = True

# Mostramos el diccionario
print(agenda)
