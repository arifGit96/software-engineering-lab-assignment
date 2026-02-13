from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from django.utils import timezone

class IssueBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Reduce quantity only on first issue
        if not self.pk:
            if self.book.quantity > 0:
                self.book.quantity -= 1
                self.book.save()
        super().save(*args, **kwargs)

    def mark_returned(self):
        if self.return_date is None:
            self.return_date = timezone.now().date()
            self.book.quantity += 1
            self.book.save()
            self.save()

    def fine_amount(self):
        if self.return_date:
            days = (self.return_date - self.issue_date).days
        else:
            days = (timezone.now().date() - self.issue_date).days

        if days > 7:
            return (days - 7) * 10
        return 0

    def __str__(self):
        return f"{self.book.title} → {self.user.username}"
