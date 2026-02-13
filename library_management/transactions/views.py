from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import IssueBook

@login_required
def my_books(request):
    issued = IssueBook.objects.filter(user=request.user)
    return render(request, 'transactions/my_books.html', {'issued': issued})
