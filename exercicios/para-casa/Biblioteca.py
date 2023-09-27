from Livro import Livro
class Biblioteca:
    def __init__(self): #self pega da classe especificada
        self.livros = []
        
        #Metodo Adicionar
    def adicionar_livro(self, livro):
        if(not isinstance(livro, Livro)):
         raise TypeError( f"Esperado Livro obtido valor {livro} do tipo {type(livro)}")    

        self.livros.append(livro)
        #raise NotImplementedError   
        
           #Metodo Exibir
    def  exibir_livros (self):
     #for livro in Biblioteca.livros: # percorre a lista 
        for livro in self.livros:
            print(f"Título: {livro.nome}, Autor: {livro.autor}")
            
        
            #Metodo Emprestar
    def emprestar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                if  livro.esta_emprestado:
                    raise ValueError("Livro está emprestado. selecione outro exemplar")
                livro.esta_emprestado = True
                return
                
        raise ValueError("Livro não encontrado na biblioteca")
    
                
                #Metodo Remover
    def remover_livro(self, nome_livro):
     for livro in self.livros:
        if livro.nome == nome_livro:
            if livro.esta_removido:
                raise ValueError("Livro já foi removido. Selecione outro exemplar")
            self.livros.remove(livro)
            livro.esta_removido = True  # Defina esta flag como True após a remoção
            return f"Nome: {livro.nome}, Autor: {livro.autor}, Removido: {livro.esta_removido}"
             
     raise ValueError("Livro não encontrado na biblioteca")

    
                #Metodo Buscar
    def buscar_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                if livro.encontrado:
                    raise ValueError("Livro já foi encontrado. Não é possível encontrá-lo novamente.")
                livro.encontrado = True
                return f"Nome: {livro.nome}, Autor: {livro.autor}, Emprestado: {livro.esta_removido}"
        raise ValueError("Livro não encontrado na biblioteca")
    
               
                #Metodo Devolver
    def devolver_livro(self, nome_livro):
        for livro in self.livros:
            if livro.nome == nome_livro:
                if livro.devolvido:
                    raise ValueError("Livro já foi devolvido anteriormente.")
                livro.devolvido = True
                return
        raise ValueError("Livro não encontrado na biblioteca")


        