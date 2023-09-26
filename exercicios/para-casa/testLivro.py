# Importações necessárias para criar os testes
from unittest import TestCase
from Livro import Livro

# Classe de teste para a classe Livro
class TestLivro(TestCase):
    # Teste para garantir que a inicialização de um livro ocorra sem erros
    def test_init_deve_passar(self):
        # Arrange (Preparação): Defina os valores iniciais
        nome = "Calibã e a bruxa"
        autor = "Silvia Federici"
        
        # Act (Ação): Crie uma instância de Livro com os valores preparados
        livro = Livro(nome, autor)
        
        # Assert (Verificação): Verifique se os atributos da instância têm os valores esperados
        self.assertEqual(nome, livro.nome)  # Verifica se o nome do livro está correto
        self.assertEqual(autor, livro.autor)  # Verifica se o autor do livro está correto
        self.assertEqual(False, livro.esta_emprestado)  # Verifica se o livro não está emprestado inicialmente (valor False)
