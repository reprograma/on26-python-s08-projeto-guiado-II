from Livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro)):
            raise TypeError(f'Esperado Livro obtido valor {livro} do tipo {type(livro)}.')
        self.livros.append(livro)

    def exibir_livros(self):
            return self.livros

    def emprestar_livro(self, livro: Livro):
        if livro.emprestado == True:
            return(f'O livro não está disponível')
        elif livro.emprestado:
            return(f'Este livro está disponível.')
        else:
             raise TypeError ('Não temos este livro')
    
