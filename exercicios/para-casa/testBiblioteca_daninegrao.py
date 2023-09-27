from unittest import TestCase
from Biblioteca_daninegrao import Biblioteca
from livros_daninegrao import Livros


class TestBiblioteca(TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
    
    
    def test_init_deve_passar(self):
        #Ararange / Act
        #biblioteca = Biblioteca()
        #Assert
        self.assertIsInstance(self.biblioteca.livros, list)
    
    def test_adicionar_livros_deve_passar(self):
        #Arrange
        #biblioteca = Biblioteca()
        nome_livro = "O demônio e a srtª Prym"
        autor_livro = "Paulo Coelho"
        livros = Livros(nome_livro, autor_livro)

        #Act
        self.biblioteca.adicionar_livros(livros)

        #Assert
        self.assertEqual(1, len(self.biblioteca.livros))
        
    def test_adicionar_livro_nao_deve_inserir_numero(self):
        #Arrange
        #biblioteca = Biblioteca()
        livros = 1998
        #Act/Assert
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livros(livros)


    def test_exibir_livro_deve_passar(self):
        # Arrange
        nome_livro = "Dom Casmurro"
        autor_livro = "Machado de Assis"
        livro = Livros(nome_livro, autor_livro)
        self.biblioteca.adicionar_livros(livro)

        # Act
        resultado = self.biblioteca.exibir_livro(nome_livro)

        # Assert
        self.assertEqual(1, len(resultado))
        self.assertEqual(livro, resultado[0])

    def test_emprestar_livro_deve_passar(self):
        # Arrange
        nome_livro = "A Moreninha"
        autor_livro = "Joaquim Manuel de Macedo"
        livro = Livros(nome_livro, autor_livro)
        self.biblioteca.adicionar_livros(livro)

        # Act/Assert
        self.biblioteca.emprestar_livro(nome_livro)

        
   

