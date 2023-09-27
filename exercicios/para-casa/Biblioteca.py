from Livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro: Livro):
        if(not isinstance(livro, Livro)):
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)
        #raise NotImplementedError
    def exibir_livros(self):
        return self.livros         
        #raise NotImplementedError

    def emprestar_livro(self, nome, livro: Livro):
        for livro in self.livros:
            if livro.nome == nome:
                livro.esta_emprestado = True
                break
    
    def remover_livro(self, nome, livro: Livro):
        for livro in self.livros:
            if livro.nome == nome:
                self.livros.remove(livro)
            
                
        

        