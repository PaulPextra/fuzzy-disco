from django.db import models
from django.utils import timezone
from datetime import datetime

def get_cohort():
    """Function for getting the cohort month & year"""
    date = timezone.now()
    cohort = datetime.strftime(date,"%B-%Y")
    return cohort


class Student(models.Model):
    """Students Model Class"""
    name = models.CharField(max_length=200)
    cohort = models.CharField(max_length=200, default=get_cohort())
    date_joined = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-date_joined',)
        
    def __str__(self):
        return self.name
    
class Book(models.Model):
    """Books Model Class"""
    title = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='books')
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    no_of_pages = models.IntegerField(default=10)
    
    class Meta:
        ordering = ('-title',)
    
    def __str__(self):
        return self.title
    
    