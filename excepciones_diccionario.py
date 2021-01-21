
def fun_excep():
   
    diccionario = {'Python': 1991,'Java': 1991 ,'C': 1972}

    try:
        clave = str(input('Introduce una clave: '))
        resul = diccionario[clave]
        print(f'La clave es: {clave}. El valor es: {resul}')      
    except (ValueError, TypeError, KeyError): 
        print('Clave inválida.')
        return fun_excep()
    

fun_excep()