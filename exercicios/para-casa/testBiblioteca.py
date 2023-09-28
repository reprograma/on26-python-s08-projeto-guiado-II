from unittest import TestCase
from biblioteca import Biblioteca
from livro import Livro

class TestBiblioteca(TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()

    def test_init_deve_passar(self):

        #Assert
        self.assertIsInstance(self.biblioteca.livros, list)

    def test_adicionar_livro_deve_passar(self):
        #arrange
        nome_livro = "A Pequena Sereia e o Reino das Ilusões"
        nome_autor = "Louise O'Neil"
        livro = Livro(nome_livro, nome_autor)

        #act
        self.biblioteca.adicionar_livro(livro)

        #assert
        self.assertEqual(1, len(self.biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        livro = 1988

        # Act / Assert
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)

    def test_exibir_livro(self):
        self.biblioteca.livros = "Jogador nº 1"
        self.assertEqual(self.biblioteca.exibir_livro(), "Jogador nº 1")
    
    def test_emprestar_livro(self):
        nome_livro = "O Guia do Mochileiro das Galáxias"
        nome_autor = "Douglas Adams"
        livro = Livro(nome_livro, nome_autor)
        livro.esta_emprestado = True

        self.assertEqual(self.biblioteca.emprestar_livro(livro),f"O livro que você solicitou não está disponível")
