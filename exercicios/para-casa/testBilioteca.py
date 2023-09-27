from unittest import TestCase
from Biblioteca import Biblioteca
from Livro import Livro         # nome do arquivo(Livro) e depois o nome da classe(Livro)
class TestBiblioteca(TestCase):
        def setUp(self):
              self.biblioteca = Biblioteca()
        def test_init_deve_passar(self):
              # Arrange / Act
              #biblioteca = Biblioteca()
             
              # Assert
              self.assertIsInstance(self.biblioteca.livros, list)

        def test_adicionar_livro_deve_passar(self):
              #Arrange
              #biblioteca = Biblioteca()
              nome_livro = "O mito da beleza"
              autor_livro = "Naomi Wolf" 
              livro = Livro(nome_livro, autor_livro)

              #Act
              self.biblioteca.adicionar_livro(livro)
              #Assert
             
              livro = Livro("Casei com um comunista", "Philip Roth")

              #Act
              self.biblioteca.adicionar_livro(livro)
              #Assert


              self.assertEqual(2, len(self.biblioteca.livros))

        def test_adicionar_livro_nao_deve_inserir_numero(self):
               
               #biblioteca = Biblioteca()
               livro = 1984

               #Act / Assert
               with self.assertRaises(TypeError):
                      self.biblioteca.adicionar_livro(livro)
        
        def test_exibir_livros_deve_passar(self):
               
          #biblioteca = Biblioteca()
          #montar uma lista
          nome_livro = "Afropessimismo"
          autor_livro = "Frank B. Wilderson III"
                         
          livro = Livro(nome_livro, autor_livro)              

          self.biblioteca.adicionar_livro(livro)

          livro = Livro("Casei com um comunista", "Philip Roth")
          self.biblioteca.adicionar_livro(livro)

          lista_de_livros_completa = self.biblioteca.exibir_livros()
          self.assertListEqual(lista_de_livros_completa, self.biblioteca.livros)

        def test_emprestar_livro_deve_passar(self):
          
           nome = "Afropessimismo"
           autor = "Frank B. Wilderson III"
                                  
           livro = Livro(nome, autor)              
           self.biblioteca.adicionar_livro(livro)
          
           self.assertTrue(self.biblioteca.emprestar_livro(livro))

        def test_remover_livro_deve_passar(self):
              
             nome_livro = "O mito da beleza"
             autor_livro = "Naomi Wolf" 
             livro = Livro(nome_livro, autor_livro)

              #Act
             self.biblioteca.adicionar_livro(livro)
                           
             livro = Livro("Casei com um comunista", "Philip Roth")

              #Act
             self.biblioteca.adicionar_livro(livro)
              #assert
             self.assertEqual(2, len(self.biblioteca.livros))

              #Act
             self.biblioteca.remover_livro(livro)
              #Assert
             self.assertEqual(1, len(self.biblioteca.livros))
             



        def test_buscar_livros_deve_passar(self):
          
          nome_livro = "Afropessimismo"
          autor_livro = "Frank B. Wilderson III"
                                  
          titulo = Livro(nome_livro, autor_livro)              
          self.biblioteca.adicionar_livro(titulo)
          
          titulo = Livro("Casei com um comunista", "Philip Roth")
          self.biblioteca.adicionar_livro(titulo)

          

          



          

        
        

                 
     
               



        
        
        
               #Act

               #Assert
      