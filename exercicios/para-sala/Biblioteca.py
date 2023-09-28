from Livro import Livro

class Biblioteca :
    """Classe biblioteca.
    
    Para instanciar a classe utilize o exemplo:

    biblitoeca = Biblioteca()
    """
    def __init__(self):
        self.livros = []
        """Propriedade livros do tipo Lista"""
    
    def adicionar_livro(self, livro: Livro):
        """Método adicionar_livro da classe Biblitoeca
        
        Recebe o parâmetro livro do tipo da classe Livro e
        adiciona na propriedade livros

        Retorna exceção caso o parâmetro recebido não seja do tipo Livro
        """
        if (not isinstance(livro, Livro) ):
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)   

    def lista_exibir (self):
        for index in  self.livros :
            return index    


    def emprestar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                 livro.esta_emprestado = true
                 return True
            return False

