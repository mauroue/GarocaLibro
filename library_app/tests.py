from django.test import TestCase
from .models import Book

class BookTestCase(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(title="Test Book", author="Author")
        self.assertEqual(book.quantity, 1) 