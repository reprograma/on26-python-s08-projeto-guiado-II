from unittest import TestCase
from biblioteca import Biblioteca

class TesteBiblioteca(TestCase):
    def teste_init_deve_passar(self):
        # Arrange / act
        biblioteca = Biblioteca()

        # Assert
                #intância de livros
        self.assertIsInstance(biblioteca.livros, list)