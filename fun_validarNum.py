
'''
def esta_en_rango(rango, numero):
    if numero in range(*rango):
        return numero
    else:
        return 

print(esta_en_rango([1, 20], 45))
'''
def esta_en_rango(numero):
    no = 'No existe'
    if numero <= 20:
        return numero
    else:
        return print(no)
print(esta_en_rango(21))