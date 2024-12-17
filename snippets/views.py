from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
from accounts.permissions import IsOwner


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]  # Доступ только для аутентифицированных пользователей


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

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

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        book = Book.objects.get(pk=self.kwargs['pk'])
        return book

    def get(self, request, *args, **kwargs):
        book = self.get_object()
        if book is None:
            return Response({'message': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        book = self.get_object()
        if book is None:
            return Response({'message': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        if book is None:
            return Response({'message': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)