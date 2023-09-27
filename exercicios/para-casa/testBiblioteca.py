from unittest import TestCase #Identificador de uma classe de testes
from Biblioteca import Biblioteca
from Livro import Livro

class TestBiblioteca(TestCase):
    #Utilizado para não precisar chamar a biblioteca em todas as funções
    def setUp(self):
        self.biblioteca = Biblioteca()

    def test_init_deve_passar(self):
        # Arrange / Act
        # Assert
        self.assertIsInstance(self.biblioteca.livros, list)

    def test_adicionar_livro_deve_passar(self):
        # Arrange 
        nome_livro = "O mito da beleza"
        autor_livro = "Naomi Wolf"
        livro = Livro(nome_livro, autor_livro)
        # Act
        self.biblioteca.adicionar_livro(livro)
        # Assert
        self.assertEqual(1, len(self.biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        livro = 1988

        # Act / Assert
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)

    def test_emprestar_livro_deve_passar(self):
        #Arrange
        livro = Livro("O mito da beleza", "Naomi Wolf")
        #Act
        self.biblioteca.adicionar_livro(livro)
        #Assert
        self.assertTrue(self.biblioteca.emprestar_livro("O mito da beleza"))
        self.assertTrue(livro.esta_emprestado)

    def test_emprestar_livro_inexistente_deve_retornar_false(self):
        #Act/Assert
        self.assertFalse(self.biblioteca.emprestar_livro("Livro Inexistente"))

    def teste_exibir_livros(self):
        #Arrange
        livro1 = Livro("Uzumaki", "Junji Ito")
        livro2 = Livro("Tomie", "Junji Ito")
        #Act
        self.biblioteca.adicionar_livro(livro1)
        self.biblioteca.adicionar_livro(livro2)
        livros = self.biblioteca.exibir_livros()
        #Assert
        self.assertIn(livro1, livros)
        self.assertIn(livro2, livros)