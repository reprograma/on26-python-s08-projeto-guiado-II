class Livro:
    """Classe livro"""
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.esta_emprestado = False