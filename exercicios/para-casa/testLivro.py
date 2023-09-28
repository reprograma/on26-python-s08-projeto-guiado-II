from unittest import TestCase
from livro import Livro

class TestLivro(TestCase):
    def test_init_deve_passar(self):
        #arrange
        nome = "Coraline"
        autor = "Neil Gaiman"

        #act
        livro = Livro(nome, autor)

        #assert
        self.assertEqual(nome,livro.nome)
        self.assertEqual(autor,livro.autor)
        self.assertEqual(False,livro.esta_emprestado)