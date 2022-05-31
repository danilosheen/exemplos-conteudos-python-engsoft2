class Pessoa:
    def __init__(self, nome, dataNascimento, nomePai, nomeMae):
        self.__nome = nome
        self.__dataNascimento = dataNascimento
        self.__nomePai = nomePai
        self.__nomeMae = nomeMae

    def getNome(self):
        return self.__nome

    def getDataNascimento(self):
        return self.__dataNascimento

    def getNomePai(self):
        return self.__nomePai

    def getNomeMae(self):
        return self.__nomeMae

    def setNome(self, nome):
        self.__nome = nome

    def setNome(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    def setNome(self, nomePai):
        self.__nomePai = nomePai

    def setNome(self, nomeMae):
        self.__nomeMae = nomeMae