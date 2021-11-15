from django.shortcuts import render, HttpResponse, get_object_or_404
from . models import Book, Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import StudentSerializer, BookSerializer

# Creating Request View.
def test_view(request):
    my_books = Book.objects.all()
    context = {
        'books':my_books
    }
    return render(request, 'test.html', context)

class StudentList(APIView):
    """StudentList APIView"""
    def get(self, request):
        all_students = Student.objects.all()
        serializer = StudentSerializer(all_students, many=True)
        return Response(serializer.data)
    
class BookList(APIView):
    """BookList APIView"""
    def get(self, request):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)

    