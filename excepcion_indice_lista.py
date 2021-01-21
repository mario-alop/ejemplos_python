def fun_excep():
   
    lista = [6, 14, 11, 3, 2, 1, 15, 19]
    
    try:
        numero = int(input('Introduce un índice: '))
        resul = lista[numero-1]
        print(f'El número del índice {numero} es: {resul}')
        
          
    except ValueError: 
        print('Número inválido.')
        return fun_excep()
    except IndexError:
        print('Índice no existe.')
        fun_excep()

fun_excep()