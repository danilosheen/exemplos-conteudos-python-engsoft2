from Pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, dataNascimento, nomePai, nomeMae, salario, setor):
        super().__init__(nome, dataNascimento, nomePai, nomeMae)
        self.__salario = salario
        self.__setor = setor


    def getSetor(self):
        return self.__setor

    def getSalario(self):
        return self.__salario


    def setSetor(self, setor):
        self.__setor = setor