import unittest
from Biblioteca import Biblioteca
from Livro import Livro

class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        # Configuração comum para todos os testes
        self.biblioteca = Biblioteca()
        self.livro1 = Livro("A linguagem dos cães", "Turid Rugaas")
        self.livro2 = Livro("O choque de culturas", "Jean Donaldson")

    def test_adicionar_livro(self):
        """
        Verifica se é possível adicionar livros à biblioteca.
        """
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)

        self.assertEqual(len(self.biblioteca.livros), 2)

    def test_exibir_livros(self):
        """
        Verifica se a função exibir_livros retorna a lista de títulos corretamente.
        """
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)

        livros_exibidos = self.biblioteca.exibir_livros()

        self.assertIn("A linguagem dos cães", livros_exibidos)
        self.assertIn("O choque de culturas", livros_exibidos)

    def test_emprestar_livro(self):
        """
        Verifica se a função emprestar_livro marca corretamente um livro como emprestado.
        """
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)

        self.biblioteca.emprestar_livro("A linguagem dos cães")
        self.assertTrue(self.livro1.esta_emprestado)
        self.assertFalse(self.livro2.esta_emprestado)

if __name__ == '__main__':
    unittest.main()
