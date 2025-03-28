from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)  # Tracks available copies 

    def is_available(self):
        return self.quantity > 0

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def clean(self):
        if self.balance < -100:  # Prevent excessive debt
            raise ValidationError('Member balance cannot be below -100')

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_index=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_index=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    fee = models.DecimalField(max_digits=6, decimal_places=2)  # Late fees tracking 
    
    class Meta:
        indexes = [
            models.Index(fields=['issue_date', 'return_date']),
        ] 

    @property
    def days_overdue(self):
        if self.return_date:
            return (self.return_date - self.issue_date).days - 14
        return (timezone.now() - self.issue_date).days - 14 