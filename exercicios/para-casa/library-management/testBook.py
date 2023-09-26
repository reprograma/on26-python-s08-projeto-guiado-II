# Room
from unittest import TestCase
from book import Book

class TestBook(TestCase):
    def test_init_must_pass(self):
        # Arrange
        title = "Harry Potter and the Philosopher's stone"
        author = "J.K. Rownlig"
        # Act
        book = Book(title, author)
        # Assert
        self.assertEqual(title, book.title)
        self.assertEqual(author, book.author)
        self.assertEqual(False, book.is_borrowed)