class Livro:
    def __init__(self, nome, autor, emprestado = False): # parâmetros que a classe vai receber
        self.nome = nome
        self.autor = autor
        self.esta_Emprestado = emprestado # valor padrão do começo 