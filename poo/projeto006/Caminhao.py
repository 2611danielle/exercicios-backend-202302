import Veiculo
class Caminhao( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, cilindrada):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Caminhao")
        self.cilindrada = cilindrada
        self.marcha = 1
    def ligar(self):
        return self.marcha
    def desligar(self):
        self.marcha = 1
""" Aqui comeca o teste """
Caminhao = Caminhao('5AZKG01Z12A339037', 'Ford', 'C-1519', '2017', 4464)

print(Caminhao.marca)
print(Caminhao.ligar())