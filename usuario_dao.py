from dao import DAO
from usuario import Usuario

class UsuarioDAO:

    def __init__(self):
        super().__init__('usuario.pkl')

    def add(self, usuario: Usuario):
        if isinstance(usuario, Usuario):
            super().add(usuario.senha, usuario)

    def remove(self, usuario: Usuario):
        if isinstance(usuario, Usuario):
            self.remove(usuario.senha)