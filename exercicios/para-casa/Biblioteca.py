from livro import Livro

class Biblioteca :
    def __init__(self):
        self.livros = []

    #Adicionando o livro
    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro)):
            raise TypeError(f"Esoerado Livro obtido valor {livro} do tipo {type(livro)}")

        self.livros.append(livro)

    #Removendo o livro
    def remover_livro(self, nome_livro):
        livro_removido = False
        for livro in self.livros:
            if livro.nome == nome_livro:
                self.livros.remove(livro)
                livro_removido = True
        
        if not livro_removido:
            raise ValueError (f"O livro {nome_livro} não existe na biblioteca!")
    
    #Pesquisar livro
    def pesquisar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                return livro 
    


        
        