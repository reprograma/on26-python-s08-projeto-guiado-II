
from Livro import Livro

class Biblioteca:
    
    def __init__(self):
        #self.livros = [], mudou pra:
        nome_livro = 'initNome'
        autor_livro = 'initAutor'
        livro = Livro(nome_livro, autor_livro)
        self.livros = [livro.nome]
        #testar

    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro)):
            raise TypeError(f'Esperado Livro, obtido valor {livro} do tipo {type(livro)}')
        self.livros.append(livro)


    def exibir_livro(self):
        lista_livros = self.livros
        print(lista_livros)

    def emprestar_livro(self, nome_livro):
         for livro in self.livros:
            if livro['nome'] == nome_livro:
                livro['emprestado'] = True
                break
