from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livro = []
        
    def add_livro(self, livro: Livro):
        if (isinstance(livro,Livro) == False):
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo{type(livro)}")
        self.livro.append(livro)
    
    def exibir_livros(self):
        if len(self.livro) == 0: #verifica se a list esta vzia
         raise TypeError("Lista Vazia") 
        else:  return self.livro 
        
    def emprestar_livro(self, livro: Livro):
        if(livro.emprestado == True):
          raise TypeError("Esse livro ja esta emprestado") 
        else:
         livro.emprestado = True
        return livro

    def devolver_livro(self, livro: Livro):
        if(livro.emprestado == False):
          raise TypeError("Este livro encotra-se na biblioteca") 
        else:
         livro.emprestado = False
        return livro
        
    