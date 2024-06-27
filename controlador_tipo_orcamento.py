from limite.tela_tipo_orcamento import TelaTipoOrcamento
from entidade.tipo_orcamento import TipoOrcamento
from controle.controlador_geral import ControladorGeral
from persistencia.tipo_orcamento_dao import TipoOrcamentoDAO


class ControladorTipoOrcamento:

    def __init__(self, controlador_geral):

        self.__tipo_dao = TipoOrcamentoDAO()
        if isinstance(controlador_geral, ControladorGeral):
            self.__controlador_geral = controlador_geral
        self.__tela_tipo_orcamento = TelaTipoOrcamento()

    def achar_tipo(self, categoria: str):
        for tipo in self.__tipo_dao.get_all():
            if (categoria is not None and tipo.categoria == categoria):
                return tipo
        return None

    def listar_tipo(self):
        dados_tipos = self.listar_todos_tipos()
        self.__tela_tipo_orcamento.mostrar_tipo(dados_tipos)

    def listar_todos_tipos(self):
        return [{"categoria": tipo.categoria} for tipo in self.__tipo_dao.get_all()]

    def adicionar_tipo(self):
        dados_tipo_orcamento = self.__tela_tipo_orcamento.pegar_tipo()
        if dados_tipo_orcamento is None:
            return
        t = self.achar_tipo(dados_tipo_orcamento["categoria"])
        if t is None:
            tipo_orcamento = TipoOrcamento(dados_tipo_orcamento["categoria"])
            self.__tipo_dao.add(tipo_orcamento)
            self.__tela_tipo_orcamento.mostrar_mensagem("Categoria adicionada com sucesso.")
        else:
            self.__tela_tipo_orcamento.mostrar_mensagem("Não é possível adicionar uma categoria já cadastrada.")

    def adicionar_categoria(self, tipo): #Uso para controle movimentação e controle orçamento
        t = self.achar_tipo(tipo)
        if t is None:
            tipo_orcamento = TipoOrcamento(tipo)
            self.__tipo_dao.add(tipo_orcamento)
            return tipo_orcamento
        return t

    def excluir_tipo(self):
        dados_tipos = self.listar_todos_tipos()
        tipo = self.__tela_tipo_orcamento.selecionar_categoria(dados_tipos)
        if tipo is None:
            return
        tipo_orcamento = self.achar_tipo(tipo)

        if tipo_orcamento is not None:
            self.__tipo_dao.remove(tipo_orcamento)
            self.__tela_tipo_orcamento.mostrar_mensagem("Categoria excluída com sucesso.")
            self.listar_tipo()
        else:
            self.__tela_tipo_orcamento.mostrar_mensagem("Não é possível excluir uma categoria inexistente")

    def alterar_tipo(self):
        dados_tipos = self.listar_todos_tipos()
        tipo = self.__tela_tipo_orcamento.selecionar_categoria(dados_tipos)
        if tipo is None:
            return
        tipo_orcamento = self.achar_tipo(tipo)

        if tipo_orcamento is not None:
            novo_tipo = self.__tela_tipo_orcamento.pegar_tipo(tipo_orcamento.categoria)
            if novo_tipo is None:
                return
            tipo_orcamento.categoria = novo_tipo["categoria"]
            self.__tela_tipo_orcamento.mostrar_mensagem("Categoria alterada com sucesso.")
            self.listar_tipo()
        else:
            self.__tela_tipo_orcamento.mostrar_mensagem("Não é possível alterar uma categoria inexistente.")

    def achar_categoria(self, tipo): #Uso para controle movimentação e controle orçamento
        tipo_orcamento = self.achar_tipo(tipo)
        if tipo_orcamento is not None:
            return tipo_orcamento
        else:
            return None

    def retornar(self):
        self.__controlador_geral.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.listar_tipo, 2: self.adicionar_tipo, 3: self.alterar_tipo,
                            4: self.excluir_tipo, 5: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_tipo_orcamento.tela_opcoes()]()
