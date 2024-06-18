from limite.tela_usuario import TelaUsuario
from entidade.usuario import Usuario
from controle.controlador_geral import ControladorGeral
from usuario_dao import UsuarioDao


class ControladorUsuario:

    def __init__(self, controlador_geral):
        self.__pessoa_dao = UsuarioDAO
        if isinstance(controlador_geral, ControladorGeral):
            self.__controlador_geral = controlador_geral
        self.__tela_usuario = TelaUsuario()

    def achar_usuario(self, nome: str):
        if isinstance(nome, str):
            for usuario in self.__usuario_dao_get_all:
                if usuario.nome == nome:
                    return usuario
            return None

    def cadastrar_usuario(self):
        dados_usuario = self.__tela_usuario.pegar_usuario()
        u = self.achar_usuario(dados_usuario["nome"])
        if u is None:
            usuario = Usuario(dados_usuario["nome"], dados_usuario["senha"])
            self.__usuario.append(usuario)
            self.__tela_usuario.mostrar_mensagem("Cadastro realizado com sucesso!")
            self.login()
        else:
            self.__tela_usuario.mostrar_mensagem("Usuário já cadastrado no sistema, por favor, faça o login.")

    def login(self):
        dados_usuario = self.__tela_usuario.pegar_usuario()
        usuario = self.achar_usuario(dados_usuario["nome"])
        if usuario is not None:
            if usuario.senha == dados_usuario["senha"]:
                self.__controlador_geral.usuario_logado = usuario
                self.__controlador_geral.abrir_tela()
            else:
                self.__tela_usuario.mostrar_mensagem("Senha incorreta, por favor, tente novamente")
        else:
            self.__tela_usuario.mostrar_mensagem("Usuário não cadastrado, por favor, primeiramente, realize o cadastro.")

    def alterar_senha(self):
        dados_usuario = self.__tela_usuario.pegar_senha()
        usuario = self.achar_usuario(dados_usuario["nome"])
        if usuario is not None:
            nova_senha = dados_usuario["senha"]
            usuario.senha = nova_senha
            self.__tela_usuario.mostrar_mensagem("Senha alterada com sucesso.")
        else:
            self.__tela_usuario.mostrar_mensagem("Usuário não encontrado.")

    def abrir_tela(self):
        lista_opcoes = {1: self.login, 2: self.alterar_senha, 3: self.cadastrar_usuario}
        continua = True
        while continua:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()
