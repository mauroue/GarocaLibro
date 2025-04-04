from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'author'] 