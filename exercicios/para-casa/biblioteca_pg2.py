from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []
        
    def adicionar_livro(self, livro: Livro):
        if(not isinstance(livro, Livro)):
            raise TypeError(f"Esperado livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)

    def exibir_livros(self, livro: Livro):
        #if 
        return self.livros
    
    def emprestar_livro(self, livro):
        if livro in self.livros:
            return True
        else:
            return False
    
"""
    def buscar_livro(self, livro: Livro):
        if(not isinstance(livro, Livro)):
            raise TypeError("Esse livro não faz parte do nosso acervo")
        return self.livros
    


    def buscar_livros(self):
        id_livro = input("Digite o nome do livro desejado:")
        for livro in self.livros:
            if livro["nome"] == id_livro:
                print(f"O livro xxx de id xxx, está na rua xx, prateleira x.")
            return
        print("Não possuimos este livro em nossa biblioteca.")
    """