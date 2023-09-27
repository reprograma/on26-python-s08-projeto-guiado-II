from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro

class TestBiblioteca(TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()

    def test_init_deve_passar(self):
        # arrange e act
        #biblioteca = Biblioteca()
        # assert
        self.assertIsInstance(self.biblioteca.livros, list)
    
    def test_adicionar_livro_deve_passar(self):
        # arrange
        #biblioteca = Biblioteca()
        nome_livro = "Tudo sobre o amor"
        autor_livro = "bell hooks"
        livro = Livro(nome = nome_livro, autor = autor_livro)
        # act
        self.biblioteca.adicionar_livro(livro)
        # assert
        self.assertEqual(1, len(self.biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numero(self):
        # arrange
        #biblioteca = Biblioteca()
        livro = 1988
        # act e assert
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(Livro)

    def test_exibir_livros_deve_passar(self):
        livro = Livro("Tudo sobre o amor", "bell hooks")
        self.biblioteca.adicionar_livro(livro)
        self.assertEqual([livro], self.biblioteca.exibir_livros())
        
    def test_emprestar_livro(self):
        #nome_livro = "Tudo sobre o amor"
        #autor_livro = "bell hooks"
        livro = Livro("Tudo sobre o amor", "bell hooks")
        self.biblioteca.emprestar_livros(livro)
        self.assertTrue = ()