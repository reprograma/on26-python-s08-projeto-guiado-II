from unittest import TestCase
from biblioteca import Biblioteca #do arquivo biblioteca está importando a classe Biblioteca
from livro import Livro

class TestBiblioteca(TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()

    def test_init_deve_passar(self):
        #Arrange / Act
        #biblioteca = Biblioteca()

        # Assert
        self.assertIsInstance(self.biblioteca.livros, list)
    

    def test_adicionar_livro_deve_passar(self):
        # Arrange
        #biblioteca = Biblioteca()
        nome_livro = "O mito da beleza"
        autor_livro = "Naomi Wolf"
        livro = Livro(nome_livro, autor_livro)

        # Act
        self.biblioteca.adicionar_livro(livro)

        # Assert
        self.assertEqual(1, len(self.biblioteca.livros))


    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        #biblioteca = Biblioteca()
        livro = 1988

        # Act / Assert
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)

