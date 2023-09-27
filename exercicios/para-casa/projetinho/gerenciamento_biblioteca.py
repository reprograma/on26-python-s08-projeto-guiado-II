#Atividade realizada com a ajuda de Thaysa Lima
class Livro:
    def _init_(self, nome, autor, data_lancamento, editora):
        self.nome = nome
        self.autor = autor
        self.data_lancamento = data_lancamento
        self.editora = editora
        self.esta_emprestado = False

class Biblioteca:
    def _init_(self):
        self.livros = []
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    def exibir_lista(self):
        return self.livros
    def emprestar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                livro.esta_emprestado = True