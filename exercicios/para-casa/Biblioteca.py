from Livro import Livro

class Biblioteca:

    def __init__(self):     # método construtor da classe
        """Classe Biblioteca (tem como propriedade uma lista de livros)"""

        # raise NotImplementedError     # levantando uma excessão para sinalizar que a classe não foi implementada

        self.acervo = []
        """acervo (lista): propriedade da classe Biblioteca"""
    
    def adicionar_livro(self, livro:Livro):     # parâmetro livro do tipo classe Livro
        """Método para adiconar um livro ao acervo da Biblioteca"""

        if not (isinstance(livro, Livro)):
            # se a propriedade livro não for igual a classe Livro apresente mensagem de erro
            raise TypeError (f"Esperado livro valor {livro} do tipo {type(livro)}")
        
        self.acervo.append(livro)
            # adicona o livro ao acervo da Biblioteca

    def exibir_acervo(self, livro:Livro):
        """Método para exibir o acervo de livros da Biblioteca"""

        for livro in self.acervo:
            return livro
            # para cada livro contido no acervo da Biblioteca: exiba os livros
     
    def remover_livro(self, livro:Livro):
        """Método para remover um livro do acervo da Biblioteca"""

        # para acessar os atributos da classe livro: livro_nomeatributo

        if livro.tituloLivro in self.acervo and livro.estaEmprestado == False: 
            # se o livro a ser excluído pertence ao acervo da Biblioteca e não está emprestado: remova o livro e informe ao usuário
                 self.acervo.remove(livro.tituloLivro)
                 return (f"O livro {livro.tituloLivro} foi removido com sucesso!")
        
        elif livro.estaEmprestado == True:
            # se o livro pertence ao acervo da Biblioteca e está emprestado: não remova e informe ao usuário
            return (f"O livro {livro.tituloLivro} está emprestado. Portanto, não pode ser removido do acervo.")
        
        else:
            livro.tituloLivro in self.acervo and livro.tituloLivro not in self.acervo
            # se o livro não pertence ao acervo da Biblioteca: informe ao usuário
            return (f"O livro {livro.tituloLivro} não foi encontrado no acervo da Biblioteca.")
    
    def pesquisar_livro(self, livro:Livro):
        """Método para pesquisar um livro no acervo da Biblioteca"""
       
        if livro.tituloLivro in self.acervo:
            # se o livro pertence ao acervo da Biblioteca: informe ao usuário os seus atributos
            return (f"Livro:{livro.tituloLivro}\nAutor:{livro.autorLivro}\nAno:{livro.anoLivro}\nStatus?{livro.estaEmprestado}")
        
        else:
            livro.tituloLivro not in self.acervo
            # se o livro não faz parte do acervo da Biblioteca: informe ao usuário
            return ("Livro não encontrado.")

    def emprestar_livro(self, livro:Livro):
        """Método para emprestar um livro do acervo da Biblioteca"""

        if livro.tituloLivro in self.acervo and livro.estaEmprestado == False:
            # se o livro pertence ao acervo da Biblioteca e não está emprestado: empreste o livro
            return livro.estaEmprestado == True
        
        else:
            livro.tituloLivro in self.acervo and livro.estaEmprestado == True
            # se o livro pertence ao acervo da Biblioteca e está emprestado: informe ao usuário
            return (f"O livro {livro.tituloLivro} já se encontra emprestado.")
    
    def devolver_livro(self, livro:Livro):
        """Método para devolver um livro emprestado ao acervo da Biblioteca"""

        if livro.tituloLivro in self.acervo and livro.estaEmprestado == True:
            # se o livro devolvido pertence ao acervo da Biblioteca e está emprestado: disponibilize no acervo 
            return livro.estaEmprestado == False
        
        elif livro.tituloLivro in self.acervo and livro.estaEmprestado == False:
            # se o livro devolvido pertence ao acervo da Biblioteca mas consta como disponível: existe um problema
            return ("!Procure a gerência para verificar essa situção!")
        
        else:
            livro.tituloLivro not in self.acervo
            # se o livro não pertence ao acervo da Biblioteca: informe ao usuário
            return ("Livro não encontrado")
    