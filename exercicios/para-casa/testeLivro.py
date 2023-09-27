from unittest import TestCase
from Livro import Livro

class TestLivro(TestCase):
    def test_init_deve_passar(self):
        # arrange
        nome = "pachinko"
        autor = "Min Jin Lee"
        # act
        livro = Livro(nome, autor)
        # assert
        self.assertEqual(nome, livro.nome)
        self.assertEqual(autor, livro.autor)
        self.assertEqual(False, livro.esta_emprestado)