from Livro import Livro 
class Biblioteca :
    
    def __init__ (self):
        self.livros = []
        
    def adicionar_livro (self,livro:Livro):
        if (not isinstance (livro, Livro)):
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)
    def listar_livro(self):
       for i in self.livros:
           return i
    def emprestar_livro (self,nome: Livro):
        for i  in self.livros:
            if i.nome == nome:
                i.esta_emprestado == True
                return True
            return False
    def remover_livro(self,nome:Livro):
        for i  in self.livros:
            if i == nome: 
                self.livros.remove(i)
            
          
    
        
    
         