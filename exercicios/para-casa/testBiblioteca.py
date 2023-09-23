from unittest import TestCase
from biblioteca import Biblioteca #do arquivo biblioteca está importando a classe Biblioteca
from livro import Livro

class TestBiblioteca(TestCase):

    def test_init_deve_passar(self):
        # Arrange / Act
        biblioteca = Biblioteca()

        # Assert
        self.assertIsInstance(biblioteca.livros, list)
    
    def test_adicionar_Livro_deve_passar(self):
        # Arrange
        biblioteca = Biblioteca()
        livro = Livro()

    
        # Act
        biblioteca.adicionar_livro()

        # Assert
