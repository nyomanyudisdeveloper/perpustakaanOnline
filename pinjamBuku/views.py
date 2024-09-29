from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import TransactionBorrowBook, Book, Borrower
from datetime import datetime, timedelta


def index(request):
    if request.user.is_authenticated:
        transactions_borrow_book = TransactionBorrowBook.objects.select_related('book').select_related('borrower').exclude(status='cancel')
        dateNow = datetime.today()
        context = {
            "transactions_borrow_book" : transactions_borrow_book,
            "dateNow": dateNow
        }
        # for transaction in transactions_borrow_book:
        #     return HttpResponse(transaction.book.name)
        # return HttpResponse(transactions_borrow_book)
        return render(request, "pinjamBuku/index.html", context)
    else:
        return redirect("/accounts/login/")

def update_status_transaction(request):
    transaction_id = request.POST['id']
    status = request.POST['status']
    transaction = TransactionBorrowBook.objects.filter(pk=transaction_id).update(status=status)

    return redirect("/pinjamBuku/")

def add_transaction(request):
    if request.method == 'POST':
        book = request.POST['book']
        borrower = request.POST['borrower']
        returnDate = request.POST['returnDate']
        adminID = request.user.id
        dateNow = datetime.today().strftime('%Y-%m-%d')
        status = "still borrowed"

        error_borrower_list = []
        transaction = TransactionBorrowBook.objects.filter(borrower_id=borrower,status=status).first()
        if transaction is not None:
            error_borrower_list.append("This borrower still borrow book")
        
        error_return_date_list = []
        if datetime.strptime(returnDate,'%Y-%m-%d') < datetime.today():
            error_return_date_list.append("Return date must be greater than today")
        
        
        if len(error_borrower_list) > 0 or len(error_return_date_list):
            list_book = Book.objects.all()
            list_borrower = Borrower.objects.all()
            
            context = { 
                "list_book" : list_book, 
                "list_borrower": list_borrower,
                "bookid": book,
                "borrowerid": borrower, 
                "returnDate": returnDate, 
                "error_borrower_list": error_borrower_list,
                "error_return_date_list": error_return_date_list
            }
            return render(request,"pinjamBuku/addTransaction.html",context)
        else:
            success_message = "The transacion is success saved"
            transaction = TransactionBorrowBook(borrow_date=dateNow,returned_date=returnDate,status=status,book_id=book,borrower_id=borrower,admin=adminID)
            transaction.save()

            list_book = Book.objects.all()
            list_borrower = Borrower.objects.all()
            returnDate = datetime.today() + timedelta(days=7) 
            returnDate = returnDate.strftime('%Y-%m-%d')
            context = {
                "list_book" : list_book, 
                "list_borrower": list_borrower, 
                "returnDate" : returnDate,
                "success_message": success_message
            }
            return render(request,"pinjamBuku/addTransaction.html",context)
        
    else:
        if request.user.is_authenticated:
            list_book = Book.objects.all()
            list_borrower = Borrower.objects.all()
            returnDate = datetime.today() + timedelta(days=7) 
            returnDate = returnDate.strftime('%Y-%m-%d')
            context = {
                "list_book" : list_book, 
                "list_borrower": list_borrower, 
                "returnDate" : returnDate
            }
            return render(request,"pinjamBuku/addTransaction.html",context)
        else:
            return redirect("/accounts/login/")