class Carro:
    def __init__(self, nome):
        self.nome = nome

    @property
    def motor(self, motor):
        return self._motor   



class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

c1, c2, c3, c4, c5 = Carro('polo'), Carro('fox'), Carro('virtus'), Carro('argo'), Carro('stilo')
motor10, motor10t, motor16 = Motor('1.0'), Motor('1.0 Turbo'), Motor('1.6')
marca1, marca2 = Fabricante('Volkswagen'), Fabricante('Fiat')

c1.ins_marca_motor(marca1, motor10)
c2.ins_marca_motor(marca1, motor10t)
c3.ins_marca_motor(marca1, motor16)
c4.ins_marca_motor(marca2, motor10)
c5.ins_marca_motor(marca2, motor16)

carros = [c1, c2, c3,c4,c5]

for carro in carros:
    print(carro.nome, carro.motor, carro.marca)