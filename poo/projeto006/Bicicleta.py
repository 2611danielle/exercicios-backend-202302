import Veiculo
class Bicicleta( Veiculo.Veiculo ):
    def __init__(self, marca, aro, marcha, ano):
        super().__init__(marca, aro, marcha, ano)
        super().set_tipo("Bicicleta")
        self.marca = marca
        self.aro = aro
        self.marcha = marcha
        self.marcha = 18
    def avancar(self):
        return self.marcha
    def frear(self):
        self.marcha = 1
""" Aqui comeca o teste """
Bicicleta = Bicicleta('Caloi', '29', '21', '2023')

print(Bicicleta.marca)
print(Bicicleta.avancar())
