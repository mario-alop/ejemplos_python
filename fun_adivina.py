from random import randint, uniform, random

print()
print('Introduzca un número del 1 al 10')
aleatorio = randint(0, 10)
#print(aleatorio)
def adivina():
    try:
        numero = int(input('Número: '))
        if aleatorio == numero:
            print('Has acertado el número!!!!')
        elif aleatorio > numero:
            print('El número es mayor.')
            adivina()
            return
        elif aleatorio < numero:
            print('El número es menor.')
            adivina()
            return
    except:
        print("Por favor ingrese un número válido del una al diez")
        adivina()
adivina()
