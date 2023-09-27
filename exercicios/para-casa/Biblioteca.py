from Livro import Livro

class Biblioteca :
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro)):
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)

    def exibir_livros(self):
        return self.livros   
    
    def emprestar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                livro.emprestado = True
                return True  # Se verdadeiro o livro foi emprestado com sucesso
        return False  # Se falso o livro não foi encontrado na biblioteca

    def remover_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro and not livro.emprestado:
                self.livros.remove(livro)
                return True  # Se verdadeiro  o livro foi removido com sucesso
        return False  # Se falso o livro não foi encontrado na biblioteca ou está emprestado
    
    def buscar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                status = "Disponível" if not livro.emprestado else "Emprestado"
                return f"Nome: {livro.nome}, Autor: {livro.autor}, Status: {status}"
        return "Livro não encontrado"

    def devolver_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                livro.emprestado = False
                return  # Livro foi devolvido com sucesso
        return "Livro não encontrado"