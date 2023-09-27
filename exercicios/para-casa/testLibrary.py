from unittest import TestCase
from Library import Library
from Book import Book

class TestLibrary(TestCase):
    #Arrange / Act
    library = Library()
    def setUp(self):
        self.library = Library()
        
    def test_unit_must_pass(self):
        #Arrange / Act
        #library = Library()
        
        #Asset
        self.assertIsInstance(self.library.books, list)
        
    def test_add_book_must_pass(self):
        #Arrange
        #library = Library
        book_name = "O mito da Beleza"
        book_author = "Naomi Wolf"
        book_year = "1996"
        book_comentary = "Bla"
        book = Book(book_name, book_author, book_year, book_comentary)
        
        #Act
        self.library.add_book(book)
        
        #Assert
        self.assertEqual(1, len(self.library.books))
        
    def test_add_book_not_must_insert_number(self):
        #Arrange
        #library = Library()
        book = 1988
        
        #Act / Assert
        with self.assertRaises(TypeError):
            self.library.add_book(book)