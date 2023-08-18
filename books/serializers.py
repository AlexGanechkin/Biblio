
from rest_framework import serializers

from books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(read_only=True, slug_field='last_name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'page_number', 'books_number', 'author']


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Book
        fields = '__all__'

    def validate_author(self, author):
        if author.id == 2:
            raise serializers.ValidationError('Нет автора с таким id')


class BookUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['books_number']

    # def validate_books_number(self, data):
    #     if data < 0:
    #         raise serializers.ValidationError('НЕ для тебя эта книга')
    #     return data


class BookDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id']
