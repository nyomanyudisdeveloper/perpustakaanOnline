from django.db import models
from datetime import date

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Borrower(models.Model):
    full_name = models.CharField(max_length=200)
    identity_number = models.CharField(max_length=50)
    birth_date = models.DateField()
    home_place = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

class TransactionBorrowBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    returned_date = models.DateField()
    status = models.CharField(max_length=20)
    admin = models.IntegerField(default=-2)

    def __str__(self):
        return self.book
    
    @property
    def is_past_deadline(self):
        return date.today() > self.returned_date 

 
