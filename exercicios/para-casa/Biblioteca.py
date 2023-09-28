from Livro import Livro

class Biblioteca : 
    def __init__(self): #Construtor 
        self.livros = [] #Lista de livros vazia
        
    def adicionar_livro(self, livro: Livro):
        if (not isinstance(livro, Livro) ):
            raise TypeError(f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")
        self.livros.append(livro) #Caso o valor seja válido, add o livro à lista self.livros 
    
    def exibir_livros(self): #Função que retorna a lista
        # return [livro.nome for livro in self.livros] << isso exibiria apenas os nomes
        return self.livros #Retornar a lista self.livros encontrada em __init__
    
    def emprestar_livro(self, nome_do_livro):
        for livro in self.livros: #Para cada livro em self.livros
            if livro.nome == nome_do_livro: #Se o nome do livro for igual à variável que eu criei nome_do_livro, ou seja, se ele existe
                if not livro.esta_emprestado: #E se ele já não foi emprestado
                    livro.esta_emprestado = True #Agora ele será emprestado
                    return True #Aqui a gente indica que o empréstimo foi bem sucedido
                return False #Se o livro foi emprestado, o empréstimo não será bem sucedido
            return False #Se o nome não for igual ao nome de um livro existente na lista, ele será falso 


    