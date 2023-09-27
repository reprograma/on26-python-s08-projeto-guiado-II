from unittest import TestCase #Desta forma, importamos apenas o TestCase dentro de tudo que tem no unittest
from Biblioteca import Biblioteca
from Livro import Livro

class TestBiblioteca(TestCase): #Especificamos que essa classe irá conter testes
    def setUp(self):
        self.biblioteca = Biblioteca()
        # self.livro = Livro()
    
    def test_init_deve_passar(self): #Precisamos começar os casos de teste sempre com o prefixo test
        #Arrange -> queremos chamar a nossa Biblioteca / Act
        # biblioteca = Biblioteca()
        #Assert
        self.assertIsInstance(self.biblioteca.livros, list)

    def test_adicionar_livro_deve_passar(self):
        #Arrange
        # biblioteca = Biblioteca()
        nome_livro = 'A coragem de ser imperfeito'
        autor_livro = 'Brené Brown'
        livro = Livro(nome = nome_livro, autor = autor_livro)
        self.biblioteca.adicionar_livro(livro)
        # neste momento foi preciso importar a classe Livro
        # adicionei os parâmetros que ele espera
        #Act
        # biblioteca.adicionar_livro(livro)
        # chamamos a biblioteca.adicionar_livro e esperamos receber um livro
        # após criar as variáveis nome_livro, autor_livro e livro, inserimos estas variáveis no nosso método adicionar_livro
        #Assert
        self.assertEqual(1, len(self.biblioteca.livros)) # esperamos que o tamanho da nossa lista de livros seja 1 pois adicionamos 1 livro até aqui
        # ao rodar o teste com esse método pela primeira vez, caímos no erro NotImplementedError

    def test_adicionar_livro_nao_deve_inserir_numero(self):
        #Arrange
        # biblioteca = Biblioteca()
        livro = 1988
        #Act 
        # inicialmente o teste passou mesmo o valor atríbuido à variável livro sendo um número
        #Assert
        # self.assertRaises()
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)

    def test_exibir_livro_deve_passar(self):
        #Arrange
        livro_nome = 'A pedagogia do oprimido'
        livro_autor = 'Paulo Freire'
        livro = Livro(livro_nome, livro_autor)
        self.biblioteca.adicionar_livro(livro)
        #Act
        self.biblioteca.exibir_livro(livro)
        #Assert
        self.assertEqual(livro_nome, 'A pedagogia do oprimido')
        self.assertEqual(livro_autor, 'Paulo Freire')
        
    def test_livro_esta_emprestado(self):
        self.biblioteca.emprestar_livro()
        #Arrange
        # self.livro = Livro(nome='Dom Casmurro', autor='Machado de Assis', emprestado=True)
        self.nome = 'Dom Casmurro'
        self.autor = 'Machado de Assis'
        self.esta_Emprestado = True
        #Act
        # quero saber se o livro está emprestado
        #Assert
        self.assertTrue(self.esta_Emprestado)