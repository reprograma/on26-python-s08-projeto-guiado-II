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
        lista_livros = self.livros
        if livro.nome not in lista_livros:   
            print(f'Este livro não existe em nossa lista.')
        else:
            if livro.estaEmprestado == True:
                print(f'{livro.nome} já está emprestado.')
            else:
                print(f'{livro} está disponível. Obrigada por utilizar nossos serviços!')
                livro.estaEmprestado = True    