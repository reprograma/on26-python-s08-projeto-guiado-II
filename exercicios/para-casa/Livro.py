class Livro:    # criando a classe livros, que vai ser usado dentro dos métodos da classe de biblioteca
    def __init__(self, nome, autor, ano): # método construtor INIT para definir as propriedades ou atribuições da nossa classe
                                        # self é uma função que vai ajudar a chamar a atribuição     
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.esta_emprestado = False  # estar_emprestado recebe uma palavra reservada(false/true, nesse caso)

    # módulos só é modulo quando tem um init.py(todos os arquivos denro se tornam modulos)