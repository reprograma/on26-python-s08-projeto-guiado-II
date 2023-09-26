# Room
from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if (not isinstance(book, Book)):
            raise TypeError(f"Book is expected to be obtained from value {book} of type {type(book)}")
        self.books.append(book)
# Home
# Função que exibe a lista de livros da biblioteca
    def display_books(self):
        return self.books

# Função para emprestar livro
    def lend_book(self, title: Book): # Emprestar livro bom base no título
        for book in self.books: # Verifica cada livro na biblioteca
            if book.title == title: # Verifica se o livro na biblioteca tem o mesmo título que desejo emprestar
             if not book.is_borrowed: # Verifica se o livro não está emprestado
                book.is_borrowed = True # Indica que o livro foi emprestado com sucesso
                return True # Encerra a função quando o livro é emprestado
            else:
                return False # Retorna se o livro já tiver emprestado
        return False # encerra o loop se não encontrar nenhum livro na lista