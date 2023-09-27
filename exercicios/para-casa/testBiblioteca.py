#__init__ inicializa os modulos
from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro
import io
from contextlib import redirect_stdout

class TestBiblioteca(TestCase):# teste case identifica que esse é o teste 
   def setUp(self):
        self.biblioteca = Biblioteca()  # biblioteca = Biblioteca()
        self.nome_livro1 = "O mito da beleza"  
        self.autor_livro1 = "Naomi Wolf"
        self.livro1 = Livro(self.nome_livro1, self.autor_livro1)
        self.biblioteca.adicionar_livro(self.livro1)
        
        self.nome_livro2 = "Onde estará Norma?"  
        self.autor_livro2 = "Miró"
        self.livro2 = Livro(self.nome_livro2, self.autor_livro2)
        self.biblioteca.adicionar_livro(self.livro2)


   def test_init_deve_passar(self):
       # Arrange
       # Assert
       self.assertIsInstance(self.biblioteca.livros, list) 
       
        # teste Metodo Adicionar Livros

   def test_adicinar_livro_deve_passar(self):
        #criar o instancia(cria) objeto na classe Livro

        # Assert
        self.assertEqual(2, len(self.biblioteca.livros))
           
   def test_adicinar_livro_nao_deve_inserir_numero(self):
        # Arrange
        self.livro = 1988    
        # Act/ Assert 
        with self.assertRaises(TypeError):    
            self.biblioteca.adicionar_livro(self.livro) 
            
        # Teste Metodo Exibir Livros
    
   def test_exibir_livros_deve_passar(self):
       
        # Criar um objeto io.StringIO para capturar a saída
        output = io.StringIO()

        """ usa redirect_stdout(output) dentro do bloco with para capturar a saída impressa pelo 
            método exibir_livros da sua classe Biblioteca. Isso permite que você verifique se a saída 
            é igual à saída esperada durante o teste, como você está fazendo com 
            self.assertEqual(output.getvalue(), expected_output)."""
        with redirect_stdout(output):
        
        #ACT
         self.biblioteca.exibir_livros()
         
        # Assert
         expected_output = "Título: O mito da beleza, Autor: Naomi Wolf\nTítulo: Onde estará Norma?, Autor: Miró\n"
         self.assertEqual(output.getvalue(), expected_output)
         self.assertEqual(2, len(self.biblioteca.livros))
       
     
        # Teste Metodo Emprestar Livros

   def test_emprestar_livro_deve_passar(self):
        # Adicione o livro à biblioteca

        # Empréstimo bem-sucedido
        self.biblioteca.emprestar_livro(self.nome_livro1)

        # Verifique se o atributo esta_emprestado do livro foi marcado como True
        self.assertTrue(self.livro1.esta_emprestado)   
        
        
   def test_emprestar_livro_ja_emprestado_deve_falhar(self):
        # Adicione o livro à biblioteca

        # Empréstimo bem-sucedido
        self.biblioteca.emprestar_livro(self.nome_livro1)

        # Tente emprestar o mesmo livro novamente (já emprestado)
        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro(self.nome_livro1)
            
            
   def test_emprestar_livro_inexistente_deve_falhar(self):
        # Tente emprestar um livro que não está na biblioteca
        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro("Nome do Livro Inexistente")    
            
            
           # Teste Metodo Remover Livros

   def test_remover_livro_deve_passar(self):
        # Adicione o livro à biblioteca

        # Remoção bem-sucedido
        self.biblioteca.remover_livro(self.nome_livro2)

        # Verifique se o atributo removido do livro foi marcado como True
        self.assertTrue(self.livro2.esta_removido)  
       
    
    
   def test_remover_livro_ja_removido_deve_falhar(self):
        # Adicione o livro à biblioteca

        # Remoção  bem-sucedido
        self.biblioteca.remover_livro(self.nome_livro2)

        # Tente remover o mesmo livro novamente (já removido)
        with self.assertRaises(ValueError):
            self.biblioteca.remover_livro(self.nome_livro2)
            

   def test_remover_livro_inexistente_deve_falhar(self):
        # Tente remover um livro que não está na biblioteca
        with self.assertRaises(ValueError):
            self.biblioteca.remover_livro("Nome do Livro Inexistente")  
    
             
    # Teste Metodo Buscar Livros

   def test_buscar_livro_deve_passar(self):
        # Adicione o livro à biblioteca

        # Busca bem-sucedida
        self.biblioteca.buscar_livro(self.nome_livro1)

        # Verifique se o atributo encontrado do livro foi marcado como True
        self.assertTrue(self.livro1.encontrado)             
        
     
   def test_buscar_livro_ja_encontrado_deve_falhar(self):
        # Adicione o livro à biblioteca

        # Localização bem-sucedido
        self.biblioteca.buscar_livro(self.nome_livro1)

        # Tente buscar o mesmo livro novamente (já encontrado)
        with self.assertRaises(ValueError):
            self.biblioteca.buscar_livro(self.nome_livro1)
            
            

   def test_buscar_livro_inexistente_deve_falhar(self):
      # Tente buscar um livro que não está na biblioteca
        with self.assertRaises(ValueError):
            self.biblioteca.buscar_livro("Nome do Livro Inexistente") 
            
      # Teste Metodo Devolver Livros

   def test_devolver_livro_deve_passar(self):
        # Adicione o livro à biblioteca

        # Devolução bem-sucedida
        self.biblioteca.devolver_livro(self.nome_livro2)

        # Verifique se o atributo devolvido do livro foi marcado como True
        self.assertTrue(self.livro2.devolvido)   
        
        
   def test_devolver_livro_ja_devolvido_deve_falhar(self):
        # Adicione o livro à biblioteca

        # Devolução bem-sucedida
        self.biblioteca.devolver_livro(self.nome_livro2)

        # Tente devolver o mesmo livro novamente (já devolvido)
        with self.assertRaises(ValueError):
            self.biblioteca.devolver_livro(self.nome_livro2)
            

   def test_devolver_livro_inexistente_deve_falhar(self):
        # Tente devolver um livro que não está na biblioteca
        with self.assertRaises(ValueError):
            self.biblioteca.devolver_livro("Nome do Livro Inexistente")    
            
            
   