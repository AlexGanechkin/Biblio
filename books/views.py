from django.db.migrations import serializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from books.models import Author, Book
from books.serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer, \
    BookUpdateSerializer, BookDestroySerializer, AuthorDetailSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer


class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDestroySerializer
