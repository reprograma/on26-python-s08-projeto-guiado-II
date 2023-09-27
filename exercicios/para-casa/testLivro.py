from unittest import TestCase
from Livro import Livro

class TestLivro(TestCase):
    def test_init_deve_passar(self):
        #Arrange
        nome = " Pequeno manual antracista"
        autor = " Djamila Ribeiro"
        # Act
        livro = Livro(nome, autor)
        
        #Assert
        self.assertEqual(nome, livro.nome)
        self.assertEqual(autor, livro.autor)
        self.assertEqual(False, livro.esta_emprestado)
        self.assertEqual(False, livro.esta_removido)
        self.assertEqual(False, livro.encontrado)
        self.assertEqual(False,livro.devolvido )

        