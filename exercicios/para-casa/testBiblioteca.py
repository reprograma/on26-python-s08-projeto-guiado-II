from unittest import TestCase 
from BibliotecaP import Biblioteca 
from Livro import Livro
class testBiblioteca(TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
    def test_init_sucess(self):  #o python espera que o def comece com "test"
        #arrange/act- chamar o cod fonte
        biblioteca = Biblioteca()
        #assert
        self.assertIsInstance(self.biblioteca.livros, list)
    
    def test_adicionar_livro_sucess(self):
        # Arrange 
        #biblioteca = Biblioteca()
        titulo = "mecânica quântica"
        autor = "Feyman"
        livro = Livro(titulo, autor)

        # Act
        self.biblioteca.adicionar_livro(livro)

        #assert
        self.assertEqual(1,len(self.biblioteca.livros))
    
    def test_add_livro_nao_numero_sucess(self):
        #arrange
        livro = 1997
        #assert/act
        with self.assertRaises(TypeError):
            self.biblioteca.adicionar_livro(livro)

    def test_listar_vazia(self):
       #arrange
       #lista = Biblioteca() foi retirado pois usamos o comando setUp no inicio
       lista = Biblioteca()
       #act
       acervo_listados = lista.listar_livros()
       self.assertEqual (0, len(acervo_listados)) == 0        

    def test_listar_livros(self):
        #arrange/
        lista = Biblioteca()
        lista.adicionar_livro(Livro("mecânica quântica", "Feyman"))
        #act/assert
        acervo_listado = lista.listar_livros()
        self.assertEqual (1, len(acervo_listado))
        self.assertEqual (acervo_listado[0].titulo, "mecânica quântica")
        self.assertEqual (acervo_listado[0].autor, "Feyman")

    def testar_emprestimo(self):
        #arrange/act
        situacao = Biblioteca()
        situacao.adicionar_livro(Livro("mecânica quântica", "Feyman"))
        livro_emprestado = situacao.emprestar_livros("mecânica quântica")
        #assert
        self.assertEqual(livro_emprestado.titulo, "mecânica quântica")
        self.assertEqual(livro_emprestado.esta_emprestado, True)

    def testar_emprestimo_dois_livros(self):
        #arrange/act
        situacao = Biblioteca()
        situacao.adicionar_livro(Livro("mecânica quântica", "Feyman"))
        situacao.adicionar_livro(Livro("Uma breve história do tempo", "Stephen Hawking"))
        livro_emprestado1 = situacao.emprestar_livros("mecânica quântica")
        livro_emprestado2 = situacao.emprestar_livros("Uma breve história do tempo")
        #assert
        self.assertEqual(livro_emprestado1.titulo, "mecânica quântica")
        self.assertEqual(livro_emprestado1.esta_emprestado, True)
        self.assertEqual(livro_emprestado2.titulo, "Uma breve história do tempo")
        self.assertEqual(livro_emprestado2.esta_emprestado, True)

    def testar_devolucao(self):
        #arrange/act
        situacao = Biblioteca()
        situacao.adicionar_livro(Livro("mecânica quântica", "Feyman"))
        livro_devolvido = situacao.devolver_livro("mecânica quântica")
        #assert
        self.assertEqual(livro_devolvido.titulo, "mecânica quântica")
        self.assertEqual(livro_devolvido.devolvido, True)