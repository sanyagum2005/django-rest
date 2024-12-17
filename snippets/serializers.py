from rest_framework import serializers
from snippets.models import Book

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150)
    author = serializers.CharField(max_length=100)
    published_date = serializers.DateField()
    isbn = serializers.CharField(max_length=13, required=True)
    summary = serializers.CharField()
    genre = serializers.CharField(max_length=50, required=False)

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