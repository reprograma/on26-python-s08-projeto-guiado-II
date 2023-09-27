# Sistema de biblioteca
    # Adicionar, listar e emprestar livros
from Livro import Livro

class Biblioteca:
    """Classe biblioteca"""
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro)):
            raise TypeError(f"Esperado do valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)

    def exibir_livros(self):
        return self.livros
    
    def emprestar_livros(self, livro: Livro):
        livro.esta_emprestado = True