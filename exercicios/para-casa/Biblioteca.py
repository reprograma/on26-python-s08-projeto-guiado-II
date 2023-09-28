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
        return f"O {livro_objeto.nome}, do(a) autor(a) {livro_objeto.autor} foi adicionado ao catálogo da biblioteca."

    #Criar método exibir_livros
    def exibir_livro(self):
        return [livro.nome for livro in self.livros]
        
    #Criar método emprestar_livro
    def emprestar_livro(self, livro: Livro):
        if livro in self.livros:
            if livro.esta_emprestado:
                return f"{livro.nome} já está emprestado."
            else:
                livro.esta_emprestado = True
                return f"{livro.nome} foi emprestado a você."
        else:
            return f"Livro não existente no catálogo."

nome_livro = "O mito da beleza"
autor_livro = "Naomi Wolf"

# Instanciando o objeto livro_objeto da classe Livro, passando as variáveis nome_livro e autor_livro
livro_objeto = Livro(nome = nome_livro, autor = autor_livro)
print(f"Criamos o objeto livro_objeto da classe Livro com os valores nome = {livro_objeto.nome} e autor = {livro_objeto.autor}\n")

# Instanciando o objeto biblioteca_objeto da classe Biblioteca 
biblioteca_objeto = Biblioteca()

# Cadastrando o livro criado anteriormente no objeto livro_objeto
# passamos o objeto livro_objeto para o método adicionar_livro do objeto biblioteca_objeto
# que por sua vez adiciona o objeto livro_objeto na lista de livros
biblioteca_objeto.adicionar_livro(livro_objeto)
      
# Exibe o livro adicionado ao acervo
for livro in biblioteca_objeto.livros:
    print(f"O livro {livro.nome} do(a) autor(a) {livro.autor} foi adicionado ao acervo")

print(f"A lista de livros contidos na biblioteca é:\n{biblioteca_objeto.exibir_livro()}")

print(biblioteca_objeto.emprestar_livro(livro_objeto))

biblioteca_objeto.emprestar_livro(livro_objeto)
