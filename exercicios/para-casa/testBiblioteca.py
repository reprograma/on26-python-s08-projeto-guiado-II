from unittest import TestCase #Identificador de uma classe de testes
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

    def test_emprestar_livro_deve_passar(self):
        #Arrange
        biblioteca = Biblioteca()
        livro = Livro("O mito da beleza", "Naomi Wolf")
        #Act
        biblioteca.adicionar_livro(livro)
        #Assert
        self.assertTrue(biblioteca.emprestar_livro("O mito da beleza"))
        self.assertTrue(livro.esta_emprestado)

    def test_emprestar_livro_inexistente_deve_retornar_false(self):
        #Arrange
        biblioteca = Biblioteca()
        #Act/Assert
        self.assertFalse(biblioteca.emprestar_livro("Livro Inexistente"))

    def teste_exibir_livros(self):
        #Arrange
        biblioteca = Biblioteca()
        livro1 = Livro("Uzumaki", "Junji Ito")
        livro2 = Livro("Tomie", "Junji Ito")
        #Act
        biblioteca.adicionar_livro(livro1)
        biblioteca.adicionar_livro(livro2)
        livros = biblioteca.exibir_livros()
        #Assert
        self.assertIn(livro1, livros)
        self.assertIn(livro2, livros)