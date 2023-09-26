# Room
from unittest import TestCase
from library import Library
from book import Book

class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library()

    def test_init_must_pass(self):
        # Assert
        self.assertIsInstance(self.library.books, list)
    
    def test_add_must_pass(self):
        # Arange
        book_title = "New Moon"
        book_author = "Sthephanie Meyer"
        book = Book(book_title, book_author)
        # Act
        self.library.add_book(book)
        # Assert
        self.assertEqual(1, len(self.library.books))

    def test_add_book_must_not_insert_numbers(self):
        # Arrange
        book = 1988
        # Act / Assert
        with self.assertRaises(TypeError):
            self.library.add_book(book)
# Home
# New test for display
    def test_display_available_books(self):
        # Arange
        book_title = "New Moon"
        book_author = "Sthephanie Meyer"
        book = Book(title=book_title, author=book_author)
        self.library.add_book(book)
        # Act
        available_books = self.library.display_books()
        # Assert
        self.assertListEqual(available_books, [book])

    def test_display_list_empty(self):
        # Act
        empty_books = self.library.display_books()

        # Assert
        self.assertListEqual(empty_books, [])  # A lista deve estar vazia

#New test for lend   
    def test_lend_book_success(self):
        # Arrange
        book_title = "Harry Potter and the Philosopher's Stone"
        book_author = "J.K. Rowling"
        book = Book(book_title, book_author)
        self.library.add_book(book)

        # Act
        result = self.library.lend_book(book_title)

        # Assert
        self.assertTrue(result)  # Emprestado com sucesso
        self.assertTrue(book.is_borrowed)  # Verifica se o estado do livro foi atualizado

    def test_lend_book_already_borrowed(self):
        # Arrange
        book_title = "Pride and Prejudice"
        book_author = "Jane Austen"
        book = Book(book_title, book_author)
        self.library.add_book(book)
        self.library.lend_book(book_title)  # Empréstimo inicial

        # Act
        result = self.library.lend_book(book_title)  # Tentativa de empréstimo novamente

        # Assert
        self.assertFalse(result)  # O empréstimo deve falhar (livro já emprestado)
        self.assertTrue(book.is_borrowed)  # O estado do livro deve permanecer emprestado

    def test_lend_book_not_found(self):
        # Act
        result = self.library.lend_book("Book not found")

        # Assert
        self.assertFalse(result)  # O empréstimo deve falhar (livro não encontrado)