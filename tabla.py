numero = int(input('Introduce un numero: '))
for i in range(10):
    iterancion = i + 1
    print(f'{iterancion} * {numero} = {iterancion*numero}')


count=0 
while(count<5):
    count = count+1
    print("Iteración número {}".format(count)) 
else:
    print("Bucle while finalizado")

alumnos = ["Ane", "Mikel", "Unai", "Lorea"] 
for i in range(len(alumnos)):
    print(alumnos[i])