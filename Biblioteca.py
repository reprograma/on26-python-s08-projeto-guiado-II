from Livro import Livro 
class Biblioteca :
   def __init__(self):
        
        self.livros = []

   def adicionar_livro(self, livro: Livro):
      if(not isinstance (livro, Livro)): #funçao de atribuição - #not= não é do tipo livro dará um erro...
         raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
      self.livros.append(livro) 

   def exibir_livro(self,livro_auto_ajuda, livro_como_ficar_milionario):
      