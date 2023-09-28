from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro

class TestLivro(TestCase):
  def setUp(self):
      self.biblioteca = Biblioteca()

  def test_init_deve_passar(self):
        # Arrange
        nome = "Calibã e a bruxa"
        autor = "Silvia Federici"
        # Act
        livro = Livro(nome, autor)
        # Assert
        self.assertEqual(nome, livro.nome)
        self.assertEqual(autor, livro.autor)
        self.assertEqual(False, livro.esta_emprestado)
  
  def test_emprestar_livro_deve_marcar_como_emprestado(self):
      # Arrange
      nome_do_livro = "Aura"
      autor_do_livro = "Carlos Fuentes"
      livro = Livro(nome_do_livro, autor_do_livro)
      self.biblioteca.adicionar_livro(livro) #Add livro à lista

       # Act
      emprestado = self.biblioteca.emprestar_livro(nome_do_livro)

      # Assert
      self.assertTrue(emprestado)  # Verifica se o empréstimo funcionou e se o livro está marcado como emprestado
      self.assertTrue(livro.esta_emprestado)