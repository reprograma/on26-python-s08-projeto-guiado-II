from unittest import TestCase

from Livro import Livro
from Biblioteca import Biblioteca

class TestBiblioteca(TestCase):
    def setUp(self):
         self.biblioteca = Biblioteca()

    def test_init_deve_passar(self):  # usa o DEF pq ele é um método
        # Arrange / Act 
        #biblioteca = Biblioteca()

        #  Assert
        self.assertIsInstance(self.biblioteca.livros, list)
    def test_adicionar_livro_deve_passar(self):
        # Arrange 
        #biblioteca = Biblioteca()
        nome_livro = "Bunker"
        autor_livro = "Kevin Brooks"
        livro = Livro(nome_livro, autor_livro)

        # Act
        self.biblioteca.adicionar_livro(livro)
        
        # Assert 
        self.assertEqual(1, len(self.biblioteca.livros))  

    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # Arrange
        #biblioteca = Biblioteca()
        livro = 1988

        # Act
        #self.biblioteca.adicionar_livro(livro) # essa função está sendo chamada na linha 38

        # Assert
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro) 

    def test_init_exibir_livros(self, livro_auto_ajuda, livro_como_ficar_milionario):
        self.biblioteca = exibir_livros  

      

    def test_init_emprestar_livro(self, livro: livros):
        nome_livro = "livro_auto_ajuda" , "livro_como_ficar_milionario"
        autor_livro = "João" , "Fernanda"
        livro_auto_ajuda = livro_auto_ajuda(nome_livro, autor_livro)
        livro_como_ficar_milionario = livro_como_ficar_milionario(nome_livro, autor_livro)
        return nome_livro - str(self.livro_auto_ajuda, livro_como_ficar_milionario)
    
        self.livro_como_ficar_milionario = livro_como_ficar_milionario
           

