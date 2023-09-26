class Livro:
    """
    Classe que representa um livro.

    Atributos:
        titulo (str): O título do livro.
        autor (str): O autor do livro.
        esta_emprestado (bool): Indica se o livro está emprestado.
    """

    def __init__(self, titulo, autor):
        """
        Inicializa uma instância do Livro.

        Args:
            titulo (str): O título do livro.
            autor (str): O autor do livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.esta_emprestado = False
