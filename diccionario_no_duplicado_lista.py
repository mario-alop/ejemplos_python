nombre = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}
lista = []
print()
for i in nombre:
    print(i) 
    print(nombre[i])
print()
aux = []
for i in nombre:
    lista.append(nombre[i])
for i in lista:
    if i not in aux:
        aux.append(i)
        lista = aux
print(lista)
print()
