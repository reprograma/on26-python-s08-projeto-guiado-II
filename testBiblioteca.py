from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro
class TestBiblioteca (TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
        
    def test_init_deve_passar(self):
        # Arrange/ Act
        # biblioteca = Biblioteca()
        
        # Assert
        self.assertIsInstance (self.biblioteca.livros, list)
    def test_adicionar_livro_deve_passar(self):
        #Arrange
        
        #biblioteca = Biblioteca()
        nome_livro = "Harry Potter"
        autor_livro = "J.K. Rowlling"
        livro = Livro(nome_livro, autor_livro)
        #Act
        self.biblioteca.adicionar_livro(livro)
        #Assert
        self.assertEqual(1, len(self.biblioteca.livros))
    def test_adicionar_livro_nao_deve_inserir_numero(self):
        #Arrange
        biblioteca = Biblioteca()
        livro = 1988
        #Act/Assert 
    
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)
    def test_listar_livro(self):
        #Arrange
        nome_livro = "Harry Potter"
        autor_livro = "J.K. Rowlling"
        livro = Livro(nome_livro,autor_livro)      
        #Act
        self.biblioteca.adicionar_livro(livro)
        self.biblioteca.listar_livro()
        #Assert 
        self.assertEqual (1, len(self.biblioteca.livros))
        
           
    def test_emprestar_livro(self):
        #Arrange
        nome_livro = "Harry Potter"
        autor_livro = "J.K Rowlling"  
        livro = Livro (nome_livro, autor_livro)
        #Act      
        self.biblioteca.adicionar_livro(livro)    
        esta_emprestado = self.biblioteca.emprestar_livro(nome_livro) 
        #Assert
        self.assertTrue(esta_emprestado)
    def test_remover_livro(self):
        #Arrange
        
        nome_livro = "Harry Potter"
        autor_livro = "J.K Rowlling"
        
        livro = Livro(nome_livro,autor_livro)
        #Act
        self.biblioteca.adicionar_livro(livro)
        self.biblioteca.remover_livro(livro)
        
        #Assert 
        self.assertEqual (0, len(self.biblioteca.livros))
        
    
        
        