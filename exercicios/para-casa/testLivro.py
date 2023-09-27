from unittest import TestCase
from Livro import Livro

class TestLivro(TestCase):
    def test_init_deve_passar(self):
        #Arrange # configuração
        nome = 'A pedagogia da autonomia'
        autor = 'Paulo Freire'

        #Act
        livro = Livro(nome, autor) # temos uma variável livro do tipo Livro
        #Assert
        self.assertEqual(nome, livro.nome)
        self.assertEqual(autor, livro.autor)
        self.assertEqual(False, livro.esta_Emprestado)