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

    def setUp(self):
        self.biblioteca = Biblioteca()

    #Testa se livros é do tipo lista
    def test_init_deve_passar(self):
        #Assert
        self.assertIsInstance(self.biblioteca.livros, list)

    #Testa se 1 livro foi adicionado à lista de livros
    def test_adicionar_livro_deve_passar(self):
        #Arrange
        nome_livro = "O mito da beleza"
        autor_livro = "Naomi Wolf"
        livro = Livro(nome_livro, autor_livro)
        #Act
        self.biblioteca.adicionar_livro(livro)
        #Assert
        self.assertEqual(1, len(self.biblioteca.livros))

    #Testa se o sistema vai bloquear a inserção de números no lugar de objetos.
    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        livro = 1988
        # Act / Assert
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)

    #Testa se o método exibir_livros vai retornar uma lista 
    def test_exibir_livros_deve_passar(self):
        # Arrange
        self.biblioteca.livros = ["Livro 1", "Livro 2"]
        lista = self.biblioteca.livros
        #Act
        self.biblioteca.exibir_livro()
        # Assert
        self.assertEqual(lista, ["Livro 1", "Livro 2"])

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
