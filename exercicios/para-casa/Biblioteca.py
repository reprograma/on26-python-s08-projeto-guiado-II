from Livro import Livro

class Biblioteca : 
    def __init__(self): #Construtor 
        self.livros = [] #Lista de livros 
        
    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro) ):
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)        
    
    def exibir_livros(self):
        return self.livros

    def emprestar_livro(self, nome_do_livro):
        for livro in self.livros:
            if livro.nome == nome_do_livro:
                livro.esta_emprestado = True
                return True
            return False 
    