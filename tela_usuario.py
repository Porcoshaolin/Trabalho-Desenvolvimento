import PySimpleGUI as sg
from limite.tela import Tela


class TelaUsuario(Tela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.__window.Read()
        opcao = 0
        if button == '1':
            opcao = 1
        if button == '2':
            opcao = 2
        if button == '3':
            opcao = 3
        self.close()
        return opcao

    def init_opcoes(self):

        sg.ChangeLookAndFeel('DarkGray16')

        layout = [
            [sg.Button('Fazer login', size=(30, 1), key='1')],
            [sg.Button('Esqueci a senha', size=(30, 1), key='2')],
            [sg.Button('Sou novo usuário, quero me cadastrar', size=(30, 1), key='3')],
        ]

        self.__window = sg.Window('Menu Usuário', resizable=True).Layout(layout)

    def pegar_usuario(self):
        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
                [sg.Text('Nome', size=(15,1)), sg.InputText('', key='nome')],
                [sg.Text('Senha', size=(15,1)), sg.InputText('', key='senha')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro/Login').Layout(layout)

        button, values = self.open()

        if button == 'Cancelar':
            self.close()
            self.tela_opcoes()

        nome = values['nome']
        senha = values['senha']
        self.close()
        return {"nome": nome, "senha": senha}

    def pegar_senha(self):
        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
                [sg.Text('Usuário:', size=(15,1)), sg.InputText('', key='nome')],
                [sg.Text('Nova Senha:', size=(15,1)), sg.InputText('', key='senha')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Nova Senha').Layout(layout)

        button, values = self.open()

        if button == "Cancelar":
            self.tela_opcoes()

        nome = values['nome']
        senha = values['senha']
        self.close()
        return {"nome": nome, "senha": senha}

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values












