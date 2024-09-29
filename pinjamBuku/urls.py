from django.urls import path

from . import  views

app_name = 'pinjamBuku'

urlpatterns = [
    path("",views.index, name="index"),
    path("addTransaction/", views.add_transaction, name="addTransaction"),
    path("updateStatusTransaction/", views.update_status_transaction, name="updateStatusTransaction")
]

