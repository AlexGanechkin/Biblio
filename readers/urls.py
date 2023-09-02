from django.urls import path, include
from rest_framework.authtoken import views

from readers.views import ReaderListView, ReaderDetailView, ReaderCreateView, ReaderUpdateView, ReaderDeleteView, \
    ReaderLogout

urlpatterns = [
    path('', ReaderListView.as_view()),
    path('<int:pk>/', ReaderDetailView.as_view()),
    path('create/', ReaderCreateView.as_view()),
    path('<int:pk>/update/', ReaderUpdateView.as_view()),
    path('<int:pk>/delete/', ReaderDeleteView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', ReaderLogout.as_view()),
]
