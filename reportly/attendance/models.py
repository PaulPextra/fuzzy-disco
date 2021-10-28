from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    date_of_birth = models.DateField()
    about = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=300)
    no_of_pages = models.IntegerField(default=10)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='books')
    author = models.CharField(max_length=300)
    isbn = models.CharField(max_length=42, null=True, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    