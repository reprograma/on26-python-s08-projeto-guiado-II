from unittest import TestCase
from biblioteca import Biblioteca
from livro import Livro

class testBiblioteca(TestCase):

    def setUp(self):
        self.biblioteca = Biblioteca()
    
    def teste_init_deve_passar(self):
        
        #Arrange/Act
        #biblioteca = Biblioteca()
        
        #Assert
        self.assertIsInstance(self.biblioteca.livros, list)

    def teste_adicionar_livros_deve_passar(self):
        
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

    def teste_exibir_livros_deve_passar(self):

        #Arrange
        self.biblioteca.livros = ['Blabla']

        #Act
        self.biblioteca.exibir_livros()
        
        #Assert
        self.assertEqual(self.biblioteca.livros,['Blabla'])

    def test_emprestar_livro_existente_deve_passar(self):
        
        #Arrange
        nome = 'O mito da beleza'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)
        self.biblioteca.livros = [livro]

        #Act
        self.biblioteca.emprestar_livro(livro)

        #Assert
        self.assertTrue(livro.isBorrowed)

    def teste_emprestar_livro_inexistente_deve_passar(self):

        #Arrange
        nome = 'Pururuca'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)

        #Act/#Assert
        with self.assertRaises(NameError):
            self.biblioteca.emprestar_livro(livro)
        
    def teste_emprestar_livro_emprestado_deve_passar(self):

        #Arrange
        nome = 'O mito da beleza'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)
        livro.isBorrowed = True
        self.biblioteca.livros = [livro]

        #Act
        self.biblioteca.emprestar_livro(livro)

        #Assert
        self.assertTrue(livro.isBorrowed)

    def teste_remover_livro_na_lista_deve_passar(self):
        #Arrange
        nome = 'Pururuca'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)
        self.biblioteca.livros = [livro]
        
        #Act
        self.biblioteca.remover_livro(livro)

        self.assertFalse(livro in self.biblioteca.livros)

    def teste_remover_livro_inexistente_deve_passar(self):
        #Arrange
        nome = 'Pururuca'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)
        
        #Act/#Assert
        with self.assertRaises(ValueError):
            self.biblioteca.remover_livro(livro)

    def teste_remover_livro_emprestado_deve_passar(self):
        #Arrange
        nome = 'Pururuca'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)
        livro.isBorrowed = True
        self.biblioteca.livros = [livro]

        #Assert/#Act
        self.assertEqual(f'{livro.nome} está emprestado e portando não pode ser removido.', self.biblioteca.remover_livro(livro))

    def teste_devolver_livro_inexistenteNaLista_deve_passar(self):

        #Arrange
        nome = 'Pururuca'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)
        
        #Act/#Arrange
        with self.assertRaises(ValueError):
            self.biblioteca.devolver_livro(livro)

    def teste_devolver_livro_devolvido_deve_passar(self):
        #Arrange
        nome = 'Pururuca'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)
        self.biblioteca.livros = [livro]

        #Assert/#Act
        self.assertFalse(self.biblioteca.devolver_livro(livro))

    def teste_devolver_livro_disponível_deve_passar(self):
        
        #Assert
        nome = 'Pururuca'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)
        livro.isBorrowed = True
        self.biblioteca.livros = [livro]
        
        #Act
        self.biblioteca.devolver_livro(livro)

        #Assert
        self.assertFalse(self.biblioteca.devolver_livro(livro))

    def teste_buscar_livro_inexistente_na_lista_deve_passar(self):
        #Arrange
        nome = 'Pururuca'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)

        #Assert/#Act
        with self.assertRaises(ValueError):
            self.biblioteca.buscar_livro(livro)

    def teste_buscar_livro_emprestado_deve_passar(self):
        nome = 'Pururuca'
        autor = 'Igea Martins'
        livro = Livro(nome, autor)
        livro.isBorrowed = True
        self.biblioteca.livros = [livro]

        #Assert/#Act
        self.assertEqual(f'{livro.nome}, de {livro.autor}, está emprestado.', self.biblioteca.buscar_livro(livro))