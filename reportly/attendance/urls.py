from django.urls import path
from .views import test_view, StudentList, BookList

app_name = 'attendance'

urlpatterns = [
    path('books/', test_view, name='all_books'),
    path('api/students/', StudentList.as_view()),
    path('api/books/', BookList.as_view()),
]
