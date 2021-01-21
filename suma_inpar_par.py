num1 = int(input('Introduzca un número entero: '))
num2 = int(input('Introduzca otro número entero: '))
total_par = 0
total_inpar = 0
total = 0
for i in range(num1, num2+1):
    print(f'El número: {num1} + {i} = {num1+i}')
    total += num1 + i
    if i % 2 == 0:
        total_par += num1 + i
    else:
        total_inpar += num1 + i
print(f'La suma total de números es: {total}')
print(f'La suma total de números pares es: {total_par} y la suma de los impares es: {total_inpar}')