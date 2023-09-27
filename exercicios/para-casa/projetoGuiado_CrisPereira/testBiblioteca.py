# Testes Cris Pereira - semana 08
from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro

class TestBiblioteca(TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
        self.livro1 = Livro("Sister Outsider", "Audre Lorde")
        self.livro2 = Livro("Memórias da Plantação", "Grada Kilomba")

    def test_init_deve_passar(self):
        # Arrange / Act feitos no setup()
        # Assert
        self.assertIsInstance(self.biblioteca.livros, list)
    
    def test_adicionar_livro_deve_passar(self):
        # Arrange 
        nome_livro = "O mito da beleza"
        autor_livro = "Naomi Wolf"
        livro = Livro(nome_livro, autor_livro)

        # Act
        self.biblioteca.adicionar_livro(livro)

        # Assert
        self.assertEqual(1, len(self.biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        livro = 1988

        # Act / Assert
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)

# Novos testes abaixo
    def test_exibir_livros(self):
        #Arrange
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)
        lista_biblioteca = [self.livro1, self.livro2]

        #Act / Assert
        self.assertEqual(self.biblioteca.exibir_livros(), lista_biblioteca)

    def test_emprestar_livros(self):
         #Arrange
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)

         #Act
        self.biblioteca.emprestar_livro("Sister Outsider")
        self.biblioteca.emprestar_livro("Memórias da Plantação")

        #Assert
        self.assertTrue(self.livro1.esta_emprestado)     
        self.assertTrue(self.livro2.esta_emprestado) 

    def test_remover_livro(self):
        #Arrange
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)

        #Act
        self.biblioteca.remover_livro("Sister Outsider")

        #Assert
        self.assertIsNot(self.biblioteca.livros, self.livro1)


    def test_buscar_livro_existente(self):
        #Arrange
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)

        #Act
        livro_buscado = self.biblioteca.buscar_livro("Sister Outsider")

        #Assert
        self.assertEqual(livro_buscado, self.livro1)

    def test_buscar_livro_inexistente(self):
        #Arrange
        self.biblioteca.adicionar_livro(self.livro1)

        #Act
        livro_buscado = self.biblioteca.buscar_livro("Memórias da Plantação")

        #Assert
        self.assertEqual(livro_buscado, "Livro não encontrado.")

    def test_devolver_livro(self):
        #Arrange
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)
        self.biblioteca.emprestar_livro("Sister Outsider")
        self.biblioteca.emprestar_livro("Memórias da Plantação")

        #Act
        self.biblioteca.devolver_livro("Memórias da Plantação")

        #Assert
        self.assertFalse(self.livro2.esta_emprestado)

        




