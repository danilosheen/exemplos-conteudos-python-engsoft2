from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, dataNascimento, nomePai, nomeMae, debitos, compras):
        super().__init__(nome, dataNascimento, nomePai, nomeMae)
        self.__debitos = debitos
        self.__compras = compras


    def getDebito(self):
        return self.__debitos

    def getCompras(self):
        return self.__compras


    def setDebito(self, debitos):
        self.__debitos = debitos