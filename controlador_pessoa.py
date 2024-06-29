from tela_pessoa import TelaPessoa
from pessoa import Pessoa
from controlador_geral import ControladorGeral
from pessoa_dao import PessoaDAO


class ControladorPessoa:

    def __init__(self, controlador_geral):
        self.__pessoa_dao = PessoaDAO
        if isinstance(controlador_geral, ControladorGeral):
            self.__controlador_geral = controlador_geral
        self.__tela_pessoa = TelaPessoa()

    def achar_pessoa(self, nome: str):
        for pessoa in self.__pessoa_dao_get_all:
            if(nome is not None and pessoa.nome == nome):
                return pessoa
        return None

    def listar_pessoa(self):
        dados_pessoas = self.listar_todas_pessoas()
        self.__tela_pessoa.mostrar_pessoa(dados_pessoas)

    def listar_todas_pessoas(self):
        return [{"nome": pessoa.nome} for pessoa in self.__pessoa_dao.get_all()]

    def adicionar_pessoa(self):
        dados_pessoa = self.__tela_pessoa.pegar_pessoa()
        p = self.achar_pessoa(dados_pessoa["nome"])


        if p is None:
            pessoa = Pessoa(dados_pessoa["nome"])
            self.__pessoa_dao.add(pessoa)
            self.__tela_pessoa.mostrar_mensagem("Pessoa adicionada com sucesso.")
        else:
            self.__tela_pessoa.mostrar_mensagem("Não é possível adicionar uma pessoa já cadastrada.")

    def adicionar_fornecedor_pagador(self, nome): #Uso para controlador movimentação
        p = self.achar_pessoa(nome)
        if p is None:
            pessoa = Pessoa(nome)
            self.__pessoa_dao.add(pessoa)
            return pessoa
        return p

    def excluir_pessoa(self):
        self.listar_pessoa()
        p = self.__tela_pessoa.selecionar_pessoa()
        pessoa = self.achar_pessoa(p)

        if pessoa is not None:
            self.__pessoa_dao.remove(pessoa)
            self.__tela_pessoa.mostrar_mensagem("'Pessoa' excluída com sucesso.")
            self.listar_pessoa()
        else:
            self.__tela_pessoa.mostrar_mensagem("Não é possível excluir uma pessoa inexistente")

    def alterar_pessoa(self):
        self.listar_pessoa()
        p = self.__tela_pessoa.selecionar_pessoa()
        pessoa = self.achar_pessoa(p)

        if pessoa is not None:
            nova_pessoa = self.__tela_pessoa.pegar_pessoa()
            pessoa.nome = nova_pessoa["nome"]
            self.__tela_pessoa.mostrar_mensagem("Pessoa alterada com sucesso.")
            self.listar_pessoa()
        else:
            self.__tela_pessoa.mostrar_mensagem("Não é possível alterar uma pessoa inexistente.")

    def alterar_fornecedor_pagador(self, nome): #Uso para controlador movimentação
        self.listar_pessoa()
        pessoa = self.achar_pessoa(nome)
        if pessoa is not None:
            return pessoa
        else:
            return None

    def retornar(self):
        self.__controlador_geral.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.listar_pessoa, 2: self.adicionar_pessoa, 3: self.alterar_pessoa,
                            4: self.excluir_pessoa, 5: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()
