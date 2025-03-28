from django.contrib import admin
from .models import Book, Member, Transaction

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'quantity')
    search_fields = ('title', 'author')
    list_filter = ('author',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'balance')
    search_fields = ('user__username', 'user__email', 'phone')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'issue_date', 'return_date', 'fee')
    list_filter = ('issue_date', 'return_date')
    search_fields = ('book__title', 'member__user__username') 