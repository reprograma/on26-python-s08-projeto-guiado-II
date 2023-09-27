class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def exibir_livros(self):
        return self.livros


def test_exibir_livros():
    biblioteca = Biblioteca()

    livro1 = 'livro 1'
    livro2 = 'livro 2'
    livro3 = 'livro 3'

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    livros_na_biblioteca = biblioteca.exibir_livros()

    assert livro1 in livros_na_biblioteca
    assert livro2 in livros_na_biblioteca
    assert livro3 in livros_na_biblioteca

    print('teste passou com sucesso!')

test_exibir_livros()

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append({'nome': livro, 'esta_emprestado': False})

    def exibir_livros(self):
        return [livro['nome'] for livro in self.livros]

    def emprestar_livro(self, nome_livro):
        for livro in self.livros:
            if livro['nome'] == nome_livro:
                livro['esta_emprestado'] = True

def test_emprestar_livro():
    biblioteca = Biblioteca()

    livro1 = 'livro 1'
    livro2 = 'livro 2'

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    biblioteca.emprestar_livro(livro1)

    for livro in biblioteca.livros:
        if livro['nome'] == livro1:
            assert livro['esta_emprestado'] == True

    for livro in biblioteca.livros:
        if livro['nome'] == livro2:
            assert livro['esta_emprestado'] == False

    print('teste passou com sucesso!')

test_emprestar_livro()
