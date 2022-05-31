import Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, dataNascimento, nomePai, nomeMae, salario, setor):
        super().__init__(nome, dataNascimento, nomePai, nomeMae)
        self._salario = salario
        self._setor = setor