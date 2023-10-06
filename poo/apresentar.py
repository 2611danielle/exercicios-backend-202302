class Apresentar:
    def __init__(self, nomeCompleto):
        self.nomeCompleto = nomeCompleto
    def apresenta01(self):
        """ Aqui estou declarando método apresenta01 """
        return "Olá, estou me apresentando"
    def apresenta (self, nome):
        """ Aqui estou declarando método apresenta """
        return "Olá, eu me chamo {0}". format (nome)
    def apresentaComAtrib (self):
        """ Aqui estou declarando método apresentaComAtrib """
        return "Meu nome completo é {0} ".format (self.nomeCompleto)
""" Aqui inicia nosso programa """
meApresento = Apresentar("Danielle Batista de Souza Silva")
print (meApresento.apresenta01())
print (meApresento.apresenta ("Dani Souza"))
print (meApresento.apresentaComAtrib())
meApresento.nomeCompleto = "Danielle de Souza"
print (meApresento.apresentaComAtrib())