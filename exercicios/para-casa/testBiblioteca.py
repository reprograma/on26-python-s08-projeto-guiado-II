from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro

class testBiblioteca(TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
    
    def test_init_deve_passar(self):
        # Arrange / Act
        #biblioteca = Biblioteca()
       
        # Assert
        self.assertIsInstance(self.biblioteca.livros, list)

    def test_adicionar_livro_deve_passar(self):    
        #Arrange
        # biblioteca = Biblioteca()
        nome_livro = "O vendedor de sonhos"
        autor_livro = "Augusto Cury"
        livro = Livro(nome_livro, autor_livro)
        
        #Act
        self.biblioteca.adicionar_livro(livro)
        #Assert
        self.assertEqual(1, len(self.biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numeros(self):
        #Arrange
        #biblioteca = Biblioteca()
        livro = 1988

        # Assert / Act
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro) 
    
    def test_exibir_livro_deve_mostrar(self):
        #Arrange
        nome_livro = "O vendedor de sonhos"
        autor_livro = "Augusto Cury"
        livro = Livro(nome_livro, autor_livro)
        self.biblioteca.adicionar_livro(livro)
        #Act
        lista_livros = self.biblioteca.exibir_livro()
        #Assert 
        self.assertEqual(1, len(lista_livros))

    def test_emprestar_livro_deve_emprestar(self):
        #Arrange
        nome_livro = "O vendedor de sonhos"
        autor_livro = "Augusto Cury"
        livro = Livro(nome_livro, autor_livro)
        self.biblioteca.emprestar_livro(livro)
        #Act
        self.biblioteca.emprestar_livro(nome_livro = 'O vendedor de sonhos')
        #Assert
        self.assertTrue(self.biblioteca.emprestar_livro)
        
               
