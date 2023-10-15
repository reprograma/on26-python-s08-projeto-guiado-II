#não é obrigatorio#
 
from Biblioteca import Biblioteca 
from Livro import Livro 

nome_livro = "O mito da beleza"
autor_livro = "Naomi Wolf"
livro_objeto = Livro(nome = nome_livro,autor = autor_livro)

biblioteca_objeto = Biblioteca()


print(biblioteca_objeto.livros)

biblioteca_objeto.adicionar_livro(livro_objeto)

for livro in biblioteca_objeto.livros:
    print(livro.nome)
    print(livro.autor)