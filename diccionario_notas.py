estudiantes = {}
id = 1
aprobados = 5
suspensos = 4
suma = 0
media = 0
print()
cantidad = int(input('Introduce la cantidad de alumnos que vamos a guradar: '))
print()
while id <= cantidad:
    nombre = input('Nombre del alumno: ')
    nota = float(input('Dame una nota del alumno: '))
    suma += nota
    print()
    estudiantes[id] = {'nombre': nombre, 'nota': nota}
    id = id + 1
print()

for alumno, notas in estudiantes.items():
    print(alumno,notas)
    

print()
print('Lista de Aprobados: ')
for key, value in estudiantes.items():
    if value['nota'] >= aprobados:
        print(key,value)
print()
print('Lista de Suspensos: ')
for key, value in estudiantes.items():
    if value['nota'] <= aprobados:
        print(key,value)
print()
for i in estudiantes:
    media = i
print(f'La nota media de la clase es: ', suma/media)
print()
