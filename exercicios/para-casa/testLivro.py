from unittest import TestCase
from Livro import Livro

class TestLivro(TestCase):    
    def test_init_deve_passar(self):  #testar o método construtor
        # arrenge
        nome = "Calibã e a bruxa"
        autor = "Silvia Federici"
        # act
        livro = Livro(nome, autor)
        # assert
        self.assertEqual(nome, livro.nome)
        self.assertEqual(autor, livro.autor)
        self.assertEqual(False, livro.esta_emprestado) 
    
    


