from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookMixin:
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def handle_not_found(self, book):
        if book is None:
            return Response({'message': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)
        return None