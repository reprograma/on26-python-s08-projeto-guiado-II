from unittest import TestCase
from Biblioteca import Biblioteca
from livro import Livro

class TestBiblioteca(TestCase):
    def test_init_deve_passar(self):
        # Arrange / Act
        biblioteca = Biblioteca()

        # Assert
        self.assertIsInstance(biblioteca.livros, list)
    
class TestBiblioteca(TestCase):
    def test_init_deve_passar(self):
        # Arrange / Act
        biblioteca = Biblioteca()

        # Assert
        self.assertIsInstance(biblioteca.livros, list)
    
    def test_adicionar_livro_deve_passar(self):
        # Arrange 
        biblioteca = Biblioteca()
        nome_livro = "Dom Casmurro"
        autor_livro = "Machado de Assis"
        livro = Livro(nome_livro, autor_livro)

        # Act
        biblioteca.adicionar_livro(livro)

        # Assert
        self.assertEqual(1, len(biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numero(self):
        #Arrange
        biblioteca = Biblioteca
        livro = 1988
        #act/assert
        with self.assertRaises(TypeError):
            biblioteca.adicionar_livro(livro)
    
    def test_remover_livro_deve_passar(self):
        #Arrange
        biblioteca = Biblioteca()
        nome_livro = "Dom Casmurro"
        autor_livro = "Machado de Assis"
        livro = Livro(nome_livro, autor_livro)
        biblioteca.adicionar_livro(livro)

        # Act
        biblioteca.remover_livro(nome_livro)

        # Assert
        self.assertEqual(0, len(biblioteca.livros))
    
    
    def test_pesquisar_livro_deve_passar(self):
        #Arrange
        biblioteca = Biblioteca()
        nome_livro = "Dom Casmurro"
        autor_livro = "Machado de Assis"
        livro = Livro(nome_livro, autor_livro)
        biblioteca.adicionar_livro(livro)
        
        #Act
        livro_pesquisa = "Dom Casmurro"
        livro_encontrado = biblioteca.pesquisar_livro(livro_pesquisa)

        # Act/#Assert
        self.assertEqual("Dom Casmurro", livro_encontrado.nome)