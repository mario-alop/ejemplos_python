class Vehiculo:
    kilometros_recoridos: int = 0

    def __init__(self, marca):
        super().__init__()
        self.marca = marca

    def avanzar(self, kilometros_conducidos):
        self.kilometros_recoridos += kilometros_conducidos


class Coche(Vehiculo):
    diesel = 0
    kilometros_recoridos = 0
    gasolina = 0

    def __init__(self, matricula, marca):
        Vehiculo.__init__(self, marca)
        self.matricula = matricula
        self.marca = marca
        # self.kilometros_recoridos = kilometros_recoridos
        # self.gasolina = gasolina

    def avanzar(self, km_conducidos):
        if self.gasolina <= 0 and self.diesel <= 0:
            self.repostar(50)
        elif self.gasolina - km_conducidos * 0.1 < 0 and self.diesel - km_conducidos * 0.1 < 0:
            print('Es necesario repostar gasolina para reorrer la cantidad indicada de kilómetros')
            print('Es necesario repostar diesel para reorrer la cantidad indicada de kilómetros')
            self.repostar(50)
            self.kilometros_recoridos += km_conducidos
            self.gasolina -= (km_conducidos * 0.1)
            self.diesel -= (km_conducidos * 0.1)
            print(f'Kilometros recoridos = {self.kilometros_recoridos},'
                  f' gasolina = {self.gasolina}, diesel = {self.diesel}')

        else:
            self.kilometros_recoridos += km_conducidos
            self.gasolina -= (km_conducidos * 0.1)
            self.diesel -= (km_conducidos * 0.1)
            print(f"Kilometros recoridos = {self.kilometros_recoridos},"
                  f" gasolina = {self.gasolina}, diesel = {self.diesel}")

    def repostar(self, litros):
        self.diesel += litros
        self.gasolina += litros
        print(f'diesel = {self.diesel}')
        print(f'gasolina = {self.gasolina}')


class Bicicleta(Vehiculo):
    kilometros_recorridos = 0
    aire = 0

    def __init__(self, marca):
        super().__init__(marca)
        self.marca = marca

    def avanzar(self, km_conducidos):
        if self.aire < 0:
            self.hinchar_ruedas(50)
        elif self.aire - km_conducidos * 0.1 < 0:
            self.hinchar_ruedas(50)
            self.kilometros_recoridos += km_conducidos
            self.aire -= (km_conducidos * 0.1)
            print(f'Kilometros recoridos = {self.kilometros_recoridos}')
        else:
            self.kilometros_recoridos += km_conducidos
            self.aire -= (km_conducidos * 0.1)
            print(f'Kilometros recoridos = {self.kilometros_recoridos}')

    def hinchar_ruedas(self, dar_aire):
        self.aire += dar_aire
        print('Es necesario hinchar parar ecorrer la cantidad indicadade kms.')


coche1 = Coche('8529FKK', 'BMW')
print(f'Coche matricula: {coche1.matricula} marca: {coche1.marca}')
coche1.avanzar(50)
coche1.avanzar(100)
coche1.avanzar(250)
coche1.avanzar(200)
print()
coche2 = Coche('2244DDD', 'Mercedes')
print(f'Coche matricula: {coche2.matricula} marca: {coche2.marca}')
coche2.avanzar(50)
coche2.avanzar(100)
print()
bici = Bicicleta('BH')
print(f'Bicicleta marca: {bici.marca}')
bici.avanzar(60)
bici.avanzar(250)
bici.avanzar(500)
