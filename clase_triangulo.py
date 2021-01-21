import math


class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        # self.tipo = tipo

    def area(self):
        tipo = self.tipo_triangulo()
        area = 0
        if tipo == 'Equilátero':
            semiperimeto = (self.lado1 + self.lado2 + self.lado3) / 2
            area = math.sqrt(semiperimeto * (semiperimeto - self.lado1) *
                             (semiperimeto - self.lado2) * (semiperimeto - self.lado3))

        if tipo == 'Escaleno':
            semiperimeto = (self.lado1 + self.lado2 + self.lado3) / 2
            area = math.sqrt(semiperimeto * (semiperimeto - self.lado1) *
                             (semiperimeto - self.lado2) * (semiperimeto - self.lado3))

        if tipo == 'Isósceles':
            semiperimeto = (self.lado1 + self.lado2 + self.lado3) / 2
            area = math.sqrt(semiperimeto * (semiperimeto - self.lado1) *
                             (semiperimeto - self.lado2) * (semiperimeto - self.lado3))

        return area

    def tipo_triangulo(self):
        # self.tipo = ''
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            # self.tipo = 'Equilatero'
            return 'Equilátero'
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:
            # self.tipo = 'Escaleno'
            return 'Escaleno'
        else:
            # self.tipo = 'Isósceles'
            return 'Isósceles'

    def perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro


cateto1 = int(input('Introdece el cateto 1: '))
cateto2 = int(input('Introdece el cateto 2: '))
hipotenusa = int(input('Introdece de la hipotenusa: '))
miTriangulo = Triangulo(cateto1, cateto2, hipotenusa)
print(f'El area del triangulo es: {miTriangulo.area()}')
print(f'El tipo de triangulo es: {miTriangulo.tipo_triangulo()}')
print(f'El perimetro del triangulo es: {miTriangulo.perimetro()}')
