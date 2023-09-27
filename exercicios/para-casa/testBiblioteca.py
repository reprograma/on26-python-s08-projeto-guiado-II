from unittest import TestCase
from biblioteca import Biblioteca
from livro import Livro

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
        self.assertEqual(1, len(self.biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numero(self):

        #Arrange
        #biblioteca = Biblioteca()
        livro = 1988

        #Act
        #biblioteca.adicionar_livro(livro)
        #n precisa chamar essa função pq eu já defini um valor hipotético pro livro

        #Assert
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)

    def test_exibir_livros_deve_passar(self):

        #Arrange
        self.biblioteca.livros = ['Blabla']
        lista = self.biblioteca.livros

        #Act
        self.biblioteca.exibir_livros()
        
        #Assert
        self.assertEqual(lista,['Blabla'])

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

    #def test_emprestar_livro_nDisponivel_deve_passar(self):

        #Arrange

        #Act

        #Assert