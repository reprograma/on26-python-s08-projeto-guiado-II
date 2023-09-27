from Livro import Livro

class Biblioteca :
    """Classe biblioteca.
    
    Para instanciar a classe utilize o exemplo:

    biblioteca = Biblioteca()
    """
    def __init__(self):
        self.livros = []
        """Propriedade livros do tipo Lista"""
    
    def adicionar_livro(self, livro: Livro):
        """Método adicionar_livro da classe Biblitoeca
        
        Recebe o parâmetro livro do tipo da classe Livro e
        adiciona na propriedade livros

        Retorna exceção caso o parâmetro recebido não seja do tipo Livro
        """
        if (not isinstance(livro, Livro) ):
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)  

    def exibir_livros(self):
        """Método exibir_livros da classe Biblioteca
        
        Exibe a lista de livros"""
        
        return self.livros

    def emprestar_livro(self, livro: Livro):        
    
        """Método emprestar_livro da classe Biblioteca
       
        Recebe o parâmetro livro do tipo da classe Livro e
        muda o valor esta_emprestado"""

        if livro in self.livros:
            i = self.livros.index(livro)
            self.livros[i].esta_emprestado = True     

        else:
            raise ValueError("Livro não encontrado na biblioteca")
        
    def remover_livro(self, livro: Livro):
        """Método remover_livro da classe Biblioteca
            
        Recebe o parâmetro livro do tipo da classe Livro e
        remove na propriedade livros
        """
        if livro in self.livros:
            i = self.livros.index(livro)
            try:
                if self.livros[i].esta_emprestado:
                    raise ValueError("Livros emprestados não podem ser removidos")
            except:
                pass
            else:
                self.livros.pop(i)
        else:
            raise ValueError("Livro não encontrado na biblioteca")
        
    def buscar_livro(self, livro: Livro):
        """Método buscar_livro da classe Biblioteca
            
        Recebe o parâmetro livro do tipo da classe Livro e
        retorna suas propriedades
        (nome do livro, autor e informação se livro está disponível ou emprestado)
        """
        if livro in self.livros:
            i = self.livros.index(livro)
            livro_buscado = self.livros[i]
            infos_livro = {
                "Nome do livro": livro_buscado.nome_livro,
                "Nome do autor": livro_buscado.autor_livro,
                "O livro está disponível?": livro_buscado.esta_emprestado
            }
            return infos_livro
        else:
            raise ValueError("Livro não encontrado na biblioteca")

    def devolver_livro(self, livro: Livro):
            """Método devolver_livro da classe Biblioteca
                
            Recebe o parâmetro livro do tipo da classe Livro e
            mudar o status do livro para não emprestado na propriedade Livros
            """
            if livro in self.livros:
                i = self.livros.index(livro)
                self.livros[i].esta_emprestado = False
            
            else:
                raise ValueError("Livro não encontrado na biblioteca")
