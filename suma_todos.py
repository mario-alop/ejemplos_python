num1 = int(input('Introduzca un número entero: '))
num2 = int(input('Introduzca otro número entero: '))
total = 0
for i in range(num1, num2+1):
    print(f'El número: {num1} + {i} = {num1+i}')
    total += num1 + i
print(f'La suma total de números es: {total}')