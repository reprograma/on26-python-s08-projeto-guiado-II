from unittest import TestCase
from livro import Livro

class TesteLivro(TestCase):
    def test_init_deve_passar(self):
        #arrange
        nome = "O Pequeno Principe"
        autor = "Antoine de Saint-Exupéry"

        #act
        livro = Livro(nome, autor)

        #assert
        self.assertEqual(nome, livro.nome)
        self.assertEqual(autor, livro.autor)