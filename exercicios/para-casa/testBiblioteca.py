from unittest import TestCase
from biblioteca import Biblioteca #do arquivo biblioteca está importando a classe Biblioteca
from livro import Livro

class TestBiblioteca(TestCase):

    def test_init_deve_passar(self):
        # Arrange / Act
        biblioteca = Biblioteca()

        # Assert
        self.assertIsInstance(biblioteca.livros, list)
    

    def test_adicionar_livro_deve_passar(self):
        # Arrange
        biblioteca = Biblioteca()
        livro = Livro("livro", "autor")

        # Act
        biblioteca.adicionar_livro(livro)

        # Assert
        self.assertEqual(1, len(biblioteca.livros))


    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        biblioteca = Biblioteca()
        livro = 1988

        # Act / Assert
        with self.assertRaises(TypeError):
            biblioteca.adicionar_livro(livro)
