
from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro

#atualizações na classe testBiblioteca de segunda

class testBiblioteca(TestCase):

    def setUp(self):
        self.biblioteca = Biblioteca()
    
    def test_init_deve_passar(self):
        
        #Arrange/Act
        #biblioteca = Biblioteca()
        
        #Assert
        self.assertIsInstance(self.biblioteca.livros, list)

    def test_adicionar_livros_deve_passar(self):
        
        #Arrange
        #biblioteca = Biblioteca()
        nome_livro = 'O mito da beleza'
        autor_livro = 'Naomi Wolf'
        livro = Livro(nome_livro, autor_livro)

        #Act
        self.biblioteca.adicionar_livro(livro)

        #Assert
        self.assertEqual(2, len(self.biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numero(self):

        #Arrange
        #biblioteca = Biblioteca()
        livro = 1988

        #Act
        #biblioteca.adicionar_livro(livro)
        
        #Assert
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)

    

        def test_exibir_livro_deve_passar(self):

        #Arrange
        #biblioteca = Biblioteca()
         nome_livro = 'O mito da beleza'
        autor_livro = 'Naomi Wolf'
        lista_livros = self.biblioteca.livros
        #livro = Livro(nome_livro, autor_livro)

        #Act
        self.biblioteca.exibir_livro()
        
        #Assert
        self.assertEqual(self.biblioteca.exibir_livro(), print(lista_livros))

        def test_emprestar_livro_naLista_deve_passar(self):
           
        #Arrange
         nome = 'python guia pratico do básico ao avançado'
         autor = 'Rafael FVC Santos'
         livro = Livro(nome, autor)
        self.biblioteca.livros = ['Psicologia Financeira', 'Dom Casmurro', 'O pequeno principe']
        lista_livros = self.biblioteca.livros

        #Act
        self.biblioteca.emprestar_livro(livro)

        #Assert
        self.assertTrue(livro.nome not in lista_livros)

    
        # Adiciona alguns livros à biblioteca
        livro1 = Livro("Livro 1", "Autor 1")
        livro2 = Livro("Livro 2", "Autor 2")
        Biblioteca.adicionar_livro(livro1)
        Biblioteca.adicionar_livro(livro2)

        # Verifica que os livros não estão emprestados inicialmente
        self.assertFalse(livro1.emprestado)
        self.assertFalse(livro2.emprestado)

        # Empresta um livro
        Biblioteca.emprestar_livro("Livro 1")

        # Verifica que apenas o livro emprestado foi atualizado
        self.assertTrue(livro1.emprestado)
        self.assertFalse(livro2.emprestado)