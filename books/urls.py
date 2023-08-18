from django.urls import path, include
from rest_framework import routers

from books.views import AuthorViewSet, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

author_router = routers.SimpleRouter()
author_router.register('author', AuthorViewSet)

urlpatterns = [
    path('', include(author_router.urls)),
    path('', BookListView.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
    path('create/', BookCreateView.as_view()),
    path('<int:pk>/update/', BookUpdateView.as_view()),
    path('<int:pk>/delete/', BookDeleteView.as_view()),
]
