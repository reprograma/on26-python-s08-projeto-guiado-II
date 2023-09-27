from unittest import TestCase
from Book import Book
from Library import Library

class TestShowBooks(TestCase):
    def test_init_show_books(self):
        self.show_books= []
        
        name = "The Lion King:The Gift"
        author = "Beyoncé Carter Knowles"
        year = "2019"
        comentary = "Beyoncé called the album sonic cinema and said that the film is a new experience of storytelling, and that the album is influenced by everything from R&B, pop, hip hop and Afrobeats. Beyoncé also said that wanted to put everyone on their own journey to link the storyline and that the songs were inspired by the remake's storyline, which gives the listener a chance to imagine their own imagery, while listening to a new contemporary interpretation. The songs were also produced by African producers, which Beyoncé said was because authenticity and heart were important to, since the film is set in Africa."

        book = Book(name, author, year, comentary)

        self.assertEqual(name, book.name)
        self.assertEqual(author, book.author)
        self.assertEqual(year, book.year)
        self.assertEqual(comentary, book.comentary)