import unittest
from Livro import Livro

class TestLivro(unittest.TestCase):
    def test_livro_inicializa_corretamente(self):
        livro = Livro("A linguagem dos cães", "Turid Rugaas")
        self.assertEqual(livro.titulo, "A linguagem dos cães")
        self.assertEqual(livro.autor, "Turid Rugaas")
        self.assertFalse(livro.esta_emprestado)

if __name__ == '__main__':
    unittest.main()
