lista = [12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64, 23]
diccionario = {}
for i in lista:
    if i not in diccionario:
        diccionario[i] = 1
    else:
        diccionario[i] = diccionario[i] + 1

print()
print('Lista:')
print()
print(lista)
print()
print('Número de veces que aparece cada número en la lista:')
print()
print(diccionario)
print()