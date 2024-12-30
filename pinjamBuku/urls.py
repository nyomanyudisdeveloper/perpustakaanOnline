from django.urls import path

from . import  views

app_name = 'pinjamBuku'

urlpatterns = [
    path("",views.index, name="index"),
    path("book/", views.book, name="book"),
    path("addTransaction/", views.add_transaction, name="addTransaction"),
    path("updateStatusBook/",views.update_status_book,name="updateStatusBook"),
    path("updateStatusTransaction/", views.update_status_transaction, name="updateStatusTransaction")
]

