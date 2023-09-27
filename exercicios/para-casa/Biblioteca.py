from Livro import Livro

class Biblioteca :
    def __init__(self):
        self.livros = [] # propriedade declarada

    def adicionar_livro(self, livro: Livro): # o parametrô livro é do tipo classe Livro
        # raise NotImplementedError -> não precisamos mais do método de exceção pois agora temos um comportamento:
        if (not isinstance(livro, Livro)):
            raise TypeError('mensagem de erro') 
        self.livros.append(livro)

    def exibir_livro(self, livro: Livro):
        # raise NotImplementedError
        self.livros = []
        print(livro)

    def emprestar_livro(self):
        if self.emprestar_livro is False:
            return

        self.emprestar_livro = True
        print('O livro {} não está disponível para empréstimo')
        # raise NotImplementedError

