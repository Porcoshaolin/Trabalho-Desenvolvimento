from dao import DAO
from pessoa import Pessoa

class PessoaDAO:

    def __init__(self):
        super().__init__('pessoa.pkl')

    def add(self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa):
            super().add(pessoa.nome, pessoa)

    def remove (self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa):
            self.remove(pessoa.nome)