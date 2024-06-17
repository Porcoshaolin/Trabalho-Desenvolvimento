import PySimpleGUI as sg
from limite.tela import Tela

class TelaTipoOrcamento(Tela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if button == '1':
            opcao = 1
        if button == '2':
            opcao = 2
        if button == '3':
            opcao = 3
        if button == '4':
            opcao = 4
        if button == '5':
            opcao = 5

        self.close()
        return opcao

    def init_opcoes(self):

        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
                    [sg.Text('CATEGORIAS DE ORÇAMENTO', font=('Century Gothic', 25))],
                    [sg.Text("Escolha uma das opções abaixo:", font=("Open Sans",15), size=(30,1))],
                    [sg.Button("Listar categorias", font=("Open Sans",15), size=(30,1), key='1')],
                    [sg.Button("Adicionar categoria", font=("Open Sans",15), size=(30,1), key='2')],
                    [sg.Button("Alterar categoria", font=("Open Sans",15), size=(30,1), key='3')],
                    [sg.Button("Excluir categoria", font=("Open Sans",15), size=(30,1), key='4')],
                    [sg.Button("Retornar", font=("Open Sans",15), size=(30,1), key='5')]
        ]

        self.__window = sg.Window('Categorias orçamentárias', element_justification='c').Layout(layout)

    def pegar_tipo(self):

        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
                    [sg.Text('Categorias', font=("Helvica", 25))],
                    [sg.Text('Nome da categoria:', size=(15,1)), sg.InputText('', key='categoria')],
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Categorias orçamentárias', element_justification='c').Layout(layout)

        button, values = self.open()

        if button == 'Cancelar':
            self.close()
            self.tela_opcoes()

        categoria = values['categoria']
        if isinstance(categoria, str) and categoria is not None:
            self.close()
            return {"categoria": categoria}

    def mostrar_tipo(self, dados_tipo):
        string_todos_tipos = ''
        for dado in dados_tipo:
            string_todos_tipos = string_todos_tipos + "NOME DA CATEGORIA: " + dado["categoria"] + '\n'

        sg.Popup('LISTA DE AMIGOS', string_todos_tipos)

    def selecionar_categoria(self):

        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
                    [sg.Text('Selecionar Categoria', font=("Century Gothic", 25))],
                    [sg.Text('Selecione o nome da categoria:', font=("Helvica", 15))],
                    [sg.Text('Nome da categoria:', size=(15, 1)), sg.InputText('', key='categoria')],
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Selecionar categoria', element_justification='c').Layout(layout)

        button, values = self.open()

        if button == 'Cancelar':
            self.close()
            self.tela_opcoes()

        categoria = values['categoria']
        self.close()
        return categoria

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values














