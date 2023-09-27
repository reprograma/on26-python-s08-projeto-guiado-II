# importando biblioteca e classe de testes
from unittest import TestCase

# importando o código fonte
from Livro import Livro

# declarando a classe de testes e informando a classe de teste do unittest como argumento
class TesteLivro(TestCase):

    def teste_init_deve_passar(self):
        # verifica se a classe Livro é inicilizada corretamente

        # arrange
        titulo_livro = "O Calor das Coisas" 
        autor_livro = "Nélida Piñon"
        ano_livro = 1998
        # criando as variáveis para executar os testes

        # act
        livro = Livro(titulo_livro, autor_livro, ano_livro)
        # criando a variável livro que chama a classe Livro
        # e que recebe as propriedades da classe Livro

        # assert
        self.assertEqual(titulo_livro, livro.tituloLivro)
        # testa se a variável nome é igual a propriedade nome da classe Livro
        self.assertEqual(autor_livro, livro.autorLivro)
        # testa se a variável autor é igual a propriedade autor da classe Livro
        self.assertEqual(ano_livro, livro.anoLivro)
        # testa se a variável ano é igual a propriedade ano da classe Livro
        self.assertEqual(False, livro.estaEmprestado)
        # testa se o livro adicionado está com o status padrão de "não emprestado"