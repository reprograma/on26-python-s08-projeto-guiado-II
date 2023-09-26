# Importação da classe Livro
from Livro import Livro

# Classe Biblioteca
class Biblioteca:
    # Método de inicialização da classe
    def __init__(self):
        # Inicializa a lista de livros como vazia
        self.livros = []
        
    # Método para adicionar um livro à biblioteca
    def adicionar_livro(self, livro: Livro):
        # Verifica se o objeto passado como livro é uma instância da classe Livro
        if not isinstance(livro, Livro):
            # Lança um erro TypeError se não for um objeto Livro
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
        
        # Adiciona o livro à lista de livros na biblioteca
        self.livros.append(livro)
    
    # Método para exibir todos os livros na biblioteca
    def exibir_livros(self):
        return self.livros
    
    # Método para emprestar um livro da biblioteca
    def emprestar_livros(self, nome_livro):
        # Itera sobre a lista de livros na biblioteca
        for livro in self.livros:
            # Verifica se o nome do livro coincide com o nome fornecido
            if livro.nome == nome_livro:
                # Marca o livro como emprestado (altera o atributo esta_emprestado)
                livro.esta_emprestado = True
                # Retorna True para indicar que o empréstimo foi bem-sucedido
                return True
        
        # Se nenhum livro com o nome fornecido for encontrado, retorna False
        return False
