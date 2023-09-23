from unittest import TestCase
from biblioteca import Biblioteca #do arquivo biblioteca está importando a classe Biblioteca

class TestBiblioteca(TestCase):

    def test_init_deve_passar(self):
        # Arrange / Act
        biblioteca = Biblioteca()

        # Assert
        self.assertIsInstance(biblioteca.livros, list)
