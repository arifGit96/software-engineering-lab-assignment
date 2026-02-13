from django.contrib import admin
from .models import IssueBook

@admin.action(description="Mark selected books as returned")
def mark_as_returned(modeladmin, request, queryset):
    for obj in queryset:
        obj.mark_returned()

@admin.register(IssueBook)
class IssueBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'issue_date', 'return_date')
    actions = [mark_as_returned]
