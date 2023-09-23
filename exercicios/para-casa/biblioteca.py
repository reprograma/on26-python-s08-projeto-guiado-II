from livro import Livro

class Biblioteca :
    def __init__(self):
        self.livros = []
        
    def adicionar_livro(self, livro: Livro):
        raise NotImplementedError
        