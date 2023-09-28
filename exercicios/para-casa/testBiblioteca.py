from unittest import TestCase
from biblioteca import Biblioteca
from livro import Livro


class TestBiblioteca(TestCase):
    
    def setUp(self):
        self.biblioteca = Biblioteca() #com o self. na frente é comunicado que agora biblioteca é uma variável da classe
    
    
    def test_init_deve_passar(self):
        # Arrange / Act
        #biblioteca = Biblioteca()
        # Assert
        self.assertIsInstance(self.biblioteca.livro, list) #biblioteca.livros diz que a biclioteca contem os livros
        
        
    def test_add_livro_deve_passar(self):
        #Arrange
        #biblioteca = Biblioteca()
        livro = Livro(nome="Torto Arado", autor="Itamar Vieira", emprestado=False)
        #Act 
        self.biblioteca.add_livro(livro)
        #Assert
        self.assertEqual(1, len(self.biblioteca.livro))        
    
    def test_exibir_livro_deve_passar(self):
        #Arrange
        #biblioteca = Biblioteca()
        livro1 = Livro(nome="Torto Arado", autor="Itamar Vieira", emprestado=False)
        livro2 = Livro(nome="Entendendo algoritmo", autor="Aditya", emprestado=False)

        for livro in [livro1,livro2]:
         self.biblioteca.add_livro(livro)
        
        self.assertEqual(2, len(self.biblioteca.exibir_livros()))        
            
    
    def test_emprestar_livro_deve_passar(self):
        #Arrange
        #biblioteca = Biblioteca()
        livro_objeto = Livro(nome="Torto Arado", autor="Itamar Vieira", emprestado=False)
        self.assertEqual(True, self.biblioteca.emprestar_livro(livro_objeto).emprestado)   
     
    def test_add_livro_nao_deve_inserir_num(self):
        #Arrange
        #biblioteca = Biblioteca()
        livro = 1989
        #Assert / Act
        with self.assertRaises(TypeError):
            self.biblioteca.add_livro(livro)
            
                    
        