from unittest import TestCase
from Livro import Livro

class TestLivro(TestCase):
    def test_init_deve_passar(self):
        # Arrange  
        nome = "Mindset"
        autor = "Carol Dweck"
        # Act
        livro = Livro(nome, autor) 
        # Assert
        self.assertEqual(nome, livro.nome)
        self.assertEqual(autor, livro.autor)
        self.assertEqual(False, livro.esta_emprestado)
       

        