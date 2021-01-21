numeros1 = []
numeros2 = []
iguales = []
aux = 0

for i in range(5):
    numeros1.append(int(input(f'Lista 1ª introduzca el {i+1} número: ')))

print()

for i in range(5):
    numeros2.append(int(input(f'Lista 2ª introduzca el {i+1} número: ')))

for i in range(5):
    if numeros1[i] in numeros2:
        iguales.append(numeros1[i])

print()

print(iguales)