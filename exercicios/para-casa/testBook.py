from unittest import TestCase
from Book import Book

class testBook(TestCase):
    def testInitSucess(self):
        #Arrange
        name = "A Game of Thrones"
        author = "George RR Martin"
        #Act
        book = Book(name, author)
        #Assert
        self.assertEqual(name, book.name)
        self.assertEqual(author, book.author)
        self.assertEqual(True, book.isBorrowed)