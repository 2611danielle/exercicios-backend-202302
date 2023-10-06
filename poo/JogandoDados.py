class JogandoDados:
    """
    classe que representara  o jogo de dados para tabuleiro
    """
    def __init__(self):
        self.__numeroDeLados = 6
    def get_numeroDeLados(self):
        return self.__numeroDeLados
    def set_numeroDeLados(self, numeroDeLados):
        self.__numeroDeLados = numeroDeLados
    def jogarDados(self):
        import random as _random
        return _random.randint(1, self.__numeroDeLados)
    """ Aqui inicia nosso programa """
jogar = JogandoDados()
print(jogar.get_numeroDeLados())
for d in range(10):
    print(jogar.jogarDados(), end = " ")
print("========")
jogar.set_numeroDeLados(8)
print(jogar.get_numeroDeLados())
for d in range(5):
    print(jogar.jogarDados(), end = " ")
