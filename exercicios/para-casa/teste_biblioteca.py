from unittest import TestCase
from biblioteca_pg2 import Biblioteca
from livro import Livro

class TestBiblioteca(TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()

    def test_init_deve_passar(self):
        # Arrange / Act
        
        # Assert
        self.assertIsInstance(self.biblioteca.livros, list)

    def test_adicionar_livro_deve_passar(self):
        
        #Arrange / organizar os valores p/serem testados
        nome_livro = "O mito da beleza"
        autor_livro = "Naomi Wolf"
        livro = Livro(nome_livro, autor_livro)

        #Act / chamar a função q qro testar
        self.biblioteca.adicionar_livro(livro)

        # Assert / comparar o resultado da função com o valor q eu vou informar
        self.assertEqual(1, len(self.biblioteca.livros))

    
    def test_adicionar_livro_nao_deve_inserir_numero(self):
        #arrange
    
        livro = 1988

        #assert/act
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)

    def test_exibir_livros_deve_passar(self):
        # Arrange
        self.biblioteca.livros = ["Jessica"]
        nome_livro = "Jessica"
        autor_livro = "yy"
        livro = Livro(nome_livro , autor_livro)

        # Act
        self.biblioteca.exibir_livros(livro)

        # Assert
        self.assertEqual(["Jessica"], self.biblioteca.livros) #comparação do livro com biblioteca

    def test_emprestar_livro_deve_passar_ou_nao(self):
        #Arrange / organizar os valores p/serem testados
        self.biblioteca.livros = ["xxx"]
        nome_livro = "xxx"
        autor_livro = "RJ"
        livro = Livro(nome_livro, autor_livro)

        # Act / chamar a função q qro testar
        self.biblioteca.emprestar_livro(Livro)

        # Assert / comparar o resultado da função com o valor q eu vou informar
        self.assertTrue
        self.assertFalse

    """
    def test_buscar_livro_deve_passar_ou_nao(self):

        #Arrange / organizar os valores p/serem testados
        self.biblioteca.livros = ["WWW"]
        nome_livro = "WWW"
        autor_livro = "JR"
        livro = Livro(nome_livro, autor_livro)

        # Act / chamar a função q qro testar
        self.biblioteca.buscar_livro(self, livro, Livro)

        # Assert / comparar o resultado da função com o valor q eu vou informar
        self.assertIsInstance(self.biblioteca.livros, list)
        
        with self.assertRaises(TypeError):
            self.biblioteca.buscar_livro(livro)
"""