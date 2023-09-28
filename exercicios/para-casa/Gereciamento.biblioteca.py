#Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []
    def adicionar_livro(self, livro: Livro):
        if (isinstance (livro) != Livro):
            raise TypeError(f"Esperado livro obtido valor {livro} do tipo{type(livro)}")
        self.livros.append = (livro)

#TestBiblioteca
from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro
class TestBiblioteca(TestCase):

    def test_unittest_deve_passar(self):
        #Arrange
        biblioteca = Biblioteca()
        #Act
        #Assert
        self.assertIsInstance(biblioteca.livros, list)


    def test_adicionar_livro_deve_passar(self):
        #Arrange
        biblioteca = Biblioteca()
        livro = Livro()
        nome_livro = "Diario de Anne Frank"
        autor_livro = "Anne Frank"
        livro = Livro(nome_livro, autor_livro)

        #Act
        biblioteca.adicionar_livro(livro)

        #Assert
        self.assertEwual(1, len(biblioteca.livros))

    def test_adicionar_livro_nao_deve_inserir_numero(self):
        #Arrange
        biblioteca = Biblioteca()
        livro = 1998

        
        # Act/ Assert
        #assertRaises - queremos que nosso código não funcione.
        with self.assertRaises(TypeError):
              biblioteca.adicionar_livro(livro)


#Livro
class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor 
        self.esta_Emprestado = False
    
#Teste Livro
from unittest import TestCase   
from Livro import Livro

class TestLivro(TestCase):
    def test_init_deve_passar(self):
        #Arrange 
        nome = "tudo sobre o amor"
        autor = "Bell Hooks"

        #Act
        livro = Livro(nome, autor)

        #Assert 
        self.assertEqual(nome, livro.nome)
        self.assertEqual(autor, livro.autor)
        self.assertEqual(False, livro.esta_Emprestado)

#Emprestar Livros
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def exibir_livros(self):
        for livro in self.livros:
            print(f"Título: {livro['tudo sobre o amor']}, Autor: {livro['Bell Hooks']}, Disponivel: {livro['esta_emprestado']}")

    def emprestar_livro(self, nome_do_livro):
        for livro in self.livros:
            if livro['titulo'] == nome_do_livro:
                livro['esta_emprestado'] = True

#Teste Emprestar 
def test_emprestar_livro():
    biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.emprestar_livro('Livro 1')


test_emprestar_livro()

#Exibir Livros
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def exibir_livros(self):
        for livro in self.livros:
            print(f"Tudo sobre o amor: {livro['tudo sobre o amor']}, Autor: {livro['Bell Hooks']}")


#Teste exibir 

def test_exibir_livros():
    biblioteca = Biblioteca()

    livro1 = {'titulo': 'tudo sobre o amor 1', 'autor': 'Bell Hooks 1'}
    livro2 = {'titulo': 'Diario de Anne Frank 2', 'autor': 'Anne Frank 2'}

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    biblioteca.exibir_livros()


#act
test_exibir_livros()
    
