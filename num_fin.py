numeros = []
aux = 0
tamnio = 1
terminar = ''
while True:
    aux = (input(f'Introduzca el {tamnio}º número: '))
    terminar = str(aux)
    if terminar != 'fin':
        numeros.append(aux)
        tamnio += 1
        print(f'Números introducidos: {numeros}')
    else:
        break
numeros.sort()        
print(f'Números introducidos: {numeros}')

mayor = numeros[0]
for x in range(1,tamnio-1):
    if numeros[x] > mayor:
        mayor = numeros[x]

print(f'Número mayor de la lista: {mayor}')