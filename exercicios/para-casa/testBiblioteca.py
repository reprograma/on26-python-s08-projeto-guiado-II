from unittest import TestCase # de dentro de unittest importamos a ferramenta TestCase

from Livro import Livro # de dentro do módulo livro importamos a classe livro
from Biblioteca import Biblioteca # de dentro do modulo bibliteca a classe biblioteca

class TestBiblioteca(TestCase): # criando uma classe de teste biblioteca que vai usar a ferramenta testCase
    def setUp(self): # setup é usado para abreviar uma função grande
         self.biblioteca = Biblioteca() #acessando a varável biblioteca e atribuindoa classe

    def test_init_deve_passar(self):  # o __INIT__ é chamado de consultor, ele permite e dar inicio os métodos e propriedades 
        # Arrange / Act 
        #biblioteca = Biblioteca()

        #  Assert
        self.assertIsInstance(self.biblioteca.livros, list) # testando se os livros da biblioteca estão associados a uma lista
    def test_adicionar_livro_deve_passar(self): 

        # Arrange 
        #biblioteca = Biblioteca()
        nome_livro = "Bunker"
        autor_livro = "Kevin Brooks"
        ano = 2002
        livro = Livro(nome_livro, autor_livro, ano) 

        # Act
        self.biblioteca.adicionar_livro(livro)
        
        # Assert 
        self.assertEqual(1, len(self.biblioteca.livros))  #

    # def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        #biblioteca = Biblioteca()
        #   livro = 1988

        # Act
        #self.biblioteca.adicionar_livro(livro) # essa função está sendo chamada na linha 38

        # Assert
       # with self.assertRaises(TypeError):
        #    self.biblioteca.adicionar_livro(livro) 

    # def test_init_exibir_livros_vazio(self): # o self aparece dentro de todas as funções que 
    #     lista_vazia = Biblioteca() #criando uma nova variável chamada lista vazia que recebe o módulo biblioteca
    #     livros_listados = lista_vazia.exibir_livro() #
    #     self.assertEqual(0, len(livros_listados)) == 0 # os dois == e o zero garante que a lista está vazia fazem(que a lista é do tamanho de zero que é iguala zero)

    # def test_init_exibir_livros(self):
    #     lista = Biblioteca()  
    #     lista.adicionar_livro(Livro("Bunker", "Keven Brooks", 2002))
    #     relacao = lista.exibir_livro()
    #     self.assertEqual(1, len(relacao))  #relação é os livros disponíveis para exibir
    #     self.assertEqual(relacao[0].nome, "Bunker")
    #     self.assertEqual(relacao[0].autor, "Keven Brooks")
    #     self.assertEqual(relacao[0].ano, 2002)


        #fazer devolução
    def test__initt__devolver_livro(self):
        lista_devolucao = Biblioteca()  # a class aqui é biblioteca de onde tiraremos as informações para 
        lista_devolucao.devolver_livro(Livro("Bunker", "Keven Brooks", 2002))
        self.assertEqual(lista_devolucao[1].nome, "Bunker")
        self.assertEqual(lista_devolucao[1].autor, "Keven Brooks")
        self.assertEqual(lista_devolucao[0].ano, 2002)
        ## será que deveria ter um return?##

        ####### MAIS PRA FRENTE EU VOLTO PRA FAZER OS DEMAIS\ºº/######
        # nome_livro = "livro_auto_ajuda" , "livro_como_ficar_milionario"
        # autor_livro = "João" , "Fernanda"
        #livro_auto_ajuda = livro_auto_ajuda(nome_livro, autor_livro)
       # livro_como_ficar_milionario = livro_como_ficar_milionario(nome_livro, autor_livro)
       # return nome_livro - str(self.livro_auto_ajuda, livro_como_ficar_milionario)
    
        #self.livro_como_ficar_milionario = livro_como_ficar_milionario
           

