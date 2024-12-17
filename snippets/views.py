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

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView, BookMixin):
    serializer_class = BookSerializer

    def get_object(self):
        return self.get_object(self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        book = self.get_object()
        not_found_response = self.handle_not_found(book)
        if not_found_response:
            return not_found_response
        
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        book = self.get_object()
        not_found_response = self.handle_not_found(book)
        if not_found_response:
            return not_found_response

        serializer = self.get_serializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        book = self.get_object()
        not_found_response = self.handle_not_found(book)
        if not_found_response:
            return not_found_response
            
        serializer = self.get_serializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        not_found_response = self.handle_not_found(book)
        if not_found_response:
            return not_found_response

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)