from livros_daninegrao import Livros

class Biblioteca:
    def __init__(self):
        self.livros = []
        
    def adicionar_livros(self, livros: Livros):
        if (not isinstance(livros, Livros)):
            raise TypeError(f"Esperado livros obtido valor{livros} do tipo {type(livros)}")
        self.livros.append(livros)
        
    def exibir_livro(self, nome_livro):
        livros_encontrados = []
        for livro in self.livros:
            if livro.nome == nome_livro:
                livros_encontrados.append(livro)
        return livros_encontrados

    def emprestar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                self.livros.remove(livro)
                return livro
    
    