class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.esta_emprestado = False
        self.esta_removido = False
        self.encontrado = False
        self.devolvido = False
    