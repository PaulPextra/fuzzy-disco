from django.contrib import admin
from .models import Book, Student

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','no_of_pages', 'isbn', 'date']
    list_editable = ['isbn']
    list_filter = ['date']
    list_per_page = 2
    search_fields = ['title', 'author', 'body']

admin.site.register(Student)
