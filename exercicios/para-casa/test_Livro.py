from unittest import TestCase
from Livro import Livro

class test_Livro(TestCase):
    #arrange/act 
    def test__inti__sucess(self):
        titulo = "Mecânica Quântica"
        autor = "Richard Feyman"
        livros = Livro(titulo, autor)
        #assert
        self.assertEqual(titulo, livros.titulo)
        self.assertEqual(autor, livros.autor)
        self.assertEqual(False, livros.esta_emprestado)
        self.assertEqual(True, livros.devolvido)