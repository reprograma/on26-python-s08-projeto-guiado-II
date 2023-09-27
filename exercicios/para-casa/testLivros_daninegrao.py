from unittest import TestCase
from livros_daninegrao import Livros

class TestLivros(TestCase):
    def test_init_deve_passar(self):
        #Arrange 
        nome = "Meu pé de laranja lima"
        autor = "José Mauro de Vasconcelos"
        #Act
        livros = Livros(nome, autor)
        #Assert
        self.assertEqual(nome, livros.nome)
        self.assertEqual(autor, livros.autor)
        self.assertAlmostEqual(False, livros.esta_emprestado)