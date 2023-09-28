from biblioteca import Biblioteca
from livro import Livro
from testBiblioteca import TestBiblioteca


livro_objeto = Livro(nome="Torto Arado", autor="Itamar Vieira", emprestado=False)
livro2_objeto = Livro(nome="Entendendo algoritmo", autor="Aditya", emprestado=False)
biblioteca_objeto = Biblioteca()
lista = [livro_objeto,livro2_objeto]
for livro in lista:
    biblioteca_objeto.add_livro(livro)


for livros in biblioteca_objeto.exibir_livros():
    print(f"Nome: {livros.nome}  Autor:  {livros.autor} Emprestado:  {livros.emprestado}")

emprestar = biblioteca_objeto.emprestar_livro(livro_objeto)
if(emprestar.emprestado == True):
    print(f"O Livro: {emprestar.nome} foi emprestado com sucesso")



