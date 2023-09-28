from Livro import Livro

class Biblioteca:
    def __init__(self):
       self.livros = []
       #raise NotImplementedError
       
    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro)):
            raise TypeError(f'Esperado Livro obtido valor {livro} do tipo {type(livro)}')
        self.livros.append(livro)

#resolução projeto
    def exibir_livro(self):
        return self.livros

        
    def emprestar_livro(self, nome_livro):
        #return (self.nome, self.autor)
        for livro in self.livros:
            if livro.nome == nome_livro:
                 livro.esta_emprestado = True
            else:
                return ("Livro indisponível")

       

