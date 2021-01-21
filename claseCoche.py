class Coche:
    def __init__(self, matricula, marca, kilometros_recoridos, gasolina):
        super().__init__()
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recoridos = kilometros_recoridos
        self.gasolina = gasolina

    def avanzar(self, km_conducidos):
        if self.gasolina <= 0:
            self.repostar(50)
        elif self.gasolina - km_conducidos * 0.1 < 0:
            print('Es necesario repostar para reorrer la cantidad indicada de kilómetros')
            self.repostar(50)
            self.kilometros_recoridos += km_conducidos
            self.gasolina -= (km_conducidos * 0.1)
            print(f'Kilometros recoridos = {self.kilometros_recoridos}, gasolina = {self.gasolina}')
               
        else:
            self.kilometros_recoridos += km_conducidos
            self.gasolina -= (km_conducidos * 0.1)
            print(f'Kilometros recoridos = {self.kilometros_recoridos}, gasolina = {self.gasolina}')

    def repostar(self,litros):
        self.gasolina += litros
        print(f'gasolina = {self.gasolina}')
        

coche1 = Coche('8529FKK', 'BMW', 0, 0)
coche1.avanzar(50)
coche1.avanzar(100)
coche1.avanzar(250)
coche1.avanzar(200)

