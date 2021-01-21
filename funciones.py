def saludo(nombre):
    print('Hola, ' + nombre + '. ¡Bienvenido!')

saludo('mario')

def multi(a, b):
    resul = a * b
    return resul

print(multi(5, 5))

def suma_todo( *args): 
    resultado = 0
    for i in args:
        resultado += i
    return resultado 


v, w, x, y, z= 5, 2, 12, 6, 9
total=suma_todo(v,w,x,y,z)
print(f"La suma total es:" + str(total)) # La suma total es: 34


print()

def test_var_args(f_arg, *argv):
    print("primer argumento normal:", f_arg)
    for arg in argv:
        print("argumentos de *argv:", arg)

test_var_args('python', 'foo', 'bar')