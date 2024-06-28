import PySimpleGUI as sg
from tela import Tela


class TelaPessoa(Tela):
    self.__window = None
    self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if button == '1':
            opcao = 1
        elif button == '2':
            opcao = 2
        elif button == '3':
            opcao = 3
        elif button == '4':
            opcao = 4
        elif button == '5':
            opcao = 5
        else:
            opcao = None

    def init_opcoes(self, nome_pessoa=''):

        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
            [sg.Text('Informações de Pessoas', font=('Century Gothic', 25))],
            [sg.Text("Escolha uma das opções abaixo:", font=("Open Sans", 15), size=(30, 1))],
            [sg.Button("Listar pessoas", font=("Open Sans", 15), size=(30, 1), key='1')],
            [sg.Button("Adicionar pessoa", font=("Open Sans", 15), size=(30, 1), key='2')],
            [sg.Button("Alterar pessoa", font=("Open Sans", 15), size=(30, 1), key='3')],
            [sg.Button("Excluir pessoa", font=("Open Sans", 15), size=(30, 1), key='4')],
            [sg.Button("Retornar", font=("Open Sans", 15), size=(30, 1), key='5')
        ]

        self.__window = sg.Window('Opções em informação de pessoas', element_justification='c').Layout(layout)

def pegar_pessoa(self, nome_pessoa=''):

        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
            [sg.Text('Insira o nome da pessoa', font=("Open Sans", 12))],
            [sg.InputText(nome_pessoa, key='pessoa')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]

        ]

        self.__window = sg.Window('Opções em informação de pessoas', element_justification='c').Layout(layout)

        button, values = self.open()


def pegar_pessoa(self):
        nome = input("Nome: ")
        print("\n")
        if isinstance(nome, str) and nome is not None:
            return {"nome": nome}

    def mostrar_pessoa(self, dados_pessoa):
        print("Nome: ", dados_pessoa["nome"])

    def selecionar_pessoa(self):
        nome = input("Digite a pessoa que deseja selecionar: ")
        print("\n")
        if isinstance(nome, str) and nome is not None:
            return nome
