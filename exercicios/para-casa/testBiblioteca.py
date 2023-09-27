from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro

class TestBiblioteca(TestCase):

    def setUp(self):
        self.biblioteca = Biblioteca()

    def test_init_deve_passar(self):
        # Arrange / Act
        biblioteca = Biblioteca()
        
        # Assert
        self.assertIsInstance(biblioteca.livros, list)
    
    def test_adicionarlivro_deve_passar(self):
        # Arrange
        biblioteca = Biblioteca()
        nome_livro = 'O Mito da Beleza'
        autor_livro = 'Naomi Wolf'
        livro = Livro(nome_livro, autor_livro)

        # Act
        self.biblioteca.adicionar_livro(Livro)

        # Assert
        self.assertEqual(1, len(biblioteca.livros))

    def test_adicionar_livro_não_aceita_num(self):
        # Arrange
        biblioteca = Biblioteca()
        livro = 1988

        # Act / Assert
        with self.assertRaises(TypeError):
            biblioteca.adicionar_livro(livro)
        
        def test_exibir_livros_deve_passar(self):
        #Arrange
            biblioteca.livros = ['O Método Fair Play']
            lista = self.biblioteca.livros

        #Act
            self.biblioteca.exibir_livros()

        #Assert
            self.assertEqual(lista,['O Método Fair Play'])

    def test_emprestar_livro_naLista_deve_passar(self):

        #Arrange
        nome = 'O mito da beleza'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)
        self.biblioteca.livros = ['O mito da beleza', 'Eram os deuses astronautas', 'Tarântula']
        lista_livros = self.biblioteca.livros

        #Act
        self.biblioteca.emprestar_livro(livro)

        #Assert
        self.assertTrue(livro.nome in lista_livros)

    def test_emprestar_livro_inexistente_deve_passar(self):

        #Arrange
        nome = 'Pururuca'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)
        self.biblioteca.livros = ['O mito da beleza', 'Eram os deuses astronautas', 'Tarântula']
        lista_livros = self.biblioteca.livros

        #Act
        self.biblioteca.emprestar_livro(livro)

        #Assert
        self.assertTrue(livro.nome not in lista_livros)

    
