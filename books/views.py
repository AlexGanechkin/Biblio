from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from books.models import Author, Book
from books.permissions import AuthorPermission
from books.serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer, \
    BookUpdateSerializer, BookDestroySerializer, AuthorDetailSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    permission_classes = [AuthorPermission]


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = [permissions.IsAdminUser]


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer
    permission_classes = [permissions.IsAdminUser]


class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDestroySerializer
    permission_classes = [permissions.IsAdminUser]
