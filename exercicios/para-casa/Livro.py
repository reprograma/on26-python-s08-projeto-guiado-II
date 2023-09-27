class Livro:

    def __init__(self, titulo_livro, autor_livro, ano_livro):     # método construtor da classe
        """Classe Livro (tem como atributos: nome do livro, autor do livro e status do livro)"""
        
        self.tituloLivro = titulo_livro
        """nome (str): propriedade da classe Livro"""
        self.autorLivro = autor_livro
        """autor (str): propriedade da classe Livro"""
        self.anoLivro = ano_livro
        """ano (str): propriedade da classe Livro"""
        self.estaEmprestado = False     # por padrão, quando o livro é adicionado, ele não está emprestado
        """status (bool): propriedade da classe Livro"""
