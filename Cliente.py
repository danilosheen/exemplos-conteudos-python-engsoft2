import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, dataNascimento, nomePai, nomeMae, debitos, compras):
        super().__init__(nome, dataNascimento, nomePai, nomeMae)
        self._debitos = debitos
        self._compras = compras