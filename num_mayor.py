numeros = []
aux = 0
for i in range(5):
    aux = int(input(f'Introduzca el {i+1}º número: '))
    numeros.append(aux)

print(f'Números introducidos: {numeros}')

mayor = numeros[0]
for x in range(1,5):
    if numeros[x] > mayor:
        mayor = numeros[x]

print(f'Número mayor de la lista: {mayor}')