from Book import Book

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book: Book):
        if (not isinstance(book, Book)):
            raise TypeError(f"Esperado Livro obtido valor {book} do tipo {type(book)}")
        self.books.append(book)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #     self.books = []
        
    # def add_books(self, book: Book):
    #     if(isinstance(book) != Book)
    #         raise TypeError(f"Esperado Livro obtido valor {book} do tipo {type(book)}")
    #     self.books.append(book)