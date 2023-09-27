import unittest
from Biblioteca import Biblioteca
from Biblioteca import Livro

class TestLivro(unittest.TestCase):
    def test_init_deve_passar(self):
        #Arrange
        nome = "Calibã e a bruxa"
        autor = "Silvia Federici"

        #Act
        livro = Livro(nome, autor)

        #Assert
        self.assertEqual(nome, livro.nome)
        self.assertEqual(autor, livro.autor)
        self.assertEqual(False, livro.esta_emprestado)

class TestBiblioteca(unittest.TestCase):
    def test_init_deve_passar(self):
        #Arrange / Act
        biblioteca = Biblioteca()

        #Assert
        self.assertIsInstance(biblioteca.livros, list)

    def test_adicionar_livro_deve_passar(self):
        #Arrange
        biblioteca = Biblioteca()
        nome_livro = "O mito da beleza"
        autor_livro = "Naomi Wolf"
        livro = Livro(nome_livro, autor_livro)

        #Act
        biblioteca.adicionar_livro(livro)
        
        #Assert
        self.assertEqual(1, len(biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        biblioteca = Biblioteca()
        livro = 1988

        # Act / Assert
        with self.assertRaises(TypeError):
            biblioteca.adicionar_livro(livro)

    def test_exibir_livros_deve_passar(self):
        # Arrange
        self.biblioteca.livros = ["Lista de livors"]
        lista = self.biblioteca.livros

        #Act
        self.biblioteca.exibir_livros()

        # Assert
        self.assertEqual(lista, ["Lista de livors"])

    def test_emprestar_livro_deve_passar(self):

        # Arrange
        nome = "O mito da beleza"
        autor = "Naomi Wolf"
        livro = Livro(nome, autor)
        self.biblioteca.livros = ["O mito da beleza", "Torto Arado"]
        lista_livros = self.biblioteca.livros

        # Act
        self.biblioteca.emprestar_livro(livro)

        # Assert
        self.assertTrue(livro.nome in lista_livros)

    def test_emprestar_livro_inexistente_deve_passar(self):
        # Arrange
        nome = "Livro inexistente"
        autor = "Ninguém"
        livro = Livro(nome, autor)
        self.biblioteca.livros = ["O mito da beleza", "Torto Arado"]
        lista_livros = self.biblioteca.livros

        #Act
        self.biblioteca.emprestar_livro(livro)

        # Assert
        self.assertTrue(livro.nome not in lista_livros)
