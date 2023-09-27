class Livro:
    """Classe biblioteca.
    
    Recebe no construtor os parametros nome e autor como o exemplo:
    
    livro = Livro("nome livro","autor livro")
    """
    def __init__(self, nome_livro, autor_livro):        
        self.nome_livro = nome_livro
        """propriedade nome do livro"""
        self.autor_livro = autor_livro
        """propriedade autor do livro"""
        self.esta_emprestado = False
        """propriedade esta_emprestado. Valor padrão é falso"""
