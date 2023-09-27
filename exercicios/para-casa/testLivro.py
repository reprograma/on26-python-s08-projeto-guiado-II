from unittest import TestCase
from Livro import Livro

class TestLivro(TestCase):
    def test_init_deve_passar(self):
        # Arrange
        nome_livro = "A paixão segundo GH"
        autor_livro = "Clarice Lispector"
        # Act
        livro = Livro(nome_livro, autor_livro)
        # Assert
        self.assertEqual(nome_livro, livro.nome_livro)
        self.assertEqual(autor_livro, livro.autor_livro)
        self.assertEqual(False, livro.esta_emprestado)