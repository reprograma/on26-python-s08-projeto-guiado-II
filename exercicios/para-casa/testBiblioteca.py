from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro

class TestBiblioteca(TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()

    def test_init_deve_passar(self):
        # Arrange / Act     
        # Assert
        self.assertIsInstance(self.biblioteca.livros, list)

    def test_adicionar_livro_deve_passar(self):
        # Arrange
        nome_livro = "Anne de Green Gables"
        autor_livro = "L. M. Montgomery"
        livro = Livro(nome_livro, autor_livro)

        # Act
        self.biblioteca.adicionar_livro(livro)

        # Assert
        self.assertEqual(1, len(self.biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        livro = 1988
             
        # Assert / act
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)

# Teste associado ao método Exibir Livros

    def test_exibir_livros_deve_retornar_lista_de_livros(self):
        # Arrange
        nome_livro1 = "Anne de Green Gables"
        autor_livro1 = "L. M. Montgomery"
        livro1 = Livro(nome_livro1, autor_livro1)

        nome_livro2 = "Dom Quixote"
        autor_livro2 = "Miguel de Cervantes"
        livro2 = Livro(nome_livro2, autor_livro2)

        self.biblioteca.adicionar_livro(livro1)
        self.biblioteca.adicionar_livro(livro2)

        # Act
        lista_de_livros = self.biblioteca.exibir_livros()

        # Assert
        self.assertEqual(len(lista_de_livros), 2)
        self.assertIn(livro1, lista_de_livros)
        self.assertIn(livro2, lista_de_livros)

# Teste associado ao método Emprestar Livro

    def test_emprestar_livro_deve_marcar_livro_como_emprestado(self):
        # Arrange
        nome_livro = "Alice no País das Maravilhas"
        autor_livro = "Lewis Carrol"
        livro = Livro(nome_livro, autor_livro)
        self.biblioteca.adicionar_livro(livro)

        # Act
        emprestado = self.biblioteca.emprestar_livro(nome_livro)

        # Assert
        self.assertTrue(emprestado)  # Verifica se o livro foi emprestado com sucesso
        self.assertTrue(livro.emprestado)  # Verifica se o atributo emprestado do livro está como True 
    
# Teste associado ao método Remover Livro (Extra)

    def test_remover_livro_deve_remover_livro_nao_emprestado(self):
        # Arrange
        nome_livro = "Romeu e Julieta"
        autor_livro = "William Shakespeare"
        livro = Livro(nome_livro, autor_livro)
        self.biblioteca.adicionar_livro(livro)

        # Act
        removido = self.biblioteca.remover_livro(nome_livro)

        # Assert
        self.assertTrue(removido)  # Verifica se o livro foi removido com sucesso
        self.assertNotIn(livro, self.biblioteca.livros)  # Verifica se o livro não está mais na biblioteca

 # Teste associado ao método Buscar Livro (Extra)   

    def test_buscar_livro_deve_retornar_informacoes_do_livro(self):
        # Arrange
        nome_livro = "Morro dos Ventos Uivantes"
        autor_livro = "Emilly Bronte"
        livro = Livro(nome_livro, autor_livro)
        self.biblioteca.adicionar_livro(livro)

        # Act
        informacoes = self.biblioteca.buscar_livro(nome_livro)

        # Assert
        self.assertEqual(informacoes, f"Nome: {nome_livro}, Autor: {autor_livro}, Status: Disponível")

# Teste associado ao método Devolver Livro (Extra)   

    def test_devolver_livro_deve_marcar_livro_como_nao_emprestado(self):
        # Arrange
        nome_livro = "Emma"
        autor_livro = "Jane Austen"
        livro = Livro(nome_livro, autor_livro)
        self.biblioteca.adicionar_livro(livro)
        self.biblioteca.emprestar_livro(nome_livro)

        # Act
        devolvido = self.biblioteca.devolver_livro(nome_livro)

        # Assert
        self.assertIsNone(devolvido)  # Verifica se o livro foi devolvido com sucesso
        self.assertFalse(livro.emprestado)  # Verifica se o atributo emprestado do livro está como False