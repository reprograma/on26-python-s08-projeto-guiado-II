from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro

class TestBiblioteca(TestCase):

    def setUp(self): # Esse método é chamado antes de cada um dos testes dessa classe
        self.biblioteca = Biblioteca()

    def test_init_deve_passar(self):
        # Arrange / Act feitos no setup()
        # Assert
        self.assertIsInstance(self.biblioteca.livros, list)

    def test_adicionar_livro_deve_passar(self):
        # Arrange
        nome_livro = "Grande Sertão: Veredas"
        autor_livro = "Guimarães Rosa"
        livro = Livro(nome_livro, autor_livro)

        # Act
        self.biblioteca.adicionar_livro(livro)
        
        # Assert
        self.assertEqual(1, len(self.biblioteca.livros))
        
    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        livro = 1984

        # Act / Assert
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)
    
    def test_exibir_livro_deve_passar(self):
        # Arrange
        nome_livro1 = "Cem anos de solidão"
        autor_livro1 = "Gabriel García Márquez"
        livro1 = Livro(nome_livro1, autor_livro1)

        nome_livro2 = "A casa dos espíritos"
        autor_livro2 = "Isabel Allende"
        livro2 = Livro(nome_livro2, autor_livro2)

        # # Act
        self.biblioteca.adicionar_livro(livro1)
        self.biblioteca.adicionar_livro(livro2)
        livros_exibidos = self.biblioteca.exibir_livros()
        
        # # Assert
        retorno_esperado = [livro1, livro2]
        self.assertEqual(retorno_esperado, livros_exibidos)

    def test_emprestar_livro_deve_passar(self):

        # Arrange
        nome_livro = "Ficções"
        autor_livro = "Jorge Luis Borges"
        livro = Livro(nome_livro, autor_livro)
        self.biblioteca.adicionar_livro(livro)

        # # Act
        self.biblioteca.emprestar_livro(livro)
        
        # # Assert
        self.assertTrue(self.biblioteca.livros[0].esta_emprestado)

    def test_remover_livro_deve_passar(self):

        # Arrange
        nome_livro = "O paraíso são os outros"
        autor_livro = "Valter Hugo Mãe"
        livro = Livro(nome_livro, autor_livro)
        self.biblioteca.adicionar_livro(livro)

        # Act
        self.biblioteca.remover_livro(livro)
        
        # Assert
        self.assertFalse(livro in self.biblioteca.livros)
            
    def test_buscar_livro_deve_passar(self):

        # Arrange
        nome_livro = "Olhos d'água"
        autor_livro = "Conceição Evaristo"
        livro = Livro(nome_livro, autor_livro)
        self.biblioteca.adicionar_livro(livro)

        # Act
        self.biblioteca.buscar_livro(livro)
        livro_buscado = self.biblioteca.buscar_livro(livro)
        
        # Assert
        retorno_esperado = {
            "Nome do livro": nome_livro, 
            "Nome do autor": autor_livro,
            "O livro está disponível?": False}
        
        self.assertEqual(livro_buscado, retorno_esperado)

    def test_devolver_livro_deve_passar(self):

        # Arrange
        nome_livro = "Torto Arado"
        autor_livro = "Itamar Vieira Junior"
        livro = Livro(nome_livro, autor_livro)
        self.biblioteca.adicionar_livro(livro)
        self.biblioteca.emprestar_livro(livro)

        # # Act
        self.biblioteca.devolver_livro(livro)
        
        # # Assert
        self.assertFalse(self.biblioteca.livros[0].esta_emprestado)
