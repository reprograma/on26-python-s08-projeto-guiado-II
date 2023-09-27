from unittest import TestCase
from Bookstolend import BooksToLend
from Library import Library

list_books = ["Calibã", "The Lion King: The Gift",
              "The Witcher", "Nanatsu no Taizai", "The Hunger Games"]

class TestLendBook(TestCase):
    def test_init_lend_book(self):
        
        
        name = list_books
        
        book = BooksToLend(name)
        
        self.assertEqual(name, book.name)