class Robot:
    
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        

    def mueve(self, orden):
        for i in orden:
            if i == 'A':
                self.x +=  1
            if i == 'R':
                self.x -= 1
            if i == 'I':
                self.y -= 1
            if i == 'D':
                self.y += 1

    def posicion_actual(self):
        print(f'Posición actual: {self.x},{self.y}')

    def devolver_ordenes(self, lista):
        ordenes = ''
        for i in lista:
            ordenes += i
        return print(f'Ordenes recibidas: {ordenes}')

    def posicion_inicial(self):
        ordenes = ''
        if self.x > 0:
            for i in range(self.x):
                ordenes += 'R'
                self.x -= 1
        if self.x < 0:
            for i in range(self.x, 0):
                ordenes += 'A'
                self.x += 1
        if self.y > 0:
            for i in range(self.y):
                ordenes += 'I'
                self.y -= 1
        if self.y < 0:
            for i in range(self.y, 0):
                ordenes += 'D'
                self.y += 1
            
        return print(f'Secuencia para posición inicial : {ordenes}')

miRobot = Robot(0, 0)
orden1 = []
orden = ''
while orden != 'fin':
    orden = input('>> Introduce la orden: ')
    orden1.append(orden)
    miRobot.mueve(orden)
    miRobot.posicion_actual()

miRobot.devolver_ordenes(orden1)
miRobot.posicion_inicial()
miRobot.posicion_actual()




