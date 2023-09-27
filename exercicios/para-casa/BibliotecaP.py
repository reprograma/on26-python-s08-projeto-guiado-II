from Livro import Livro
class Biblioteca:
    def __init__(self):
        self.livros=[]
        #raise NotImplemented

    def adicionar_livro(self, livro: Livro):
        #raise NotImplementedError 
        if (not isinstance(livro, Livro)): #qual o tipo desse parametro
            raise TypeError(f"Esperado livro{livro} do tipo {type(livro)}")
        self.livros.append(livro)

    def listar_livros(self):
        return self.livros
    
    def emprestar_livros(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.esta_emprestado = True
                return livro
        return None   
    
    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.devolvido = True
                return livro
        return None
        

    