from unittest import TestCase
from livro import Livro


class TestLivro(TestCase):
    def test_init_deve_passar(self):
        #Arrange
        nome = "Torto Arado"
        autor ="Itamar Vieira"
        #Act
        livro = Livro(nome, autor,False)
        #Assert
        self.assertEqual(nome, livro.nome)
        self.assertEqual(autor, livro.autor)
        self.assertEqual(False, livro.emprestado)
        
        
        