# Importações necessárias para criar os testes
from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro

# Classe de teste para a classe Biblioteca
class TestBiblioteca(TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
    
    # Teste para verificar se a biblioteca é inicializada corretamente
    def test_init_deve_passar(self):
        # Assert: Verificar se a propriedade 'livros' é uma lista
        self.assertIsInstance(self.biblioteca.livros, list)
    
    # Teste para adicionar um livro à biblioteca
    def test_adicionar_livro_deve_passar(self):
        # Arrange: Criar um livro
        nome_livro = "O mito da Beleza"
        autor_livro = "Naomi Wolf"
        livro = Livro(nome_livro, autor_livro)
        
        # Act: Adicionar o livro à biblioteca
        self.biblioteca.adicionar_livro(livro)
        
        # Assert: Verificar se a biblioteca tem 1 livro após a adição
        self.assertEqual(1, len(self.biblioteca.livros))
        
    # Teste para garantir que não seja possível adicionar um número como livro
    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange: Criar um livro que é na verdade um número
        livro = 1988
        
        # Act / Assert: Verificar se a tentativa de adicionar o número como livro gera um erro de tipo
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)
    
    # Teste para verificar se o método exibir_livros retorna todos os livros adicionados
    def teste_exibir_livros_deve_passar(self):
        # Arrange: Adicionar dois livros à biblioteca
        livro1 = Livro("Livro 1", "Autor 1")
        livro2 = Livro("Livro 2", "Autor 2")
        self.biblioteca.adicionar_livro(livro1)
        self.biblioteca.adicionar_livro(livro2)
        
        # Act: Chamar o método exibir_livros
        livros = self.biblioteca.exibir_livros()
        
        # Assert: Verificar se o método retorna corretamente os livros adicionados
        self.assertEqual(2, len(livros))
        self.assertIn(livro1, livros)
        self.assertIn(livro2, livros)
    
    # Teste para verificar se é possível emprestar um livro
    def test_emprestar_livro_deve_passar(self):
        # Arrange: Adicionar um livro à biblioteca
        nome_livro = "O mito da Beleza"
        autor_livro = "Naomi Wolf"
        livro = Livro(nome_livro, autor_livro)
        self.biblioteca.adicionar_livro(livro)
        
        # Act: Chamar o método emprestar_livro
        emprestado = self.biblioteca.emprestar_livros(nome_livro)
        
        # Assert: Verificar se o livro foi emprestado corretamente
        self.assertTrue(emprestado)
        self.assertTrue(livro.esta_emprestado)
    
    # Teste para verificar se emprestar um livro inexistente retorna falso
    def test_emprestar_livro_inexistente_deve_retronar_falso(self):
        # Arrange: Definir um livro inexistente para emprestar
        nome_livro = "Livro Inexistente"
        
        # Act: Chamar o método emprestar_livro com um livro que não existe na biblioteca
        emprestado = self.biblioteca.emprestar_livros(nome_livro)
        
        # Assert: Verificar se o método retorna False quando o livro não existe
        self.assertFalse(emprestado)
