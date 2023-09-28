from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro)):
            raise TypeError(f"Esperado livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)

    def exibir_livro(self):
        return self.livros

    def emprestar_livro(self, livro: Livro):
        if livro.esta_emprestado == True:
            return(f"O livro que você solicitou não está disponível")
        elif livro.esta_emprestado:
            return(f"O livro que você você solicitou está disponível")
        else:
            raise TypeError("Este livro não consta na nossa base de dados")
