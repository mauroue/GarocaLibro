from django.test import TestCase
from .models import Book

class BookTestCase(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(title="Test Book", author="Author")
        self.assertEqual(book.quantity, 1) 
    
    # Should add more tests for other functionality
    def test_book_availability(self):
        book = Book.objects.create(title="Test Book", author="Author", quantity=0)
        self.assertFalse(book.is_available())
        
        book.quantity = 1
        book.save()
        self.assertTrue(book.is_available()) 