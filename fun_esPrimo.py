def esPrimo(num):
    if num % 2 == 0:
        print(f'El número: {num} es primo')
        return True
    else:
        print(f'El número: {num} no es primo')
        return False
        

print(esPrimo(3))