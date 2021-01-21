import math


class Poligono:
    def __init__(self, color, *lados):
        self.color = color
        self.lados = lados


    def perimetro(self):
        aux = 0
        for i in self.lados:
            aux = sum(i)
        return aux

class Triangulo(Poligono):
    def __init__(self, color, *lados):
        super().__init__( color, *lados)
        self.color = color
        self.lados = lados

    def perimetro(self):
        return super(Triangulo, self).perimetro()

    def tipo_triangulo(self):
        lado = self.lados[0]

        if lado[0] == lado[1] and lado[0] == lado[2]:
            # self.tipo = 'Equilatero'
            return 'Equilátero'
        elif lado[0] != lado[1] and lado[0] != lado[2] and lado[1] != lado[2]:
            # self.tipo = 'Escaleno'
            return 'Escaleno'
        else:
            # self.tipo = 'Isósceles'
            return 'Isósceles'


    def area(self):
        tipo = self.tipo_triangulo()
        lado = self.lados[0]
        area = 0
        if tipo == 'Equilátero':
            semiperimeto = (lado[0] + lado[1] + lado[2]) / 2
            area = math.sqrt(semiperimeto * (semiperimeto - lado[0]) *
                             (semiperimeto - lado[1]) * (semiperimeto - lado[2]))

        if tipo == 'Escaleno':
            semiperimeto = (lado[0] + lado[1] + lado[2]) / 2
            area = math.sqrt(semiperimeto * (semiperimeto - lado[0]) *
                             (semiperimeto - lado[1]) * (semiperimeto - lado[2]))

        if tipo == 'Isósceles':
            semiperimeto = (lado[0] + lado[1] + lado[2]) / 2
            area = math.sqrt(semiperimeto * (semiperimeto - lado[0]) *
                             (semiperimeto - lado[1]) * (semiperimeto - lado[2]))

        return area

class Cuadrado(Poligono):
    def __init__(self, color, *lados):
        super().__init__( color, *lados)
        self.color = color
        self.lados = lados

    def perimetro(self):
        return super(Cuadrado, self).perimetro()

    def area(self):
        lado = self.lados[0]
        area = lado[0]**2
        return area

print()
p1 = Poligono('rojo', [2, 4, 5])
print(f'Poligono {p1.color} con {p1.perimetro()} metros de perímetro')
print()
t1 = Triangulo('verde', [9, 8, 6])
print(f'Triangulo {t1.color} con {t1.perimetro()} metros de perímetro ')
print(f'El tipo de triangulo es: {t1.tipo_triangulo()}')
print(f'El Area del triangulo es: {t1.area()}')
print()
c1 = Cuadrado('Azul', [5, 5, 5, 5])
print(f'Cuadrado {c1.color} con {c1.perimetro()} metros de perímetro ')
print(f'El Area del Cuadrado es: {c1.area()}')
c1.area()
print()
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)
print(mi_lista[:])
