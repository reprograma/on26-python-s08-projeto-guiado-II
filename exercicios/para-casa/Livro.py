# Definição da classe Livro
class Livro:
    # Método de inicialização da classe, chamado quando um novo objeto Livro é criado
    def __init__(self, nome, autor):
        # Atribui o nome do livro ao atributo 'nome'
        self.nome = nome 
        # Atribui o autor do livro ao atributo 'autor'
        self.autor = autor
        # Inicializa o atributo 'esta_emprestado' como False, indicando que o livro não está emprestado inicialmente
        self.esta_emprestado = False
