'''
## Sistema de gerenciamento de biblioteca
Criar um sistema de gerenciamento de biblioteca usando TDD com as funcionalidades:
- Adicionar livros
- Listar livros
- Emprestar livros

Criar método exibir_livros
- O método deve ter ao menos 1 (um) teste associado
- O método deve não tem parâmetro além do self (contém apenas o self obrigatório)
- O método deve exibir todos os livros que foram adicionados (dica retorne a lista e valide se contém todos os livros adicionados)

Criar método emprestar_livro
- O método deve ter ao menos 1 (um) teste associado
- O método deve receber como parâmetro o nome do livro a ser emprestado
- O método deve marcar o valor de esta_emprestado como True
'''

class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.esta_emprestado = False

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro)):
            raise TypeError(f"Esperado Livro, obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro)

    #Criar método exibir_livros
    def exibir_livro(self):
        return self.livros
        
    #Criar método emprestar_livro
    def emprestar_livro(self, livro: Livro):
        if livro.nome not in self.livros:
            print(f"Livro não existente no catálogo.")
        else:
            if livro.esta_emprestado == True:
                print(f"{livro.nome} já está emprestado.")
            else:
                livro.esta_emprestado = True


nome_livro = "O mito da beleza"
autor_livro = "Naomi Wolf"
livro_objeto = Livro(nome = nome_livro, autor = autor_livro)

biblioteca_objeto = Biblioteca()

print(biblioteca_objeto.livros)

for livro in biblioteca_objeto.livros:
    print(livro.nome)
    print(livro.autor)