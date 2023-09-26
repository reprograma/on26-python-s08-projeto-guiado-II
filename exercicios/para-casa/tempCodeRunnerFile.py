import unittest
from Biblioteca import Biblioteca
from Livro import Livro

class TestBiblioteca(unittest.TestCase):
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
                                                 
# a seguir código acrescentado por mim

    def test_exibir_livros_deve_passar(self):
        # Arrange
        biblioteca = Biblioteca()
        livro1 = Livro("O choque de culturas", "Jean Donaldson")
        livro2 = Livro("A Linguagem dos cães", "Turid Rugass")
        biblioteca.adicionar_livro(livro1)
        biblioteca.adicionar_livro(livro2)

        # Act
        livros_exibidos = biblioteca.exibir_livros()

        # Assert
        self.assertEqual(2, len(livros_exibidos))
        self.assertIn(livro1, livros_exibidos)
        self.assertIn(livro2, livros_exibidos)

if __name__ == '__main__':
    unittest.main()
