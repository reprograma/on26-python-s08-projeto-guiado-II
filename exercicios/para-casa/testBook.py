from unittest import TestCase
from Book import Book

class TestBook(TestCase):
    def test_init_must_pass(self):
    #Arrange
        name = "Calibã e a Bruxa"
        author = "Silvia Federici"
        year = "1996"
        comentary = "Bla"
    
    #Act
        book = Book(name, author, year, comentary)

    #Assert
        self.assertEqual(name, book.name)
        self.assertEqual(author, book.author)
        self.assertEqual(year, book.year)
        self.assertEqual(comentary, book.comentary)
        self.assertEqual(False, book.borrowed)