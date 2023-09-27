from Book import Book

class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book: Book):
        if (not isinstance(book,Book)):
            raise TypeError(f"Esperado livro, obtido valor {book} do tipo {type(book)}")
        self.books.append(book)
        
    def showBooks(self):
        return self.books

    def borrowBook(self, name, book: Book):
        for book in self.books:
            if book.name == name:
                book.IsBorrowed = True
                return book
                
    def removeBook(self, name, book: Book):
        for book in self.books:
            if book.name == name:
                self.books.remove(book)
                   

        