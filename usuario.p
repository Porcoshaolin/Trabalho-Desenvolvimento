from pessoa import Pessoa

class Usuario:
    def __init__(self, nome: strsenha: str):
        super().__init__(nome)
        if isinstance(senha, str):
            self.__senha = senha

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, senha):
        if isinstance(senha, str):
            self.__senha = senha
