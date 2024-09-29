from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import TransactionBorrowBook, Book, Borrower
from datetime import datetime, timedelta
from django.core.paginator import Paginator


def index(request):
    if request.user.is_authenticated:
        filter_status = request.GET.get("filter_status")
        if filter_status is None:
            filter_status = 'all'
        
        if filter_status == 'all':
            transactions_borrow_book = TransactionBorrowBook.objects.select_related('book').select_related('borrower').exclude(status='cancel').order_by('borrow_date')
        else:
            transactions_borrow_book = TransactionBorrowBook.objects.select_related('book').select_related('borrower').filter(status=filter_status).exclude(status='cancel').order_by('borrow_date')
        pagination = Paginator(transactions_borrow_book,5)

        page_number = request.GET.get("page")
        if page_number is None:
            page_number = 1
        page = pagination.page(page_number)

        dateNow = datetime.today()
        context = {
            "page" : page,
            "filter_status" : filter_status,
            "dateNow": dateNow
        }
        return render(request, "pinjamBuku/index.html", context)
    else:
        return redirect("/accounts/login/")

def update_status_transaction(request):
    transaction_id = request.POST['id']
    page_number = request.POST['page_number']
    status = request.POST['status']
    transaction = TransactionBorrowBook.objects.filter(pk=transaction_id).update(status=status)

    return redirect(f"/pinjamBuku/?page={page_number}")

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
                "bookid": int(book),
                "borrowerid": int(borrower), 
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