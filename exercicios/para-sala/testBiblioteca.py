from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro

class TestBiblioteca(TestCase):
    def test_init_deve_passar(self):
        # Arrange / Act
        biblioteca = Biblioteca()

        # Assert
        self.assertIsInstance(biblioteca.livros, list)
    
    def test_adicionar_livro_deve_passar(self):
        # Arrange 
        biblioteca = Biblioteca()
        nome_livro = "O mito da beleza"
        autor_livro = "Naomi Wolf"
        livro = Livro(nome_livro, autor_livro)

        # Act
        biblioteca.adicionar_livro(livro)

        # Assert
        self.assertEqual(1, len(biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        biblioteca = Biblioteca()
        livro = 1988

        # Act / Assert
        with self.assertRaises(TypeError):
            biblioteca.adicionar_livro(livro)