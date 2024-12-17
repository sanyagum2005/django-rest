from rest_framework import serializers
from snippets.models import Book
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail'  # Название URL для представления детали книги
    )

    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'books']

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150)
    author = serializers.HyperlinkedRelatedField(
        view_name='author-detail',  # Название URL для представления детали автора
        queryset=Author.objects.all()
    )
    published_date = serializers.DateField()
    isbn = serializers.CharField(max_length=13, required=True)
    summary = serializers.CharField()
    genre = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'genre']

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance