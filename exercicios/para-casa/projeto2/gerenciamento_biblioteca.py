class Livro:
    def __init__(self, nome, autor, data_lancamento, editora):
        self.nome = nome
        self.autor = autor
        self.data_lancamento = data_lancamento
        self.editora = editora
        self.esta_emprestado = False

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def exibir_lista(self):
        return self.livros

    def emprestar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                livro.esta_emprestado = True

    def remover_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro and not livro.esta_emprestado:
                self.livros.remove(livro)

    def buscar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                disponibilidade = "Sim" if not livro.esta_emprestado else "Não"
                return f"Livro: {livro.nome}, Autor: {livro.autor}, Data de Lançamento: {livro.data_lancamento}, Editora: {livro.editora}, Disponível: {disponibilidade}"
        return "Livro não encontrado"

    def devolver_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                livro.esta_emprestado = False
                return


