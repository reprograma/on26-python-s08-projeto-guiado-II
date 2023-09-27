class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor 
from unittest import TestCase   
from Livro import Livro

class TestLivro(TestCase):
    def test_init_deve_passar(self):
        #Arrange 
        livro = Livro()
        nome = "tudo sobre o amor"
        autor = "Bell Hooks"

        #Act
        livro = Livro(nome, autor)

        #Assert 
        self.assertEqual(nome, livro.nome)
        self.assertEqual(autor, livro.autor)

  from unittest import TestCase
from Biblioteca import Biblioteca

class TestBiblioteca(TestCase):

    def test_unittest_deve_passar(self):
        #Arrange
        biblioteca = Biblioteca()
        #Act
        #Assert
        self.assertIsInstance(biblioteca.livros, list)
