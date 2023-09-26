class Biblioteca:
    """
    Classe que representa uma biblioteca.

    Atributos:
        livros (list): Uma lista de objetos Livro na biblioteca.
    """

    def __init__(self):
        """
        Inicializa uma instância da Biblioteca.
        """
        self.livros = []

    def adicionar_livro(self, livro):
        """
        Adiciona um livro à biblioteca.

        Args:
            livro (Livro): O objeto Livro a ser adicionado.
        """
        self.livros.append(livro)

    def emprestar_livro(self, titulo):
        """
        Marca um livro como emprestado.

        Args:
            titulo (str): O título do livro a ser emprestado.
        """
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.esta_emprestado = True

    def exibir_livros(self):
        """
        Retorna uma lista dos títulos dos livros na biblioteca.

        Returns:
            list: Uma lista de strings representando os títulos dos livros na biblioteca.
        """
        return [livro.titulo for livro in self.livros]
