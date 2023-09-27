from unittest import TestCase
from Library import Library
from Book import Book

class testLibrary(TestCase):
    def setUp(self):
        self.library = Library()

    def testInitSucess(self):
        #Arrange / Act
        
        # Assert
        self.assertIsInstance(self.library.books, list)

    def testAddBookSucess(self):
        #Arrange
        
        nameBook = "A Game of Thrones"
        authorBook = "George RR Martin"
        book = Book(nameBook, authorBook)
        #Act
        self.library.addBook(book)
        #Assert
        self.assertEqual(1, len(self.library.books))

    def testAddBookNotNumbers(self):
        #Arrange
        
        book = 2005
        #Act/Assert
        with self.assertRaises(TypeError):
            self.library.addBook(book)

    def testShowBook(self):
        book01 = Book("A Clash of Kings", "George RR Martin")
        book02 = Book("A Storm of Swords", "George RR Martin")
        self.library.addBook(book01)
        self.library.addBook(book02)

        books = self.library.showBooks()

        self.assertEqual(2, len(books))
        self.assertIn(book01, book02)
        self.assertIn(book02, book01)

    def testBorrowBook(self):
        nameBook = "A Dance with Dragons"
        nameAuthor = "George RR Martin"
        book= Book(nameBook, nameAuthor)
        self.library.addBook(book)

        borrowed = self.library.borrowBook(nameBook, nameAuthor)

        self.assertTrue(borrowed)
        self.assertTrue(book.isBorrowed)