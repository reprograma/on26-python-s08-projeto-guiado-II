from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro

class TestBiblioteca(TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()

    def test_exibir_livros_deve_retornar_lista_vazia_inicialmente(self):
        # Assert
        self.assertEqual([], self.biblioteca.exibir_livros())

    def test_exibir_livros_deve_retornar_lista_com_livros_adicionados(self):
        # Arrange
        livro = Livro("O mito da beleza", "Naomi Wolf")
        self.biblioteca.adicionar_livro(livro)

        # Act / Assert
        self.assertEqual([livro], self.biblioteca.exibir_livros())

    def test_emprestar_livro_deve_marcar_como_emprestado_se_encontrado(self):
        # Arrange
        livro = Livro("O mito da beleza", "Naomi Wolf")
        self.biblioteca.adicionar_livro(livro)

        # Act
        resultado = self.biblioteca.emprestar_livro("O mito da beleza")

        # Assert
        self.assertTrue(resultado)
        self.assertTrue(livro.esta_emprestado)

    def test_emprestar_livro_deve_retornar_False_se_livro_nao_encontrado(self):
        # Act
        resultado = self.biblioteca.emprestar_livro("Livro Inexistente")

        # Assert
        self.assertFalse(resultado)