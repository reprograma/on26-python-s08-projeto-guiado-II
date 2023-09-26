import unittest
from gerenciamento_biblioteca import Livro, Biblioteca

class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        self.biblioteca = Biblioteca()
        self.livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "1943", "Editora Éditions Gallimard")
        
        self.livro2 = Livro("O Conto da Aia", "Margaret Atwood", "1985", "Editora Marco Zero")
        

    def test_adicionar_livro(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)
        self.assertEqual(self.biblioteca.exibir_lista(), [self.livro1, self.livro2])
    

    def test_listar_livros(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.adicionar_livro(self.livro2)
        self.assertEqual(self.biblioteca.exibir_lista(), [self.livro1, self.livro2])
    

    def test_emprestar_livro(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.emprestar_livro("O Pequeno Príncipe")
        self.assertTrue(self.livro1.esta_emprestado)

        self.biblioteca.adicionar_livro(self.livro2)
        self.biblioteca.emprestar_livro("O Conto da Aia")
        self.assertTrue(self.livro2.esta_emprestado)

    def test_remover_livro(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.remover_livro("O Pequeno Príncipe")
        self.assertEqual(self.biblioteca.exibir_lista(), [])

        self.biblioteca.adicionar_livro(self.livro2)
        self.biblioteca.remover_livro("O Conto da Aia")
        self.assertEqual(self.biblioteca.exibir_lista(), [])

    def test_buscar_livro_existente(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.assertEqual(
            self.biblioteca.buscar_livro("O Pequeno Príncipe"),
            "Livro: O Pequeno Príncipe, Autor: Antoine de Saint-Exupéry, Data de Lançamento: 1943, Editora: Editora Éditions Gallimard, Disponível: Sim"
        )

        self.biblioteca.adicionar_livro(self.livro2)
        self.assertEqual(
            self.biblioteca.buscar_livro("O Conto da Aia"), "Livro: O Conto da Aia, Autor: Margaret Atwood, Data de Lançamento: 1985, Editora: Editora Marco Zero, Disponível: Sim"
        )

    def test_buscar_livro_nao_encontrado(self):
        self.assertEqual(self.biblioteca.buscar_livro("Livro Inexistente"), "Livro não encontrado")

    def test_devolver_livro(self):
        self.biblioteca.adicionar_livro(self.livro1)
        self.biblioteca.emprestar_livro("O Pequeno Príncipe")
        self.biblioteca.devolver_livro("O Pequeno Príncipe")
        self.assertFalse(self.livro1.esta_emprestado)

if __name__ == '__main__':
    unittest.main()
