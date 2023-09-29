from livro import Livro

class Biblioteca:
    
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        if not isinstance(livro, Livro):
            raise TypeError(f'Esperado Livro, obtido valor {livro} do tipo {type(livro)}')
        self.livros.append(livro)

    def exibir_livros(self):
            return self.livros
        
    def emprestar_livro(self, livro: Livro):
        if livro not in self.livros:
            raise NameError(f'Livro não existe na lista.')
        
        elif livro in self.livros and livro.isBorrowed == True:
            print(f'{livro.nome} já está emprestado.')
            return livro.isBorrowed
        else:
            livro.isBorrowed = True
            print (f'{livro.nome} Foi emprestado.')
            return livro.isBorrowed

    def remover_livro(self, livro: Livro):
        if livro.isBorrowed == True:
            return (f'{livro.nome} está emprestado e portando não pode ser removido.')
        
        elif livro.isBorrowed == False:
            self.livros.remove(livro)
        
        elif livro not in self.livros:
            raise ValueError(f'{livro.nome} não consta da lista.')

    def devolver_livro(self, livro: Livro):
        if livro not in self.livros:
            raise ValueError(f'Livro não existe na lista.')
        
        elif livro in self.livros and livro.isBorrowed == False:
            print(f'{livro.nome} já foi devolvido.')
            return livro.isBorrowed
        
        else:
            livro.isBorrowed = False
            print (f'{livro.nome} Foi devolvido.')
            return livro.isBorrowed
            
    def buscar_livro(self, livro: Livro):
        if livro not in self.livros:
            raise ValueError(f'{livro.nome} não encontrado.')
        elif livro in self.livros and livro.isBorrowed == True:
            return f'{livro.nome}, de {livro.autor}, está emprestado.'
        elif livro in self.livros and livro.isBorrowed == False:
            return f'{livro.nome}, de {livro.autor}, está disponível.'