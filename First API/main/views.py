from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import StudentSerializer, BookSerializer
from . models import Student, Book

@api_view(['GET', 'POST'])
def students(request):
    """Student APIView Function"""
    if request.method =='GET':
        all_students = Student.objects.all()
        serializer = StudentSerializer(all_students, many=True)
        data = {
            'message':'Success!',
            'data':serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)
    elif request.method =='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message":"Success",
                "data": serializer.data
            }
        else:
            error = {
                "message":"Failed",
                "error": serializer.errors
            }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET','POST'])   
def books(request):
    """Book APIViews Function"""
    if request.method == 'GET':
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        data = {
            "message": "Success!",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message":"Success",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            error = {
                "message":"Failed",
                "error": serializer.errors
            }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)