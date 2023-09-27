from Livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        if not isinstance(livro, Livro):
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)

    def exibir_livros(self):
        return self.livros

    def emprestar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                livro.esta_emprestado = True
                return True
        return False
    
    def remover_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro and not livro.esta_emprestado:
                self.livros.remove(livro)
                return

    def buscar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                status = "emprestado" if livro.esta_emprestado else "disponível"
                return f"Nome: {livro.nome}, Autor: {livro.autor}, Status: {status}"
        return "Livro não encontrado"

    def devolver_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                livro.esta_emprestado = False
                return
        return "Livro não encontrado"