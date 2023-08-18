from django.urls import path, include

from readers.views import ReaderListView, ReaderDetailView, ReaderCreateView, ReaderUpdateView, ReaderDeleteView

urlpatterns = [
    path('', ReaderListView.as_view()),
    path('<int:pk>/', ReaderDetailView.as_view()),
    path('create/', ReaderCreateView.as_view()),
    path('<int:pk>/update/', ReaderUpdateView.as_view()),
    path('<int:pk>/delete/', ReaderDeleteView.as_view()),
]
