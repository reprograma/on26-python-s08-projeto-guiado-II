class Livro:
    def __init__(self, titulo, autor):
        self.titulo= titulo
        self.autor = autor
        self.esta_emprestado = False
        self.devolvido = True
        #raise NotImplemented