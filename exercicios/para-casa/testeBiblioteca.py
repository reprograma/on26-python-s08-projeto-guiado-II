# importando biblioteca e classe de testes
from unittest import TestCase

# importando o código fonte
from Biblioteca import Biblioteca
from Livro import Livro

class TesteBiblioteca(TestCase):
    # declarando a classe de testes e informando a classe de teste do unittest como argumento

    def teste_init_deve_passar(self):     # definindo o primeiro teste (como nomear: teste_nomedoteste_oquedevefazer)
        # verifica se a classe Biblioteca é inicilizada corretamente

        # arrange / act
        biblioteca = Biblioteca()
        # criando a variável biblioteca que chama a classe Biblioteca
        
        # assert
        self.assertIsInstance(biblioteca.acervo, list)
        # testa se a propriedade acervo da classe Biblioteca tem o formato de lista

    def teste_adicionar_livro_deve_passar(self):
        # verifica se um livro é adiconado à Biblioteca
        
        #arrange
        biblioteca = Biblioteca()
        # criando a variável biblioteca que chama a classe Biblioteca
        
        titulo_livro = "Capitu"
        autor_livro = "Machado de Assis"
        ano_livro = 1998
        # criando as variáveis para executar os testes

        livro = Livro(titulo_livro, autor_livro, ano_livro)
        # criando a variável que chama a classe Livro
        
        #act
        biblioteca.adicionar_livro(livro)
        # executando ação de adicionar livro ao acervo da Biblioteca

        #assert
        self.assertEqual(1, len(biblioteca.acervo))
        # testa se o livro foi adicionado ao acervo da Biblioteca
        # espera-se que o tamanho da lista seja 1 porque um livro foi adicionado à lista vazia

    def teste_adicionar_livro_nao_deve_inserir_numero(self):
        # verifica se a propriedade livro não recebe valores numéricos

        # arrange
        biblioteca = Biblioteca()
        # criando a variável biblioteca que chama a classe Biblioteca
        
        livro = 1988
        # criando a variável para executar o teste

        # act / assert
        with self.assertRaises(TypeError):
         biblioteca.adicionar_livro(livro)
        # testa se o livro adicionado tem valores inválidos

    def teste_exibir_acervo_deve_passar(self):
        # verifica se o acervo de livros é exibido

        #arrange
        biblioteca = Biblioteca()
        # criando a variável biblioteca que chama a classe Biblioteca

        titulo_livro = "Capitu"
        autor_livro = "Machado de Assis"
        ano_livro = "1998"
        # criando as variáveis para executar os testes

        livro = Livro(titulo_livro, autor_livro, ano_livro)
        # criando a variável que chama a classe Livro

        biblioteca.adicionar_livro(livro)
        # adicionado o livro ao acervo da Biblioteca

        acervo_livros = [livro]
        # criando a variável acervo_livros que recebe os livros adicionados

        # act
        biblioteca.exibir_acervo(acervo_livros)
        # executando a ação de exibir o acervo

        # assert
        self.assertEqual(1, len(acervo_livros))
        #testa se o livro foi adicionado à variável acervo_livro
        self.assertEqual(acervo_livros, biblioteca.acervo)
        # testa se todos os livros adicionados fazem arte do acervo da Biblioteca

    def teste_remover_livro_deve_passar(self):
        # verifica se um livro é removido do acervo

         # arrange
         biblioteca = Biblioteca()
         # criando a variável biblioteca que chama a classe Biblioteca
        
         titulo_livro = "Capitu"
         autor_livro = "Machado de Assis"
         ano_livro = "1998"
         esta_emprestado = False
         # criando as variáveis para executar os testes

         livro = Livro(titulo_livro, autor_livro, ano_livro)
         # criando a variável que chama a classe Livro

         biblioteca.adicionar_livro(livro)
         # adicionado o livro ao acervo da Biblioteca
        
         # act
         biblioteca.remover_livro(livro)
         # executando ação de remover um livro da biblioteca

         # assert
         self.assertIn(livro, biblioteca.acervo)
         # testa se o livro faz paste do acervo da Biblioteca
         self.assertFalse(esta_emprestado, biblioteca.acervo)
         #testa se o livro não está emprestado e pode ser removido
    
    def teste_remover_livro_emprestado_nao_deve_passar(self):
        # verifica se um livro emprestado não é removido

        # arrange
         biblioteca = Biblioteca()
         # criando a variável biblioteca que chama a classe Biblioteca
        
         titulo_livro = "Capitu"
         autor_livro = "Machado de Assis"
         ano_livro = "1998"
         esta_emprestado = True
         # criando as variáveis para executar os testes

         livro = Livro(titulo_livro, autor_livro, ano_livro)
         # criando a variável que chama a classe Livro

         biblioteca.adicionar_livro(livro)
         # adicionado o livro ao acervo da Biblioteca
        
         # act
         biblioteca.remover_livro(livro)
         # executando a ação de remover livro

         # assert
         self.assertIn(livro, biblioteca.acervo)
         # testa se o livro pertence ao acervo da biblioteca
         self.assertTrue(esta_emprestado, biblioteca.acervo)
         # testa se o livro está emprestado e não pode ser removido
         
    def teste_pesquisar_livro_deve_passar(self):
         # verifica se ao pesquisar o método retorna o livro pesquisado

        # arrange
        biblioteca = Biblioteca()
        # criando a variável biblioteca que chama a classe Biblioteca
        
        titulo_livro = "Capitu"
        autor_livro = "Machado de Assis"
        ano_livro = "1998"
        # criando as variáveis para executar os testes

        livro = Livro(titulo_livro, autor_livro, ano_livro)
        # criando a variável que chama a classe Livro

        biblioteca.adicionar_livro(livro)
        # adicionado o livro ao acervo da Biblioteca

        # act
        biblioteca.pesquisar_livro(livro)
        # executando a ação de pesquisar livro

        # assert
        self.assertIn(livro, biblioteca.acervo)
        # testa se o livro pesquisado está no acervo da Biblioteca

    def teste_pesquisar_livro_nao_cadastrado_nao_deve_passar(self):
        # verifica se ao pesquisar um livro não cadastrado  o método informa que o livro não foi encontrado

        # arrange
        biblioteca = Biblioteca()
        # criando a variável biblioteca que chama a classe Biblioteca
        
        titulo_livro = "Capitu"
        autor_livro = "Machado de Assis"
        ano_livro = "1998"
        # criando as variáveis para executar os testes

        livro = Livro(titulo_livro, autor_livro, ano_livro)
        # criando a variável que chama a classe Livro

        # act
        biblioteca.pesquisar_livro(livro)
        # executando a ação de pesquisar livro

        # assert
        self.assertNotIn(livro, biblioteca.acervo)
        # testa se o livro pesquisado não pertence ao acervo da Biblioteca

    def teste_emprestar_livro_deve_passar(self):
        # verifica se o livro pode ser emprestado

        # arrange
        biblioteca = Biblioteca()
        # criando a variável biblioteca que chama a classe Biblioteca
        
        titulo_livro = "Capitu"
        autor_livro = "Machado de Assis"
        ano_livro = "1998"
        esta_emprestado = False
        # criando as variáveis para executar os testes

        livro = Livro(titulo_livro, autor_livro, ano_livro)
        # criando a variável que chama a classe Livro

        biblioteca.adicionar_livro(livro)
        # adicionado o livro ao acervo da Biblioteca

        # act
        biblioteca.emprestar_livro(livro)
        # executando a ação de emprestar livro

        #assert
        self.assertIn(livro, biblioteca.acervo)
        #testa se o livro pertence ao acervo
        self.assertFalse(esta_emprestado)
        # testa se o livro está disponívelno acervo para ser emprestado
    
    def teste_emprestar_livro_emprestado_nao_deve_passar(self):
        # verifica se o livro não pode ser emprestado

        # arrange
        biblioteca = Biblioteca()
        # criando a variável biblioteca que chama a classe Biblioteca
        
        titulo_livro = "Capitu"
        autor_livro = "Machado de Assis"
        ano_livro = "1998"
        esta_emprestado = True
        # criando as variáveis para executar os testes

        livro = Livro(titulo_livro, autor_livro, ano_livro)
        # criando a variável que chama a classe Livro

        biblioteca.adicionar_livro(livro)
        # adicionado o livro ao acervo da Biblioteca

        # act
        biblioteca.emprestar_livro(livro)
        # executando a ação de emprestar livro

        #assert
        self.assertIn(livro, biblioteca.acervo)
        #testa se o livro pertence ao acervo
        self.assertTrue(esta_emprestado)
        # testa se o livro já está emprestado
    
    def teste_devolver_livro_deve_passar(self):
        # verifica se o livro pode ser devolvido

        # arrange
        biblioteca = Biblioteca()
        # criando a variável biblioteca que chama a classe Biblioteca
        
        titulo_livro = "Capitu"
        autor_livro = "Machado de Assis"
        ano_livro = "1998"
        esta_emprestado = True
        # criando as variáveis para executar os testes

        livro = Livro(titulo_livro, autor_livro, ano_livro)
        # criando a variável que chama a classe Livro

        biblioteca.adicionar_livro(livro)
        # adicionado o livro ao acervo da Biblioteca

        # act
        biblioteca.devolver_livro(livro)
        # executando a ação de devolver livro

        # assert
        self.assertTrue(livro in biblioteca.acervo and esta_emprestado)
        # testa se o livro pertence ao acervo da biblioteca e está emprestado podendo ser devolvido
    
    def teste_devolver_livro_nao_emprestado_nao_deve_passar(self):
        # verifica se o livro a ser devolvido consta como não emprestado

        # arrange
        biblioteca = Biblioteca()
        # criando a variável biblioteca que chama a classe Biblioteca
        
        titulo_livro = "Capitu"
        autor_livro = "Machado de Assis"
        ano_livro = "1998"
        esta_emprestado = False
        # criando as variáveis para executar os testes

        livro = Livro(titulo_livro, autor_livro, ano_livro)
        # criando a variável que chama a classe Livro

        biblioteca.adicionar_livro(livro)
        # adicionado o livro ao acervo da Biblioteca

        # act
        biblioteca.devolver_livro(livro)
        # executando a ação de devolver livro

        # act
        self.assertIn(livro, biblioteca.acervo)
        # testa se o livro pertence ao acervo da Biblioteca
        self.assertFalse(esta_emprestado)
        # testa se o livro consta como não emprestado não podendo ser devolvido

    def teste_devolver_livro_nao_cadastrado_nao_deve_passar(self):
        # verifica se o livro foi devolvido faz parte do acervo

        # arrange
        biblioteca = Biblioteca()
        # criando a variável biblioteca que chama a classe Biblioteca
        
        titulo_livro = "Capitu"
        autor_livro = "Machado de Assis"
        ano_livro = "1998"
        # criando as variáveis para executar os testes

        livro = Livro(titulo_livro, autor_livro, ano_livro)
        # criando a variável que chama a classe Livro

        # act
        biblioteca.devolver_livro(livro)
        # executando a ação de devolver livro

        # assert
        self.assertNotIn(livro, biblioteca.acervo)
        # testa se o livro não pertence ao acervo da biblioteca
