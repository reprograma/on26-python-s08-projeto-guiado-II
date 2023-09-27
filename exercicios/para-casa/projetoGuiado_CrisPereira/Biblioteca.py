# Exercício Cris Pereira - semana 08
from Livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro)):
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)   

# Novas funcionalidades abaixo 
    def exibir_livros(self):
       return self.livros
    
    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.nome == titulo and not livro.esta_emprestado:
                livro.esta_emprestado = True

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.nome == titulo:
                self.livros.remove(livro)

    def buscar_livro(self, titulo):
        mensagem = "Livro não encontrado."
        for livro in self.livros:
            if livro.nome == titulo:
                mensagem = livro
        return mensagem
    
    def devolver_livro(self, titulo):
        mensagem = "Livro não encontrado."
        for livro in self.livros:
            if livro.nome == titulo:
                livro.esta_emprestado = False
                mensagem = f"Livro devolvido: {livro}"
        return mensagem