from django.urls import path
from .views import my_books

urlpatterns = [
    path('my-books/', my_books, name='my_books'),
]
