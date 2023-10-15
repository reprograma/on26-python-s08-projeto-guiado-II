from Livro import Livro # o from vem de "tal" lugar...  do modulo livro importamos a classe livros
class Biblioteca: # criando uma nova biblioteca chamada livro
   def __init__(self): # método construtor INIT para definir as propriedades ou atribuições da nossa classe
        
      self.livros = [] # com a funçaõ self a gente vai acessar a variável livro associando a uma lista'[]

   def adicionar_livro(self, livro: Livro): # def é usado em uma ação(verbo no infinitvo) neste caso
      if(not isinstance (livro, Livro)): #funçao de atribuição - #not isinstace diz que o "livro" só existe mas n foi utilizado
         raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}") # o raise vai estourar essa exceção e vai passar a atribuir esse livro as ações
      self.livros.append(livro) # o append adiconar as "coisas" dentro de listas
  
   def exibir_livro(self): 
      return self.livros

      
