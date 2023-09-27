from Biblioteca_daninegrao import Biblioteca 
from livros_daninegrao import Livros 

nome_livro = "O mito da beleza"
autor_livro = "Naomi Wolf"
livro_objeto = Livros(nome = nome_livro, autor = autor_livro)

biblioteca_objeto = Biblioteca()


print(biblioteca_objeto.livros)

biblioteca_objeto.adicionar_livros(livro_objeto)

for livro in biblioteca_objeto.livros:
    print(livro.nome)
    print(livro.autor)