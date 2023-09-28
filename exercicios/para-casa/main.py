from Biblioteca import Biblioteca
from Livro import Livro

nome_livro = "O vendedor de sonhos"
autor_livro = "Augusto Cury"
livro_objeto = Livro(nome = nome_livro, autor = autor_livro)

biblioteca_objeto = Biblioteca()

print(biblioteca_objeto.livros)

biblioteca_objeto.adicionar_livro(livro_objeto)

for livro in biblioteca_objeto.livros:
    print(livro.nome)
    print(livro.autor)

