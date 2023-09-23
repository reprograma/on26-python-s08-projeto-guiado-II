from livro import Livro

class Biblioteca :
    def __init__(self):
        self.livros = []
        
    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro)):
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)
        
