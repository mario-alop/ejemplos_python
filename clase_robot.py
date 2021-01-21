class Robot:
    
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def mueve(self, orden):
        if orden == 'A':
            self.x +=  1
        if orden == 'R':
            self.x -= 1
        if orden == 'I':
            self.y -= 1
        if orden == 'D':
            self.y += 1

    def posicion_actual(self):
        print(f'Posición actual: {self.x},{self.y}')

miRobot = Robot(0, 0)
orden = 'A'
while orden != 'fin':
    orden = input('>> Introduce la orden: ')
    miRobot.mueve(orden)
    miRobot.posicion_actual()

miRobot1 = Robot(0, 0)
orden = 'A'
while orden != 'fin':
    orden = input('>> Introduce la orden del segundo Robot: ')
    miRobot1.mueve(orden)
    miRobot1.posicion_actual()
