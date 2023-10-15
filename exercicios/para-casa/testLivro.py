from unittest import TestCase   # pra essa situação vamos usar o unittest que é uma biblioteca com ferramentas de teste, por ex: testCase
from Livro import Livro         # precisa importar do modulo "arquivo" livro, importamos a classe livros

class testlivro(TestCase): # criando a classe de teste livro usando da ferramenta testCase
    def test_init_deve_passar(self): # a gente utilizou novamente o método construtor que leva como parâmentro SELF
        # Arrange é usado para definir as configuraçõe do que se precisa
        nome = "Anjos e Demonios" # variável nome e autor
        autor = "Dan Browm"

        # Act é ação 
        livro = Livro(nome, autor) # dentro do act cria uma varíavel ou um objeto que realiza a ação de acessar os parâmetros da classe

        # Assert é o teste 
        self.assertEqual(nome, livro.nome) # o assertEqual ele define que tem que ser igual
        self.assertEqual(autor, livro.autor) 
        self.assertEqual(False, livro.esta_emprestado) # por ser uma palavra reservada chamamos direto da classe livros e não associamos ao objeto criado no ACT
