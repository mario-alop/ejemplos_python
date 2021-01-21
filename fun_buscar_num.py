
def buscar_num(numero, *args):
    for i in args:
        if numero in i:
            print(f'Número encontrado: {numero}')
            return numero
        else:
            print(f'El número {numero} no aparece en la lista.')

lista = [6,14,11,3,2,1,15,19]
numero = buscar_num(11, lista)
print(numero)