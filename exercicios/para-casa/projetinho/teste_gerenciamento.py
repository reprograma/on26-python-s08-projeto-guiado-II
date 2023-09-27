#Atividade realizada com a ajuda de Thaysa Lima

import unittest
from gerenciamento_biblioteca import Livro, Biblioteca

class TestBiblioteca(unittest.TestCase):
    
    def setUp(self):
        self.biblioteca = Biblioteca()
        self.livro1 = Livro("Interseccionalidade", "P.H. Collins & S. Bilge", "2021", "Editora Boitempo")
        self.livro2 = Livro("Vida e Palavras", "Veena Das", "2019", "Editora Boitempo")
    
    def test_adicionar_livro(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)
        self.assertEqual(self.biblioteca.exibir_lista(), [self.livro1, self.livro2])
    
    def test_listar_livros(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)
        self.assertEqual(self.biblioteca.exibir_lista(), [self.livro1, self.livro2])
    
    def test_emprestar_livro(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.emprestar_livro("Interseccionalidade")
        self.assertTrue(self.livro1.esta_emprestado)
        self.biblioteca.adicionar_livro(self.livro2)
        self.biblioteca.emprestar_livro("Vida e Palavras")
        self.assertTrue(self.livro2.esta_emprestado)
    
if __name__ == '_main_':
    unittest.main()
  